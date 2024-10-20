import inspect
import os
import random
from functools import lru_cache
from typing import Optional, Union

import numpy as np
import torch
from simple_inject import inject
from torch import nn

from zyplib.utils.print import print_debug


def seed_everything(seed: int):
    os.environ['PL_GLOBAL_SEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def step_lr_sched(
    scheduler: torch.optim.lr_scheduler.LRScheduler,
    metrics: Optional[Union[float, torch.Tensor]] = None,
):
    """step lr scheduler"""
    # scheduler.step()
    if isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
        scheduler.step(metrics)
    else:
        scheduler.step()


def prefixed_dict(prefix: str, d: dict):
    """给字典的每个键值对添加前缀

    >>> dic = torch_metric.compute()
    >>> prefixed_dict('val_', dic)
    >>> {'val_loss': 0.1, 'val_acc': 0.9}


    Parameters
    ----------
    - `prefix` : `str`
        - 前缀
    - `d` : `dict`
        - 需要添加前缀的字典

    Returns
    ----------
    - `dict`
        - 添加前缀后的字典
    """
    return {f'{prefix}{k}': v for k, v in d.items()}


@lru_cache
def cuda_available():
    return torch.cuda.is_available()


@lru_cache
def default_device():
    return torch.device('cuda' if cuda_available() else 'cpu')


def use_device(
    x: Union[torch.Tensor, nn.Module],
    device: Optional[Union[str, torch.device]] = None,
    hint: bool = False,
):
    """使用指定的设备

    依赖注入:
    ----------
    device 如果为 None，则首先会 inject('device') 来尝试获取设备名称，如果仍然为 None，则使用默认设备

    Parameters
    ----------
    - `x` : `torch.Tensor | nn.Module`
        - 需要移动的模型或张量
    - `device` : `str | torch.device`, optional
        - 设备名称或设备对象，如果为None，则使用默认设备
    - `hint` : `bool`, optional
        - 是否打印移动信息，默认不打印

    Returns
    ----------
    - `torch.Tensor | nn.Module`
        - 移动后的模型或张量
    """
    if device is None:
        device = inject('device', if_not_found='none')
    if device is None:
        device = default_device()

    if hint:
        print_debug(f'use_device: {x.__class__.__name__} --> {device}')
    return x.to(device)
