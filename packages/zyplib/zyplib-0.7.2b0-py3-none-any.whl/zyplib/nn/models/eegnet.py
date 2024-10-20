import torch
import torch.nn as nn

from zyplib.nn import base
from zyplib.nn.modules.conv import MaxNormConv

# class Conv2dWithConstraint(nn.Conv2d):
#     def __init__(self, *args, max_norm: int = 1, **kwargs):
#         self.max_norm = max_norm
#         super(Conv2dWithConstraint, self).__init__(*args, **kwargs)

#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         self.weight.data = torch.renorm(
#             self.weight.data, p=2, dim=0, maxnorm=self.max_norm
#         )
#         return super(Conv2dWithConstraint, self).forward(x)


class EEGNet(base.BaseModule):
    def __init__(
        self,
        samples: int = 128,
        channels: int = 60,
        F1: int = 8,
        F2: int = 16,
        D: int = 2,
        n_class: int = 1,
        kernel_1: int = 64,
        kernel_2: int = 16,
        dropout: float = 0.25,
    ):
        """EEGNet v4 版模型; 来源自 torcheeg 的实现

        - Paper: Lawhern V J, Solon A J, Waytowich N R, et al. EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces[J]. Journal of neural engineering, 2018, 15(5): 056013.
        - URL: https://arxiv.org/abs/1611.08024
        - Related Project: https://github.com/braindecode/braindecode/tree/master/braindecode


        Parameters
        ----------
        - `samples` : `int`, optional
            - 每个样本的采样点数，默认 128
        - `channels` : `int`, optional
            - 每个样本的通道数，默认 60
        - `F1` : `int`, optional
            - 第一个卷积层的卷积核数，默认 8
        - `F2` : `int`, optional
            - 第二个卷积层的卷积核数，默认 16
        - `D` : `int`, optional
            - 深度乘数，默认 2
        - `n_class` : `int`, optional
            - 分类数，默认 1
        - `kernel_1` : `int`, optional
            - 第一个卷积层的卷积核数，默认 64
        - `kernel_2` : `int`, optional
            - 第二个卷积层的卷积核数，默认 16
        - `dropout` : `float`, optional
            - 丢弃概率，默认 0.25
        """

        super(EEGNet, self).__init__()
        self.F1 = F1
        self.F2 = F2
        self.D = D
        self.n_samples = samples
        self.num_classes = n_class
        self.num_electrodes = channels
        self.kernel_1 = kernel_1
        self.kernel_2 = kernel_2
        self.dropout = dropout

        self.block1 = nn.Sequential(
            nn.Conv2d(
                1,
                self.F1,
                (1, self.kernel_1),
                stride=1,
                padding=(0, self.kernel_1 // 2),
                bias=False,
            ),
            nn.BatchNorm2d(self.F1, momentum=0.01, affine=True, eps=1e-3),
            MaxNormConv(
                nn.Conv2d(
                    self.F1,
                    self.F1 * self.D,
                    (self.num_electrodes, 1),
                    stride=1,
                    padding=(0, 0),
                    groups=self.F1,
                    bias=False,
                ),
                max_norm=1,
            ),
            nn.BatchNorm2d(self.F1 * self.D, momentum=0.01, affine=True, eps=1e-3),
            nn.ELU(),
            nn.AvgPool2d((1, 4), stride=4),
            nn.Dropout(p=dropout),
        )

        self.block2 = nn.Sequential(
            nn.Conv2d(
                self.F1 * self.D,
                self.F1 * self.D,
                (1, self.kernel_2),
                stride=1,
                padding=(0, self.kernel_2 // 2),
                bias=False,
                groups=self.F1 * self.D,
            ),
            nn.Conv2d(
                self.F1 * self.D,
                self.F2,
                1,
                padding=(0, 0),
                groups=1,
                bias=False,
                stride=1,
            ),
            nn.BatchNorm2d(self.F2, momentum=0.01, affine=True, eps=1e-3),
            nn.ELU(),
            nn.AvgPool2d((1, 8), stride=8),
            nn.Dropout(p=dropout),
        )

        self.lin = nn.Linear(self.feature_dim(), n_class, bias=False)

    def feature_dim(self):
        with torch.no_grad():
            mock_eeg = torch.zeros(1, 1, self.num_electrodes, self.n_samples)

            mock_eeg = self.block1(mock_eeg)
            mock_eeg = self.block2(mock_eeg)

        return self.F2 * mock_eeg.shape[3]

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Input (trials, 1, channels, samples)."""
        if x.ndim == 3:
            x = x.unsqueeze(1)
        x = self.block1(x)
        x = self.block2(x)
        x = x.flatten(start_dim=1)
        x = self.lin(x)

        return x
