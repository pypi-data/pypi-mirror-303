import numpy as np
from scipy import signal, stats


def peak_num(x, axis=-1):
    return len(signal.find_peaks(x, axis=axis)[0])


def cross_zero_num(x, axis=-1):
    return len(np.where(np.diff(np.sign(x), axis=axis))[0])


def abs_max(x, axis=-1):
    return np.max(np.abs(x), axis=axis)


def mean(x, axis=-1):
    return np.mean(x, axis=axis)


def std(x, axis=-1):
    return np.std(x, axis=axis)


def skew(x, axis=-1):
    return stats.skew(x, axis=axis)


def kurtosis(x, axis=-1):
    return stats.kurtosis(x, axis=axis)


def power(x, axis=-1):
    return np.sum(np.square(x), axis=axis)


def diff_mean(x, axis=-1):
    return np.mean(np.diff(x, axis=axis), axis=axis)


def diff_std(x, axis=-1):
    return np.std(np.diff(x, axis=axis), axis=axis)
