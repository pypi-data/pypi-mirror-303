import torch
import torch.nn as nn
import math


class RelativePositionMultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1, max_len=5000):
        super(RelativePositionMultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

        self.W_o = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)

        # 相対位置エンコーディングのパラメータ
        self.Er = nn.Parameter(torch.Tensor(max_len, self.d_k))
        nn.init.xavier_uniform_(self.Er)

    def forward(self, x, attn_mask=None, key_padding_mask=None):
        batch_size, seq_len, _ = x.size()
        if seq_len > self.Er.size(0):
            raise ValueError(f"Sequence length {seq_len} exceeds maximum relative positions {self.Er.size(0)}")

        Q = self.W_q(x)
        K = self.W_k(x)
        V = self.W_v(x)

        Q = Q.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)  # (B, H, L, Dk)
        K = K.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)

        # 相対位置エンコーディングの取得
        Er = self.Er[:seq_len, :]  # (L, Dk)

        # アテンションスコアの計算
        AC = torch.matmul(Q, K.transpose(-2, -1))  # (B, H, L, L)

        # 相対位置のインデックスを計算
        rel_pos = torch.arange(seq_len - 1, -seq_len, -1, device=x.device)
        rel_pos = rel_pos + (self.Er.size(0) - 1)  # シフトして正のインデックスに
        Er_embed = self.Er.index_select(0, rel_pos)  # (2L -1, Dk)

        BD = torch.matmul(Q, Er_embed.transpose(0, 1))  # (B, H, L, 2L -1)
        BD = self._relative_shift(BD)

        # スコアの合計
        scores = (AC + BD) / math.sqrt(self.d_k)

        # マスクの適用
        if attn_mask is not None:
            attn_mask = attn_mask.unsqueeze(0).unsqueeze(0)  # (1, 1, L, L)
            scores = scores.masked_fill(attn_mask == 0, float('-inf'))

        if key_padding_mask is not None:
            key_padding_mask = key_padding_mask.unsqueeze(1).unsqueeze(2)  # (B, 1, 1, L)
            scores = scores.masked_fill(key_padding_mask == 0, float('-inf'))

        attn = torch.softmax(scores, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, V)  # (B, H, L, Dk)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        out = self.W_o(out)

        return out


class CustomTransformerEncoderLayer(nn.Module):
    def __init__(self, d_model, n_head, dim_feedforward , dropout, max_len):
        super(CustomTransformerEncoderLayer, self).__init__()
        self.self_attn = RelativePositionMultiHeadAttention(d_model, n_head, dropout=dropout, max_len=max_len)
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

        self.activation = nn.ReLU()

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        src2 = self.self_attn(src, attn_mask=src_mask, key_padding_mask=src_key_padding_mask)
        src = src + self.dropout1(src2)
        src = self.norm1(src)

        src2 = self.linear2(self.dropout(self.activation(self.linear1(src))))
        src = src + self.dropout2(src2)
        src = self.norm2(src)
        return src