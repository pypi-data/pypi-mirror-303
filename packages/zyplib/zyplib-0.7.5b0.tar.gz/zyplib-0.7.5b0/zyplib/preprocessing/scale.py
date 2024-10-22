from typing import Literal

import numpy as np

from zyplib.utils.ensure import ensure_3dims


def z_score(X: np.ndarray, axis: int = -1) -> np.ndarray:
    mean = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)
    return (X - mean) / std


def minmax(
    X: np.ndarray, range_to: tuple[float, float] = (0, 1), axis: int = -1
) -> np.ndarray:
    min = np.min(X, axis=axis, keepdims=True)
    max = np.max(X, axis=axis, keepdims=True)
    return (X - min) / (max - min) * (range_to[1] - range_to[0]) + range_to[0]


def robust_scale(
    X: np.ndarray, percentiles: tuple[float, float] = (25, 75), axis: int = -1
) -> np.ndarray:
    median = np.median(X, axis=axis, keepdims=True)
    lower = np.percentile(X, percentiles[0], axis=axis, keepdims=True)
    upper = np.percentile(X, percentiles[1], axis=axis, keepdims=True)
    return (X - median) / (upper - lower)


def scale_eeg(
    signals: np.ndarray,
    method: Literal['minmax', 'robust', 'zscore'] = 'zscore',
    across: Literal['channel', 'epoch', 'total'] = 'channel',
    *,
    minmax_range: tuple[float, float] = (0, 1),
    robust_percentiles: tuple[float, float] = (25, 75),
) -> np.ndarray:
    """对 EEG 信号进行缩放（归一化）

    输入的 EEG 信号数据可能为 [C, T] 或 [N, C, T] 格式；

    指定缩放范围有三种，以下假设使用 [N, C, T] 格式和 minmax(0, 1) 缩放为例

    - `across='channel'`: 每个通道的信号直接的缩放互相独立; 即计算每个通道的 min 和 max，然后各自缩放到 [0, 1] 范围内
    - `across='epoch'`: 在完整的 [C, T] 的 Epoch 上进行缩放; 即计算 N 个 Epoch[C, T] 的 min 和 max，然后缩放到 [0, 1] 范围内
    - `across='total'`: 在完整的 [N, C, T] 的 Epoch 上进行缩放; 即计算整个 [N, C, T] 的 min 和 max，然后缩放到 [0, 1] 范围内

    Parameters
    ----------
    - `signals` : `np.ndarray`
        - 输入的 EEG 信号数据，形状为 (C, T) 或 (N, C, T)
    - `method` : `Literal['minmax', 'robust', 'zscore']`, 缩放方法
        - 'minmax' 将数据缩放到 [min, max] 范围内
        - 'zscore' 使用 z-score 标准化
        - 'robust' 使用中位数和四分位数进行缩放
    - `across` : `Literal['channel', 'epoch']`, 指定**缩放范围**
        - 'channel': 每个通道的信号直接的缩放互相独立
        - 'epoch': 在完整的 [C, T] 的 Epoch 上进行缩放
        - 'total': 在完整的 [N, C, T] 的 Epoch 上进行缩放
    - `minmax_range` : `tuple[float, float]`, optional, 仅在 `method='minmax'` 时有效
        - 缩放后的最小值和最大值，默认为 (0, 1)
    - `robust_percentiles` : `tuple[float, float]`, optional, 仅在 `method='robust'` 时有效
        - 缩放后的中位数和四分位数，默认为 (25, 75)

    """
    sig_shape = signals.shape
    signals = ensure_3dims(signals, newaxis='batch')

    N, C, T = signals.shape
    if method == 'zscore':
        scaler = z_score
    elif method == 'minmax':

        def fn_minmax(x, axis):
            return minmax(x, range_to=minmax_range, axis=axis)

        scaler = fn_minmax
    elif method == 'robust':

        def fn_robust(x, axis):
            return robust_scale(x, percentiles=robust_percentiles, axis=axis)

        scaler = fn_robust
    else:
        raise ValueError(f'Invalid method: {method}')

    if across == 'channel':
        # 对每个通道单独进行缩放
        scaled = scaler(signals, axis=-1)
    elif across == 'epoch':
        # 对每个 epoch 单独进行缩放
        # scaled = np.array([scaler(signals[i], axis=(0, 1)) for i in range(N)])
        scaled = scaler(signals, axis=(1, 2))
    elif across == 'total':
        # 对整个数据集进行缩放
        scaled = scaler(signals, axis=None)
    else:
        raise ValueError(f'Invalid across: {across}')

    return scaled.reshape(sig_shape)
