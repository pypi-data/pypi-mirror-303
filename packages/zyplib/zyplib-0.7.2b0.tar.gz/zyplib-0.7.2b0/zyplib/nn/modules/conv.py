import torch
from torch import nn

from zyplib.nn import base


class DepthwiseSeperableConv(nn.Module):
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        dilation=1,
        bias=False,
        Conv=nn.Conv1d,
    ):
        super(DepthwiseSeperableConv, self).__init__()
        self.depthwise_conv = Conv(
            in_channels,
            in_channels,
            kernel_size,
            stride,
            padding,
            dilation,
            in_channels,
            bias,
        )
        self.pointwise_conv = Conv(in_channels, out_channels, 1, 1, 0, 1, 1, bias)

    def forward(self, x):
        x = self.depthwise_conv(x)
        x = self.pointwise_conv(x)
        return x


class MaxNormConv(nn.Module):
    def __init__(self, conv: base.Conv, max_norm: int = 1):
        super(MaxNormConv, self).__init__()
        self.conv = conv
        self.max_norm = max_norm

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.conv.weight.data = torch.renorm(
            self.conv.weight.data, p=2, dim=0, maxnorm=self.max_norm
        )
        return self.conv.forward(x)
