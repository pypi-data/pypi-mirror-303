from torch import nn
from torch.nn.utils import weight_norm

from zyplib.nn import BaseModule


class CausalConv1d(nn.Conv1d):
    """1D DILATED CAUSAL CONVOLUTION."""

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        dilation=1,
        bias=True,
        padding_mode='zeros',
    ):
        super(CausalConv1d, self).__init__(
            in_channels,
            out_channels,
            kernel_size,
            stride=stride,
            padding=(kernel_size - 1) * dilation,
            dilation=dilation,
            bias=bias,
            padding_mode=padding_mode,
        )
        self.pad_size = (kernel_size - 1) * dilation

    def forward(self, x):
        y = super(CausalConv1d, self).forward(x)
        if self.pad_size != 0:
            y = y[:, :, : -self.pad_size].contiguous()
        return y


class TemporalBlock(nn.Module):
    def __init__(
        self,
        in_cn,
        out_cn,
        kernel_size,
        stride,
        dilation,
        dropout=0.2,
        padding_mode='zeros',
        activation=nn.ReLU,
    ):
        super(TemporalBlock, self).__init__()
        self.conv1 = weight_norm(
            CausalConv1d(
                in_cn,
                out_cn,
                kernel_size,
                stride=stride,
                dilation=dilation,
                padding_mode=padding_mode,
            )
        )
        self.relu1 = activation()
        self.dropout1 = nn.Dropout(dropout)

        self.conv2 = weight_norm(
            CausalConv1d(
                in_cn, out_cn, kernel_size, dilation=dilation, padding_mode=padding_mode
            )
        )
        self.relu2 = activation()
        self.dropout2 = nn.Dropout(dropout)

        self.net = nn.Sequential(
            self.conv1, self.relu1, self.dropout1, self.conv2, self.relu2, self.dropout2
        )
        self.downsample = nn.Conv1d(in_cn, out_cn, 1) if in_cn != out_cn else None
        self.relu = activation()

    def forward(self, x):
        out = self.net(x)
        res = x if self.downsample is None else self.downsample(x)
        return self.relu(out + res)


class TemporalConvNet(BaseModule):
    def __init__(
        self,
        in_ch: int,
        level_ch: list,
        num_stack=1,
        kernel_size=2,
        dropout=0.2,
        padding_mode='zeros',
    ):
        super(TemporalConvNet, self).__init__()
        layers = []
        num_levels = len(level_ch)
        dilations = [2**i for i in range(num_levels)] * num_stack
        level_ch *= num_stack
        self.reciptive_field_size = sum(dilations) * (kernel_size - 1) + 1

        for dilation_size, out_ch in zip(dilations, level_ch):
            layers += [
                TemporalBlock(
                    in_ch,
                    out_ch,
                    kernel_size,
                    stride=1,
                    dilation=dilation_size,
                    dropout=dropout,
                    padding_mode=padding_mode,
                )
            ]
            in_ch = out_ch

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)
