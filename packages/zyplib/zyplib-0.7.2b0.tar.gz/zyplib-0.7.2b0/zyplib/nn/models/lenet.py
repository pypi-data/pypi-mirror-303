from typing import List, Optional

import torch.nn as nn

from zyplib.nn.modules import BaseModule, XDim, avgpool, conv


class LeNetPro(BaseModule):
    def __init__(
        self,
        in_ch: int,
        in_samples: int,
        n_class: int,
        xdim: XDim = 1,
        num_layers: int = 2,
        feature_maps: Optional[List[int]] = None,
        kernel_sizes: Optional[List[int]] = None,
        fc_sizes: Optional[List[int]] = None,
    ):
        """基于 LeNet 的改进版，支持任意维度的输入

        默认参数下等价于一个 1D 的 LeNet

        注意 num_layers, feature_maps, kernel_sizes 的长度必须一致

        Parameters
        ----------
        - `in_ch` : `int`
            - 输入通道数
        - `in_samples` : `int`
            - 输入样本数
        - `n_class` : `int`
            - 类别数
        - `num_layers` : `int`, optional
            - 特征提取层数，by default 2
        - `feature_maps` : `list`, optional
            - 特征提取层输出通道数，by default [6, 16]
        - `kernel_sizes` : `list`, optional
            - 特征提取层卷积核大小，by default [5, 5]
        - `fc_sizes` : `list`, optional
            - 全连接层大小，by default [120, 84]
        - `xdim` : `XDim`, optional
            - 卷积网络的维度，默认 1D
        """
        super().__init__()
        Conv = conv(xdim)
        AvgPool = avgpool(xdim)

        # 设置默认值
        if feature_maps is None:
            feature_maps = [6, 16]
        if kernel_sizes is None:
            kernel_sizes = [5, 5]
        if fc_sizes is None:
            fc_sizes = [120, 84]

        assert (
            num_layers == len(feature_maps) == len(kernel_sizes)
        ), 'num_layers, feature_maps, and kernel_sizes must have the same length'

        # 构建特征提取层
        layers = []
        in_channels = in_ch
        feature_size = in_samples
        for i in range(num_layers):
            layers.extend(
                [
                    Conv(in_channels, feature_maps[i], kernel_size=kernel_sizes[i]),
                    nn.ReLU(),
                    AvgPool(kernel_size=2),
                ]
            )
            in_channels = feature_maps[i]
            feature_size = (feature_size - kernel_sizes[i] + 1) // 2  # 更新特征图大小

        self.features = nn.Sequential(*layers)

        # 计算全连接层的输入维度
        self.fc_input_dim = feature_maps[-1] * (feature_size ** xdim)

        # 构建分类器
        classifier_layers = []
        fc_input = self.fc_input_dim
        for fc_size in fc_sizes:
            classifier_layers.extend([nn.Linear(fc_input, fc_size), nn.ReLU()])
            fc_input = fc_size
        classifier_layers.append(nn.Linear(fc_input, n_class))

        self.classifier = nn.Sequential(*classifier_layers)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x
