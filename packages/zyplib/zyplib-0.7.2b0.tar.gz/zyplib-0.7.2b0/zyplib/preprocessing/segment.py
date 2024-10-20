import numpy as np

from zyplib.utils.ensure import ensure_npy


def segment_signal(
    signal: np.ndarray,
    fs: int,
    seg_duration: float,
    overlap: float = 0,
    begin: float = 0,
    end: float = None,
):
    """Segment a signal into pieces.

    在 signal最后一个维度(时间维度)上分割,
    如果最后一个段的长度小于 `seg_duration`, 则丢弃最后一个段。

    Parameters
    ----------
    - `signal` : array_like, 1-D or 2-D
        - 待分段的信号。可以是1-D或2-D数组, 类型为 `array_like`。
        - 最后一个维度为时间维度
    - `fs` : int
        - 输入信号的采样频率, 单位为Hz, 类型为 `int`。
    - `seg_duration` : float
        - 每个段的持续时间, 单位为秒, 类型为 `float`。
    - `overlap` : float, 可选
        - 相邻段之间的重叠时间, 单位为秒, 类型为 `float`。
        - 默认值为0.0, 表示无重叠
    - `begin` : float, 可选
        - 信号的起始时间, 单位为秒, 类型为 `float`。
        - 默认值为0.0
    - `end` : float, 可选
        - 信号的结束时间, 单位为秒, 类型为 `float`。
        - 默认值为None, 表示使用信号的最后一个时间点作为结束时间

    Returns
    ----------
    - `segments` : ndarray
        - The segmented signal, `[N, ..., L]`.
    """
    if seg_duration <= 0:
        raise ValueError('seg_duration must be positive.')
    if overlap < 0:
        raise ValueError('overlap must be non-negative.')
    if overlap >= seg_duration:
        raise ValueError('overlap must be less than seg_duration.')

    seg_len = int(seg_duration * fs)
    overlap_len = int(overlap * fs)
    step = seg_len - overlap_len
    if step <= 0:
        raise ValueError('overlap must be less than seg_duration.')

    if end is None:
        end = signal.shape[-1] / fs
    if end <= begin:
        raise ValueError('end must be greater than begin.')

    signal = signal[..., int(begin * fs) : int(end * fs)]

    # 计算分段后的信号长度
    length = signal.shape[-1]
    n_seg = (length - overlap_len) // step
    if n_seg <= 0:
        raise ValueError('signal is too short.')

    signal = ensure_npy(signal)

    # 分段
    segments = np.lib.stride_tricks.as_strided(
        signal,
        shape=(n_seg, *signal.shape[:-1], seg_len),
        strides=(step * signal.strides[-1], *signal.strides),
        writeable=False,
    )
    # 从 view 中拷贝数据, 避免修改原始数据
    segments = segments.copy()
    return segments
