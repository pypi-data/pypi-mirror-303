# Designer:Ethan Pan
# Coder:God's hand
# Time:2024/4/7 17:18
import torch
from torch import nn

# 定义 Transformer 模型
class TransformerModel(nn.Module):
    def __init__(self, input_size, d_model, window_size, num_heads, num_layers, dropout_prob):
        super(TransformerModel, self).__init__()

        self.input_size = input_size
        self.d_model = d_model
        self.num_heads = num_heads
        self.num_layers = num_layers
        self.window_size = window_size

        # self.lstm = nn.LSTM(input_size, d_model, batch_first=True)
        # self.dropout = nn.Dropout(dropout_prob)

        # 定义 Transformer 编码器，并指定输入维数和头数
        # self.encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=self.num_heads)
        self.encoder = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model=d_model, nhead=self.num_heads),
                                             num_layers=self.num_layers)

        # 定义全连接层，输出特征
        self.linearOut = nn.Sequential(
            nn.Flatten(),
            nn.Linear(d_model * window_size, d_model))


    def forward(self, x):
        # 调整输入维度为 (batch_size, sequence_length, input_dim)
        x = x.permute(0, 2, 1)
        # x, _ = self.lstm(x)

        # 将输入数据流经 Transformer 编码器进行特征提取
        x = self.encoder(x)

        # 将输入数据流经全连接层，进行输出
        out = self.linearOut(x)

        return out