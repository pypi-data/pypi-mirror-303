# Designer:Yudong Pan
# Coder:God's hand
# Time:2024/4/25 15:29
import torch
from torch import nn


class CNNModel(nn.Module):

    def calculateOutSize(self, model, nChan, nTime):
        '''
            Calculate the output based on input size
            model is from nn.Module and inputSize is a array
        '''
        data = torch.randn(1, 1, nChan, nTime)
        out = model(data).shape
        return out[1:]


    def __init__(self, dropout_prob, input_size, window_size, kernel_length=3):
        super(CNNModel, self).__init__()
        self.dropout_prob = dropout_prob
        self.input_size = input_size
        self.window_size = window_size
        self.kernel_length = kernel_length

        # 带通滤波卷积
        self.conv_bandpass = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=self.input_size * 2, kernel_size=(1, window_size), padding="same"),
            nn.ReLU(),
            nn.BatchNorm2d(self.input_size * 2),
            nn.Dropout(dropout_prob),
        )

        # 空间卷积
        self.conv_spatial = nn.Sequential(
            nn.Conv2d(in_channels=self.input_size * 2, out_channels=self.input_size * 4,
                      kernel_size=(self.input_size, 1), stride=(self.input_size, 1)),
            nn.ReLU(),
            nn.BatchNorm2d(self.input_size * 4),
            nn.Dropout(dropout_prob),
        )

        # 时间卷积
        self.conv_temporal = nn.Sequential(
            nn.Conv2d(in_channels=self.input_size * 4, out_channels=self.input_size * 2, kernel_size=(1, kernel_length),
                      stride=(kernel_length, 2), ),
            nn.ReLU(),
            nn.BatchNorm2d(self.input_size * 2),
            nn.Dropout(dropout_prob),
        )

        self.conv_blocks = nn.Sequential(
            self.conv_bandpass,
            self.conv_spatial,
            self.conv_temporal
        )

        # 全连接层
        self.fcSize = self.calculateOutSize(self.conv_blocks, self.input_size, self.window_size)
        self.fcUnit = self.fcSize[0] * self.fcSize[1] * self.fcSize[2]
        self.D1 = 100
        self.D2 = 50
        self.D3 = self.input_size

        self.linearOut = nn.Sequential(
            nn.Linear(self.fcUnit, self.D1),
            nn.ReLU(),
            nn.Linear(self.D1, self.D2),
            nn.ReLU(),
            nn.Dropout(self.dropout_prob),
            nn.Linear(self.D2, self.D3)
        )

    def forward(self, x):
        # 输入维度为 (batch_size, input_dim, sequence_length)
        x = x.unsqueeze(1)  # (b, 1, c, T)

        x = self.conv_blocks(x)

        x = x.reshape(-1, self.fcUnit)

        out = self.linearOut(x)

        # 输出维度为 (batch_size, input_dim)
        return out
