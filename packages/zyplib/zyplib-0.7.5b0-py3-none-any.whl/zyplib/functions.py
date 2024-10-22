import numpy as np

__all__ = ['sigmoid']


def sigmoid(x):
    x = np.clip(x, -200, 200)  # 防止溢出
    return 1 / (1 + np.exp(-x))
