import numpy as np
from scipy import signal

from zyplib.utils.ensure import ensure_npy

__all__ = [
    'welch',
    'bandpower',
    'eeg_delta_power',
    'eeg_theta_power',
    'eeg_alpha_power',
    'eeg_sigma_power',
    'eeg_beta_power',
]


def welch(x, fs, nperseg=None, max_freq=None, axis=-1):
    """Welch PSD
    计算 welch 功率谱, 最后截断结果, 返回低于 lowpass Hz 的部分

    Parameters
    ----------
    - x : array_like
    - fs : int, 采样率
    - nperseg : int, 每段的长度, 默认 2 * fs, 也就意味着频率分辨率 0.5 Hz
    - max_freq : int, 截断频率
        - 当非 None 的时候, 截断超过 max_freq 的部分
    - axis : int, 默认 -1,即最后一个维度

    Returns
    ----------
    - f : ndarray, 频率
        - 分辨率为 fs / nperseg
        - 长度为 nperseg / 2
    - Pxx : ndarray, 功率谱
    """
    x = ensure_npy(x)
    if not nperseg:
        nperseg = fs * 2
    nfft = np.power(2, np.ceil(np.log2(nperseg)))
    f, Pxx = signal.welch(x, fs, nperseg=nperseg, nfft=nfft, axis=axis)
    # 当需要截断且截断频率小于 fs / 2 时, 进行截断
    if max_freq is not None and max_freq < fs / 2:
        ind = np.argmax(f > max_freq)
        if ind == 0:
            raise ValueError('lowpass is too low')
        f = f[:ind]
        Pxx = Pxx[..., :ind]
    return f, Pxx


def bandpower(x, fs, band: tuple, axis=-1, nperseg=None):
    x = ensure_npy(x)
    f, Pxx = welch(x, fs, axis=axis, nperseg=nperseg)
    ind_min = np.argmax(f > band[0])
    ind_max = np.argmax(f > band[1])
    if ind_min == 0 or ind_max == 0:
        raise ValueError('band values are too low')
    return np.trapz(Pxx[..., ind_min:ind_max], f[ind_min:ind_max], axis=axis)


def eeg_delta_power(x, fs, axis=-1, nperseg=None):
    """Delte 0.5 and 4 Hz.

    Parameters
    ----------
    - `x` : array_like, 1-D or 2-D
        - 待处理的原始 EEG 信号, 可以是一维或二维数组, 类型为 `array_like`。
    - `fs` : float
        - 输入信号的采样频率, 单位为 Hz, 类型为 `float`。
    - `axis` : int, optional
        - 可选参数, 计算取样信号频谱的轴。默认值为 -1, 即最后一个轴, 类型为 `int`。

    Returns
    ----------
    - `band_power` : float
    """

    return bandpower(x, fs, (0.5, 4), axis=axis, nperseg=nperseg)


def eeg_theta_power(x, fs, axis=-1, nperseg=None):
    """Theta 4 and 8 Hz.

    Parameters
    ----------
    - `x` : array_like, 1-D or 2-D
        - 待处理的原始 EEG 信号, 可以是一维或二维数组, 类型为 `array_like`。
    - `fs` : float
        - 输入信号的采样频率, 单位为 Hz, 类型为 `float`。
    - `axis` : int, optional
        - 可选参数, 计算取样信号频谱的轴。默认值为 -1, 即最后一个轴, 类型为 `int`。

    Returns
    ----------
    - `band_power` : float
    """
    return bandpower(x, fs, (4, 8), axis=axis, nperseg=nperseg)


def eeg_alpha_power(x, fs, axis=-1, nperseg=None):
    """Alpha 8 and 12 Hz.

    Parameters
    ----------
    - `x` : array_like, 1-D or 2-D
        - 待处理的原始 EEG 信号, 可以是一维或二维数组, 类型为 `array_like`。
    - `fs` : float
        - 输入信号的采样频率, 单位为 Hz, 类型为 `float`。
    - `axis` : int, optional
        - 可选参数, 计算取样信号频谱的轴。默认值为 -1, 即最后一个轴, 类型为 `int`。

    Returns
    ----------
    - `band_power` : float
    """
    return bandpower(x, fs, (8, 12), axis=axis, nperseg=nperseg)


def eeg_sigma_power(x, fs, axis=-1, nperseg=None):
    """Sigma 12 and 15 Hz.

    Parameters
    ----------
    - `x` : array_like, 1-D or 2-D
        - 待处理的原始 EEG 信号, 可以是一维或二维数组, 类型为 `array_like`。
    - `fs` : float
        - 输入信号的采样频率, 单位为 Hz, 类型为 `float`。
    - `axis` : int, optional
        - 可选参数, 计算取样信号频谱的轴。默认值为 -1, 即最后一个轴, 类型为 `int`。

    Returns
    ----------
    - `band_power` : float
    """
    return bandpower(x, fs, (12, 15), axis=axis, nperseg=nperseg)


def eeg_beta_power(x, fs, axis=-1, nperseg=None):
    """Beta 12 and 30 Hz.

    Parameters
    ----------
    - `x` : array_like, 1-D or 2-D
        - 待处理的原始 EEG 信号, 可以是一维或二维数组, 类型为 `array_like`。
    - `fs` : float
        - 输入信号的采样频率, 单位为 Hz, 类型为 `float`。
    - `axis` : int, optional
        - 可选参数, 计算取样信号频谱的轴。默认值为 -1, 即最后一个轴, 类型为 `int`。

    Returns
    ----------
    - `band_power` : float
    """
    return bandpower(x, fs, (12, 30), axis=axis, nperseg=nperseg)
