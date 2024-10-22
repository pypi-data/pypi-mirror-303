from typing import Any, Dict, Union

import torch
import torch.optim
from torch import nn

from zyplib.utils.time import now

from .shapes import output_shape

__all__ = [
    'output_shape',
    'weight_initializer',
    'save_checkpoint',
    'load_checkpoint',
    'freeze',
    'unfreeze',
]


def weight_initializer(m: nn.Module):
    if isinstance(m, (nn.Conv1d, nn.Conv2d, nn.Conv3d, nn.Linear)):
        nn.init.kaiming_normal_(m.weight.data, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
            nn.init.constant_(m.bias.data, 0)
    elif isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)):
        nn.init.constant_(m.weight.data, 1)
        nn.init.constant_(m.bias.data, 0)
    elif isinstance(m, nn.LSTM):
        for name, param in m.named_parameters():
            if 'weight' in name:
                nn.init.orthogonal_(param.data)
            elif 'bias' in name:
                nn.init.constant_(param.data, 0)
    elif isinstance(m, nn.GRU):
        for name, param in m.named_parameters():
            if 'weight' in name:
                nn.init.xavier_uniform_(param.data)
            elif 'bias' in name:
                nn.init.constant_(param.data, 0)
    elif isinstance(m, nn.MultiheadAttention):
        for param in m.parameters():
            if param.dim() > 1:
                nn.init.xavier_uniform_(param)


def save_checkpoint(
    models: Union[Dict[str, nn.Module], nn.Module],
    path: str,
    optimizers: Union[Dict[str, Any], Any] = None,
    epoch=None,
    loss=None,
    **kwargs,
):
    if isinstance(loss, torch.Tensor):
        loss = loss.item()

    if not isinstance(models, dict):
        models = {'model': models}
    if optimizers is not None and not isinstance(optimizers, dict):
        optimizers = {'optimizer': optimizers}

    checkpoint = {
        'models_state_dict': {name: model.state_dict() for name, model in models.items()},
        'optimizers_state_dict': {
            name: opt.state_dict() for name, opt in optimizers.items()
        }
        if optimizers
        else None,
        'epoch': epoch,
        'loss': loss,
        'save_time': now(),
        **kwargs,
    }
    checkpoint = {k: v for k, v in checkpoint.items() if v is not None}
    torch.save(checkpoint, path)


def load_checkpoint(
    models: Union[Dict[str, nn.Module], nn.Module],
    path: str,
    optimizers: Union[Dict[str, Any], Any] = None,
    device: Union[str, torch.device] = None,
) -> Dict[str, Any]:
    checkpoint = torch.load(path, map_location=device)

    if not isinstance(models, dict):
        models = {'model': models}
    if optimizers is not None and not isinstance(optimizers, dict):
        optimizers = {'optimizer': optimizers}

    for name, model in models.items():
        model.load_state_dict(checkpoint['models_state_dict'][name])

    if optimizers and 'optimizers_state_dict' in checkpoint:
        for name, optimizer in optimizers.items():
            if name in checkpoint['optimizers_state_dict']:
                optimizer.load_state_dict(checkpoint['optimizers_state_dict'][name])

    return checkpoint


def freeze(model: nn.Module):
    for param in model.parameters():
        param.requires_grad = False


def unfreeze(model: nn.Module):
    for param in model.parameters():
        param.requires_grad = True
