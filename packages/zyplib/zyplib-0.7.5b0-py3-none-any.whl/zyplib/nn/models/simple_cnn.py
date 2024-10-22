import torch
import torch.nn as nn

from zyplib.nn.modules import BaseModule


class VerySimpleCNN(BaseModule):
    def __init__(
        self,
        in_channels,
        hid_channels,
        fc_layers=(1,),
        kernel_size=3,
        num_layers=3,
        activation=nn.LeakyReLU,
    ):
        super(VerySimpleCNN, self).__init__()

        self.layers = nn.ModuleList()
        for i in range(num_layers):
            self.layers.append(
                nn.Conv1d(
                    in_channels if i == 0 else hid_channels,
                    hid_channels,
                    kernel_size,
                    padding=kernel_size // 2,
                )
            )
            self.layers.append(activation())

        in_features = hid_channels
        fc = nn.ModuleList()
        for i in fc_layers:
            fc.append(nn.Linear(in_features, i))
            fc.append(activation())
            in_features = i
        fc = fc[:-1]  # 去掉最后一个激活函数
        self.fc = nn.Sequential(*fc)

    def forward(self, x):
        # x shape: (N, C, T)
        for layer in self.layers:
            x = layer(x)
        # x shape: (N, out_channels, T)
        x = x.mean(dim=2)  # Global average pooling
        # x shape: (N, out_channels)
        x = self.fc(x)
        # x = torch.sigmoid(x)
        return x


class AttentionCNN(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        att_channels,
        n_len_seg,
        n_classes
    ):
        """一个简单的自注意力机制的卷积神经网络

        @source: https://github.com/hsd1503/resnet1d/blob/master/acnn1d.py

        Input/Output
        ----------
        - Input: (batch, channels, length)
        - Output: (batch)

        Parameters
        ----------
        - `in_channels` : `int`
            - number of input channels
        - `out_channels` : `int`
            - number of output channels
        - `att_channels` : `int`
            - number of attention channels
        - `n_len_seg` : `int`
            - number of segments
        - `n_classes` : `int`
            - number of classes
        """
        super(AttentionCNN, self).__init__()

        self.n_len_seg = n_len_seg
        self.n_classes = n_classes
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.att_channels = att_channels

        # (batch, channels, length)
        self.cnn = nn.Conv1d(
            in_channels=self.in_channels,
            out_channels=self.out_channels,
            kernel_size=16,
            stride=4,
        )

        self.W_att_channel = nn.Parameter(
            torch.randn(self.out_channels, self.att_channels)
        )
        self.v_att_channel = nn.Parameter(torch.randn(self.att_channels, 1))

        self.dense = nn.Linear(out_channels, n_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.n_channel, self.n_length = x.shape[-2], x.shape[-1]
        assert (
            self.n_length % self.n_len_seg == 0
        ), 'Input n_length should divided by n_len_seg'
        self.n_seg = self.n_length // self.n_len_seg

        out = x

        # (n_samples, n_channel, n_length) -> (n_samples, n_length, n_channel)
        out = out.permute(0, 2, 1)
        # (n_samples, n_length, n_channel) -> (n_samples*n_seg, n_len_seg, n_channel)
        out = out.view(-1, self.n_len_seg, self.n_channel)
        # (n_samples*n_seg, n_len_seg, n_channel) -> (n_samples*n_seg, n_channel, n_len_seg)
        out = out.permute(0, 2, 1)
        # cnn
        out = self.cnn(out)
        # global avg, (n_samples*n_seg, out_channels)
        out = out.mean(-1)
        # global avg, (n_samples, n_seg, out_channels)
        out = out.view(-1, self.n_seg, self.out_channels)
        # self attention
        e = torch.matmul(out, self.W_att_channel)
        e = torch.matmul(torch.tanh(e), self.v_att_channel)
        n1 = torch.exp(e)
        n2 = torch.sum(torch.exp(e), 1, keepdim=True)
        gama = torch.div(n1, n2)
        out = torch.sum(torch.mul(gama, out), 1)
        # dense
        out = self.dense(out)

        return out
