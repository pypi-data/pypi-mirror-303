from typing import Union

import numpy as np
import torch


def to_onehot(
    y: Union[np.ndarray, torch.Tensor, list[int]], squeeze_2_class: bool = True
) -> Union[np.ndarray, torch.Tensor]:
    """将标签编码为独热码

    Parameters
    ----------
    - `y` : `np.ndarray[int] | torch.Tensor[int] | list[int]`
        - 标签, 一个一维的整数数组或张量
    - `squeeze_2_class` : `bool`, optional
        - 如果为 True 且标签为二分类, 则返回一个 [N, 1] 维度的独热码

    Returns
    ----------
    - `np.ndarray` or `torch.Tensor`
        - 独热码

    Raises
    ----------
    - `TypeError`
        - 输入必须是 NumPy 数组或 PyTorch Tensor
    """
    if isinstance(y, np.ndarray):
        num_classes = len(np.unique(y))
        if num_classes == 1 or (num_classes == 2 and squeeze_2_class):
            return y.reshape(-1, 1)
        return np.eye(num_classes)[y]
    elif isinstance(y, torch.Tensor):
        num_classes = len(torch.unique(y))
        if num_classes == 1 or (num_classes == 2 and squeeze_2_class):
            return y.reshape(-1, 1)
        return torch.eye(num_classes, device=y.device)[y]
    elif isinstance(y, list):
        return to_onehot(np.array(y), squeeze_2_class)
    else:
        raise TypeError('Input must be a NumPy array or PyTorch Tensor')


def from_onehot(y: Union[np.ndarray, torch.Tensor]) -> Union[np.ndarray, torch.Tensor]:
    """将独热码转换回标签

    Parameters
    ----------
    - `y` : `np.ndarray` or `torch.Tensor`
        - 独热码, 一个一维或二维的浮点数数组或张量

    Returns
    ----------
    - `np.ndarray` or `torch.Tensor`
        - 标签, 一个一维的整数数组或张量

    Raises
    ----------
    - `TypeError`
        - 输入必须是 NumPy 数组或 PyTorch Tensor
    """
    if isinstance(y, np.ndarray):
        if y.ndim == 1:
            return y.astype(int)
        return np.argmax(y, axis=1)
    elif isinstance(y, torch.Tensor):
        if y.dim() == 1:
            return y.long()
        return torch.argmax(y, dim=1)
    else:
        raise TypeError('Input must be a NumPy array or PyTorch Tensor')
