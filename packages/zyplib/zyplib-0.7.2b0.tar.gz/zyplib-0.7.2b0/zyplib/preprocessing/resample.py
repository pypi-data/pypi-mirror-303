import numpy as np
from scipy.signal import resample_poly


def resample_eeg(X: np.ndarray, fs: int, target_fs: int, axis: int = -1):
    """对 EEG 数据进行重采样; 将一个采样率为 `fs` 的 EEG 数据重采样为 `target_fs`

    考虑到 EEG 数据的非周期性, 使用 scipy.signal.resample_poly 进行重采样
    """
    return resample_poly(X, target_fs, fs, axis=axis)
