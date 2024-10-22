from torch import nn
from torch.nn import functional as F


def build_norm(type=None, channels=None):
    assert type is None or type in ['batch', 'instance', 'pixel']
    if type is None:
        return nn.Identity()
    elif type == 'batch':
        return nn.BatchNorm1d(channels)
    elif type == 'instance':
        return nn.InstanceNorm1d(channels)
    elif type == 'pixel':
        return PixelNorm()


class PixelNorm(nn.Module):
    """Pixel Normalization from

    'PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION

    沿着通道维度对 Pixel 向量做标准化。如输入为 `[N, 50, 1024]`
    则该方法对 N 个样本中，所有 1024 个点在 50 个通道上组成的 50-dim 向量做归一化
    """

    def __init__(self):
        super(PixelNorm, self).__init__()

    def forward(self, x, epsilon=1e-8):
        # 沿着 Channel 维，对每个 pixel 做一次 norm
        assert len(x.shape) == 3
        return x * (((x**2).mean(dim=1, keepdim=True) + epsilon).rsqrt())


class ConditionalBatchNorm1d(nn.BatchNorm1d):
    """Conditional Batch Normalization"""

    def __init__(
        self,
        num_features,
        eps=1e-05,
        momentum=0.1,
        affine=False,
        track_running_stats=True,
    ):
        super(ConditionalBatchNorm1d, self).__init__(
            num_features, eps, momentum, affine, track_running_stats
        )

    def forward(self, input, weight, bias, **kwargs):
        self._check_input_dim(input)

        exponential_average_factor = 0.0

        if self.training and self.track_running_stats:
            self.num_batches_tracked += 1
            if self.momentum is None:  # use cumulative moving average
                exponential_average_factor = 1.0 / self.num_batches_tracked.item()
            else:  # use exponential moving average
                exponential_average_factor = self.momentum

        output = F.batch_norm(
            input,
            self.running_mean,
            self.running_var,
            self.weight,
            self.bias,
            self.training or not self.track_running_stats,
            exponential_average_factor,
            self.eps,
        )
        if weight.dim() == 1:
            weight = weight.unsqueeze(0)
        if bias.dim() == 1:
            bias = bias.unsqueeze(0)
        size = output.size()
        weight = weight.unsqueeze(-1).expand(size)
        bias = bias.unsqueeze(-1).expand(size)
        return weight * output + bias


class CategoricalConditionalBatchNorm1d(ConditionalBatchNorm1d):
    def __init__(
        self,
        num_classes,
        num_features,
        eps=1e-5,
        momentum=0.1,
        affine=False,
        track_running_stats=True,
    ):
        super(CategoricalConditionalBatchNorm1d, self).__init__(
            num_features, eps, momentum, affine, track_running_stats
        )
        self.weights = nn.Embedding(num_classes, num_features)
        self.biases = nn.Embedding(num_classes, num_features)

        self._initialize()

    def _initialize(self):
        nn.init.ones_(self.weights.weight.data)
        nn.init.zeros_(self.biases.weight.data)

    def forward(self, input, c, **kwargs):
        weight = self.weights(c)
        bias = self.biases(c)
        return super(CategoricalConditionalBatchNorm1d, self).forward(input, weight, bias)
