from abc import ABCMeta
from typing import Any, Callable, Dict, Literal, Union

import torch
from torch import nn
from torch.nn import Module

from zyplib.nn import utils as nn_utils
from zyplib.utils.print import print_info
from zyplib.utils.time import now

XDim = Literal['1d', '2d', '3d', 1, 2, 3]
Conv = Union[nn.Conv1d, nn.Conv2d, nn.Conv3d]
BatchNorm = Union[nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d]
MaxPool = Union[nn.MaxPool1d, nn.MaxPool2d, nn.MaxPool3d]
AvgPool = Union[nn.AvgPool1d, nn.AvgPool2d, nn.AvgPool3d]
AdaptiveAvgPool = Union[nn.AdaptiveAvgPool1d, nn.AdaptiveAvgPool2d, nn.AdaptiveAvgPool3d]
AdaptiveMaxPool = Union[nn.AdaptiveMaxPool1d, nn.AdaptiveMaxPool2d, nn.AdaptiveMaxPool3d]
ConvTranspose = Union[nn.ConvTranspose1d, nn.ConvTranspose2d, nn.ConvTranspose3d]
Dropout = Union[nn.Dropout, nn.Dropout2d, nn.Dropout3d]


def conv(xdim: XDim = 1) -> Conv:
    if xdim == '1d':
        return nn.Conv1d
    elif xdim == '2d':
        return nn.Conv2d
    elif xdim == '3d':
        return nn.Conv3d
    elif xdim == 1:
        return nn.Conv1d
    elif xdim == 2:
        return nn.Conv2d
    elif xdim == 3:
        return nn.Conv3d
    else:
        raise ValueError(f'Invalid parameter xdim: {xdim}; 无法转换为对应的 Conv 类')


def batchnorm(xdim: XDim = 1) -> nn.Module:
    if xdim == '1d':
        return nn.BatchNorm1d
    elif xdim == '2d':
        return nn.BatchNorm2d
    elif xdim == '3d':
        return nn.BatchNorm3d
    elif xdim == 1:
        return nn.BatchNorm1d
    elif xdim == 2:
        return nn.BatchNorm2d
    elif xdim == 3:
        return nn.BatchNorm3d
    else:
        raise ValueError(f'Invalid parameter xdim: {xdim}; 无法转换为对应的 BatchNorm 类')


def maxpool(xdim: XDim = 1) -> MaxPool:
    if xdim == '1d':
        return nn.MaxPool1d
    elif xdim == '2d':
        return nn.MaxPool2d
    elif xdim == '3d':
        return nn.MaxPool3d
    elif xdim == 1:
        return nn.MaxPool1d
    elif xdim == 2:
        return nn.MaxPool2d
    elif xdim == 3:
        return nn.MaxPool3d
    else:
        raise ValueError(f'Invalid parameter xdim: {xdim}; 无法转换为对应的 MaxPool 类')


def avgpool(xdim: XDim = 1) -> AvgPool:
    if xdim == '1d':
        return nn.AvgPool1d
    elif xdim == '2d':
        return nn.AvgPool2d
    elif xdim == '3d':
        return nn.AvgPool3d
    elif xdim == 1:
        return nn.AvgPool1d
    elif xdim == 2:
        return nn.AvgPool2d
    elif xdim == 3:
        return nn.AvgPool3d
    else:
        raise ValueError(f'Invalid parameter xdim: {xdim}; 无法转换为对应的 AvgPool 类')


def adaptiveavgpool(xdim: XDim = 1) -> AdaptiveAvgPool:
    if xdim == '1d':
        return nn.AdaptiveAvgPool1d
    elif xdim == '2d':
        return nn.AdaptiveAvgPool2d
    elif xdim == '3d':
        return nn.AdaptiveAvgPool3d
    elif xdim == 1:
        return nn.AdaptiveAvgPool1d
    elif xdim == 2:
        return nn.AdaptiveAvgPool2d
    elif xdim == 3:
        return nn.AdaptiveAvgPool3d
    else:
        raise ValueError(
            f'Invalid parameter xdim: {xdim}; 无法转换为对应的 AdaptiveAvgPool 类'
        )


def adaptivemaxpool(xdim: XDim = 1) -> AdaptiveMaxPool:
    if xdim == '1d':
        return nn.AdaptiveMaxPool1d
    elif xdim == '2d':
        return nn.AdaptiveMaxPool2d
    elif xdim == '3d':
        return nn.AdaptiveMaxPool3d
    elif xdim == 1:
        return nn.AdaptiveMaxPool1d
    elif xdim == 2:
        return nn.AdaptiveMaxPool2d
    elif xdim == 3:
        return nn.AdaptiveMaxPool3d
    else:
        raise ValueError(
            f'Invalid parameter xdim: {xdim}; 无法转换为对应的 AdaptiveMaxPool 类'
        )


def convtranspose(xdim: XDim = 1) -> ConvTranspose:
    if xdim == '1d':
        return nn.ConvTranspose1d
    elif xdim == '2d':
        return nn.ConvTranspose2d
    elif xdim == '3d':
        return nn.ConvTranspose3d
    elif xdim == 1:
        return nn.ConvTranspose1d
    elif xdim == 2:
        return nn.ConvTranspose2d
    elif xdim == 3:
        return nn.ConvTranspose3d
    else:
        raise ValueError(
            f'Invalid parameter xdim: {xdim}; 无法转换为对应的 ConvTranspose 类'
        )


def dropout(xdim: XDim = 1) -> Dropout:
    if xdim == '1d':
        return nn.Dropout
    elif xdim == '2d':
        return nn.Dropout2d
    elif xdim == '3d':
        return nn.Dropout3d
    elif xdim == 1:
        return nn.Dropout
    elif xdim == 2:
        return nn.Dropout2d
    elif xdim == 3:
        return nn.Dropout3d
    else:
        raise ValueError(f'Invalid parameter xdim: {xdim}; 无法转换为对应的 Dropout 类')


class BaseModule(Module):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

    def __hash__(self) -> int:
        return hash(str(self))

    def init_weights(self, weight_init_func=None):
        if weight_init_func is None:
            self.apply(nn_utils.weight_initializer)
        else:
            self.apply(weight_init_func)

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    def freeze(self):
        nn_utils.freeze(self)

    def unfreeze(self):
        nn_utils.unfreeze(self)

    def save_checkpoint(self, path: str, optimizer=None, epoch=None, loss=None, **kwargs):
        nn_utils.save_checkpoint(self, path, optimizer, epoch, loss, **kwargs)

    def load_checkpoint(self, path: str, optimizer=None, device=None) -> Dict[str, Any]:
        nn_utils.load_checkpoint(self, path, optimizer, device)

    def summary(self):
        print_info(f'Model Architecture:\n{self}')
        print_info(f'Total trainable parameters: {self.count_parameters():,}')


class WrapFunc(nn.Module):
    def __init__(self, fn: Callable):
        super().__init__()
        self.fn = fn

    def forward(self, *args, **kwargs):
        return self.fn(*args, **kwargs)
