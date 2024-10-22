from typing import Literal, Union

import numpy as np
from scipy import fft, signal

from zyplib.utils.ensure import ensure_npy

# FilterType = Literal['butter', 'cheby1', 'cheby2', 'ellip', 'bessel']
__all__ = ['notch', 'bandpass_butter']


def notch(X, fs, f0=50, Q=30, axis=-1):
    r"""Notch filter.

    Parameters
    ----------
    - signals : array_like
        - Input signal.
    - fs : float
        - Sampling frequency.
    - f0 : float
        - Notch frequency.
    - Q : float, optional
        - Q factor. Default is 30.
        - https://en.wikipedia.org/wiki/Q_factor
        - $Q = \frac{f_0}{\Delta f}$
    - axis : int, optional
        - Axis along which to apply the filter. Default is -1.

    Returns
    ----------
    - y : ndarray
        - Filtered signal.
    """
    X = ensure_npy(X)
    b, a = signal.iirnotch(f0, Q, fs)
    return signal.lfilter(b, a, X, axis=axis)


def bandpass_butter(
    X, fs: float, lfreq: float, rfreq: float, order=3, prevent_nan=True, axis=-1
):
    r"""Bandpass filter.

    Parameters
    ----------
    - signals : array_like
        - Input signal.
    - fs : float
        - Sampling frequency.
    - lfreq : float
        - Left frequency.
    - rfreq : float
        - Right frequency.
    - order : int, optional
        - Filter order. Default is 3.
        - 注意, 太高的阶数（例如 5）可能会导致滤波器不稳定，使得结果出现 NaN 值
    - prevent_nan : bool, optional
        - 如果为 True，则尝试降低滤波器阶数以防止 NaN 值。
    - axis : int, optional

    Returns
    ----------
    - y : ndarray
        - Filtered signal.
    """
    X = ensure_npy(X)
    nyq = 0.5 * fs
    low = lfreq / nyq
    high = rfreq / nyq

    # 检查频率范围是否有效
    if low >= high or high >= 1:
        raise ValueError('Invalid frequency range. Ensure lfreq < rfreq < fs/2')

    b, a = signal.butter(order, [low, high], btype='bandpass')
    y = signal.lfilter(b, a, X, axis=axis)

    # 检查输出是否包含 NaN 值
    if np.isnan(y).any():
        print('Warning: NaN values detected in the output. Trying with a lower order.')

        if prevent_nan:
            return bandpass_butter(X, fs, lfreq, rfreq, order=max(1, order - 1), axis=axis)
        else:
            raise ValueError('NaN values detected in the output.')

    return y
