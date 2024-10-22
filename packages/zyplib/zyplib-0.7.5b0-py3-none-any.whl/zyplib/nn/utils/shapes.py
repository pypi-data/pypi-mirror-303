from typing import List, Tuple

import torch
from torch import nn


def output_shape(model: nn.Module, input_shape: Tuple[int, ...]) -> Tuple[int]:
    """计算模型输出形状

    Parameters
    ----------
    - `model` : `nn.Module`
        - 模型
    - `input_shape` : `Tuple[int, ...]`
        - 输入形状

    Returns
    ----------
    - `Tuple[int, ...]`
        - 输出形状
    """
    train_state = model.training
    shape = None
    with torch.no_grad():
        model.eval()
        shape = model(torch.randn(input_shape)).shape
    model.train(train_state)
    return shape
