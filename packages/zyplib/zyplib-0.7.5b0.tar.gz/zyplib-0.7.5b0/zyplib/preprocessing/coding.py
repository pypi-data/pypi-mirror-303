import numpy as np


def percentile_digitalize(x, axis=None):
    q1 = np.quantile(x, 0.25, axis=axis)
    q2 = np.quantile(x, 0.5, axis=axis)
    q3 = np.quantile(x, 0.75, axis=axis)
    x_digit = np.where(x < q1, 0, np.where(x < q2, 1, np.where(x < q3, 2, 3)))
    return x_digit


def features_to_onehot(features, axis=0):
    features_digit = percentile_digitalize(features, axis=axis)
    features_onehot = np.eye(4)[features_digit]
    return features_onehot


def continuous_smoothing(one_hot, alpha=0.2, decay=0.25):
    classes = one_hot.shape[-1]
    max_idx = np.argmax(one_hot, axis=-1)[..., np.newaxis]
    max_idx = np.repeat(max_idx, classes, axis=-1)
    one_hot_idx = one_hot.copy()
    one_hot_idx[..., :] = np.arange(classes)
    delta = np.abs(one_hot_idx - max_idx)
    scale = np.power(decay, delta).sum(axis=-1, keepdims=True) - 1
    running_alpha = alpha / scale
    label = np.zeros((one_hot.shape), dtype=np.int32)
    label = one_hot * (1 - alpha) + (1 - one_hot) * running_alpha * np.power(decay, delta)
    return label
