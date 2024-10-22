from collections import OrderedDict
from typing import Dict, Optional, Union

import numpy as np
import torch
from torch import nn


def module_grad_norm(module: nn.Module, p_norm: int = 2) -> float:
    """计算 module 当前所有参数的梯度的范数

    moduleGradNorm 的计算结果为 module 中所有子模块的 parameter 组成的向量的 norm

    Parameters:
    ----------
        - `module`: `torch.nn.Module`
        - `p_norm`: `int`, 范数阶数

    Returns:
    ----------
        - `total_grad_norm`: `float`
    """
    params = filter(lambda p: p.grad is not None, module.parameters())
    sum_grad_norm = 0
    for p in params:
        grad = p.grad.detach().norm(p_norm).item()
        sum_grad_norm += grad**p_norm
    total_grad_norm = sum_grad_norm ** (1 / p_norm)
    return total_grad_norm


def param_grad_norm(module: nn.Module, p_norm: int = 2) -> Dict[str, float]:
    """分别计算 module 内各个 parameter 梯度的范数，以字典的格式返回

    Parameters:
    ----------
        - `module`: `torch.nn.Module`
        - `p_norm`: `int`, 范数阶数

    Returns:
    ----------
        - `grads`: `dict`, `{parameter_name: norm}`
    """
    norms = {}
    for name, p in module.named_parameters():
        if p.grad is not None:
            grad = p.grad.detach().norm(p_norm).item()
            norms[name] = grad
    return norms


def grad_norm(
    module: nn.Module, p_norm: int = 2, type: str = 'module'
) -> Union[float, dict]:
    """计算 module 梯度的范数

    根据 type 的不同，采用不同的方式计算; 本质上是调用其他两个函数

    Parameters:
    ----------
        - `module`: `torch.nn.Module`
        - `p_norm`: `int`, 范数阶数
        - `type`:   `int`, 返回类型
            - 'module': 计算整个 module 梯度的范数，调用 `moduleGradNorm`，返回 float
            - 'param':  计算 module 各个 parameter 的范数，调用 `paramGradNorm`，返回 dict

    Returns:
    ----------
        - ans: `Union[float, dict]`
    """
    if type == 'module':
        return module_grad_norm(module, p_norm)
    elif type == 'param':
        return param_grad_norm(module, p_norm)
    else:
        return ValueError(f'Invalid argument type: {type}')
