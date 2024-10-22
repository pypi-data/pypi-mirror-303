import math
import torch
import torch.nn.functional as F
from torch import nn
from VisionDiff.rotary import RotaryEmbedding

class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6, elementwise_affine=True, memory_efficient=False):
        super().__init__()
        self.dim = dim
        self.eps = eps
        self.elementwise_affine = elementwise_affine
        if self.elementwise_affine:
            self.weight = nn.Parameter(torch.ones(dim))
        else:
            self.register_parameter('weight', None)

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        output = self._norm(x.float()).type_as(x)
        if self.weight is not None:
            output = output * self.weight
        return output

    def extra_repr(self) -> str:
        return f'dim={self.dim}, eps={self.eps}, elementwise_affine={self.elementwise_affine}'

class Mlp(nn.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features

        self.fc1 = nn.Linear(in_features, hidden_features, bias=True)
        self.fc2 = nn.Linear(hidden_features, out_features, bias=True)
        
        self.act =  nn.GELU(approximate="tanh")
        self.drop1 = nn.Dropout(0)
        self.drop2 = nn.Dropout(0)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop1(x)
        x = self.fc2(x)
        x = self.drop2(x)
        return x

class MultiheadDiffAttn(nn.Module):
    def __init__(self, embed_dim, num_heads = 4, depth=1, decoder_kv_attention_heads = None, model_parallel_size = 1):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads // model_parallel_size
        self.num_kv_heads = decoder_kv_attention_heads // model_parallel_size if decoder_kv_attention_heads is not None else num_heads // model_parallel_size
        self.n_rep = self.num_heads // self.num_kv_heads
        
        self.head_dim = embed_dim // num_heads // 2
        self.scaling = self.head_dim ** -0.5
        
        self.q_proj = nn.Linear(embed_dim, embed_dim, bias=False)
        self.k_proj = nn.Linear(embed_dim, embed_dim // self.n_rep, bias=False)
        self.v_proj = nn.Linear(embed_dim, embed_dim // self.n_rep, bias=False)
        self.out_proj = nn.Linear(embed_dim, embed_dim, bias=False)

        self.lambda_init = self.lambda_init_fn(depth)
        self.lambda_q1 = nn.Parameter(torch.zeros(self.head_dim, dtype=torch.float32).normal_(mean=0,std=0.1))
        self.lambda_k1 = nn.Parameter(torch.zeros(self.head_dim, dtype=torch.float32).normal_(mean=0,std=0.1))
        self.lambda_q2 = nn.Parameter(torch.zeros(self.head_dim, dtype=torch.float32).normal_(mean=0,std=0.1))
        self.lambda_k2 = nn.Parameter(torch.zeros(self.head_dim, dtype=torch.float32).normal_(mean=0,std=0.1))

        self.subln = RMSNorm(2 * self.head_dim, eps=1e-5, elementwise_affine=False)
        self.apply(self._init_weights)

        assert self.head_dim > 2, f"Attention head dim \"{embed_dim}\" divided by num heads \"{num_heads}\" cannot by ≤4!"
        self.rotary_emb = RotaryEmbedding(dim = self.head_dim, use_xpos=True)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            nn.init.constant_(m.weight, 0)

    def lambda_init_fn(self, depth):
        return 0.8 - 0.6 * math.exp(-0.3 * depth)

    def repeat_kv(self, x: torch.Tensor, n_rep: int) -> torch.Tensor:
        bs, n_kv_heads, slen, head_dim = x.shape
        if n_rep == 1:
            return x
        return (
            x[:, :, None, :, :]
            .expand(bs, n_kv_heads, n_rep, slen, head_dim)
            .reshape(bs, n_kv_heads * n_rep, slen, head_dim)
        )
    
    def forward(self, x):
        bsz, tgt_len, embed_dim = x.size()
        src_len = tgt_len

        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        q = q.view(bsz, tgt_len, 2 * self.num_heads, self.head_dim)
        k = k.view(bsz, src_len, 2 * self.num_kv_heads, self.head_dim)
        v = v.view(bsz, src_len, self.num_kv_heads, 2 * self.head_dim)

        q, k = self.rotary_emb.rotate_queries_and_keys(q, k)

        q = q.transpose(1, 2)
        k = self.repeat_kv(k.transpose(1, 2), self.n_rep)
        v = self.repeat_kv(v.transpose(1, 2), self.n_rep)
        q *= self.scaling
        attn_weights = torch.matmul(q, k.transpose(-1, -2))

        attn_weights = torch.nan_to_num(attn_weights)
        attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32).type_as(attn_weights)

        lambda_1 = torch.exp(torch.sum(self.lambda_q1 * self.lambda_k1, dim=-1).float()).type_as(q)
        lambda_2 = torch.exp(torch.sum(self.lambda_q2 * self.lambda_k2, dim=-1).float()).type_as(q)
        lambda_full = lambda_1 - lambda_2 + self.lambda_init
        attn_weights = attn_weights.view(bsz, self.num_heads, 2, tgt_len, src_len)
        attn_weights = attn_weights[:, :, 0] - lambda_full * attn_weights[:, :, 1]
        
        attn = torch.matmul(attn_weights, v)
        attn = self.subln(attn)
        attn = attn * (1 - self.lambda_init)
        attn = attn.transpose(1, 2).reshape(bsz, tgt_len, self.num_heads * 2 * self.head_dim)

        attn = self.out_proj(attn)
        return attn

class VisionDiff(nn.Module):
    def __init__(self, dim, num_heads=4, in_channels=None, out_channels=None, patch_size=2):
        super().__init__()
        self.dim = dim

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.patch_size = patch_size

        if in_channels:
            self.encode = nn.Conv2d(in_channels, dim, kernel_size=patch_size, stride=patch_size, bias=True)

        if out_channels:
            self.decode = nn.Linear(dim, patch_size * patch_size * out_channels, bias=True)

        self.attn = MultiheadDiffAttn(dim, num_heads=num_heads)
        self.mlp = Mlp(in_features=dim, hidden_features=dim * 4)

        self.norm1 = nn.LayerNorm(dim, elementwise_affine=False, eps=1e-6)
        self.norm2 = nn.LayerNorm(dim, elementwise_affine=False, eps=1e-6)

    def unpatchify(self, x):
        if self.out_channels:
            x = self.decode(x)
            c = self.out_channels
            p = self.patch_size
            h = w = int(x.shape[1] ** 0.5)
            assert h * w == x.shape[1]
            x = x.reshape(shape=(x.shape[0], h, w, p, p, c))
            x = torch.einsum('nhwpqc->nchpwq', x)
            imgs = x.reshape(shape=(x.shape[0], c, h * p, h * p))
            return imgs
        return x

    def patchify(self, x):
        if self.in_channels:
            x = self.encode(x)
            return x.flatten(2).transpose(1, 2)
        return x

    def forward(self, x):
        x = self.patchify(x)
        x = x + self.attn(self.norm1(x))
        x = x + self.mlp(self.norm2(x))
        x = self.unpatchify(x)
        return x

if __name__ == "__main__":
    dim, num_heads = 32, 4
    layer1 = VisionDiff(dim, num_heads, in_channels=3)
    layer2 = VisionDiff(dim, num_heads)
    layer3 = VisionDiff(dim, num_heads, out_channels=3)

    x = torch.zeros(1, 3, 64, 64) # Example "image"
    x = layer1(x)
    x = layer2(x)
    x = layer3(x)

    print(f"Output shape: {x.shape}") # [1, 3, 64, 64]