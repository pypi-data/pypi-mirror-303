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
