from typing import Any, Callable, Dict, List, Optional, Union

import numpy as np
import torch
from lightning.fabric import Fabric
from torch import nn
from torch.utils.data import DataLoader

from zyplib.train.metric.torch_metric import TorchMetricRecorder
from zyplib.train.utils import step_lr_sched
from zyplib.utils.progress_bar import rich_progress


def training_step(
    model: nn.Module,
    batch: tuple[torch.Tensor, torch.Tensor],
    optimizer: torch.optim.Optimizer,
    fn_loss: nn.Module,
    fabric: Fabric | None = None,
    metric_recorder: TorchMetricRecorder | None = None,
) -> Dict[str, Any]:
    """单个训练步骤

    Parameters
    ----------
    - `model` : `nn.Module`
        - 模型
    - `batch` : `tuple[torch.Tensor, torch.Tensor]`
        - 数据批次
    - `optimizer` : `torch.optim.Optimizer`
        - 优化器
    - `fn_loss` : `nn.Module`
        - 损失函数: `fn_loss(y_pred, y)`
    - `fabric` : `Fabric | None`, optional
        - 可选项, 如果传入了, 则会调用 fabric 的 `backward` 和 `callback`
    - `metric_recorder` : `TorchMetricRecorder | None`, optional
        - 用于记录指标的 recorder 实例，默认为 None

    Returns
    ----------
    - `Dict[str, Any]`: 计算的指标; 至少包含 `loss`
    """
    model.train()
    x, y = batch

    optimizer.zero_grad()
    y_pred = model(x)
    loss: torch.Tensor = fn_loss(y_pred, y)
    if fabric:
        fabric.backward(loss)
    else:
        loss.backward()
    optimizer.step()

    if metric_recorder:
        metrics = metric_recorder.update(y_pred, y, loss.item())
    else:
        metrics = {'loss': loss.item()}
    if fabric:
        fabric.call('on_train_batch_end', metrics=metrics)
    return metrics


def validation_step(
    model: nn.Module,
    batch: tuple[torch.Tensor, torch.Tensor],
    fn_loss: nn.Module,
    fabric: Fabric | None = None,
    metric_recorder: TorchMetricRecorder | None = None,
) -> Dict[str, Any]:
    """单个验证步骤

    Parameters
    ----------
    - `model` : `nn.Module`
        - 模型
    - `batch` : `tuple[torch.Tensor, torch.Tensor]`
        - 数据批次
    - `fn_loss` : `nn.Module`
        - 损失函数: `fn_loss(y_pred, y)`
    - `fabric` : `Fabric | None`, optional
        - 可选项, 如果传入了, 则会调用 fabric 的 `callback`
    - `metric_recorder` : `TorchMetricRecorder | None`, optional
        - 用于记录指标的 recorder 实例，默认为 None

    Returns
    ----------
    - `Dict[str, Any]`: 计算的指标; 至少包含 `loss`
    """
    model.eval()
    with torch.no_grad():
        x, y = batch
        y_pred = model(x)
        loss: torch.Tensor = fn_loss(y_pred, y)

    if metric_recorder:
        metrics = metric_recorder.update(y_pred, y, loss.item())
    else:
        metrics = {'loss': loss.item()}

    if fabric:
        fabric.call('on_validation_batch_end', metrics=metrics)
    return metrics


def train_epoch(
    model: nn.Module,
    train_loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    fn_loss: nn.Module,
    epoch_idx: int | None = None,
    fabric: Fabric | None = None,
    metric_recorder: TorchMetricRecorder | None = None,
    fn_train_step: Callable = training_step,
    **train_step_kwargs: Any,
) -> Dict[str, float]:
    """单个训练轮次

    Parameters
    ----------
    - `model` : `nn.Module`
        - 模型
    - `train_loader` : `DataLoader`
        - 训练数据加载器
    - `optimizer` : `torch.optim.Optimizer`
        - _description_
    - `fn_loss` : `nn.Module`
        - 损失函数
    - `epoch_idx` : `int | None`, optional
        - 当前轮次索引, 默认为 None
    - `fabric` : `Fabric | None`, optional
        - 可选项, 如果传入了, 则会调用 fabric 的 `callback`
    - `metric_recorder` : `TorchMetricRecorder | None`, optional
        - 用于记录指标的 recorder 实例，默认为 None
    - `fn_train_step` : `(...) -> Dict[str, Any]`, optional
        - 可选项, 用于计算单个训练步骤的函数, 默认为 `training_step`

    `fn_train_step`:
    ----------
    - 默认不提供, 使用 `procedure.training_step`; 如果提供了, 则使用提供的函数
    - 接受以下的关键字参数:
        - `['model', 'batch', 'optimizer', 'fn_loss', 'fabric', 'metric_recorder']`
    - 返回值: `Dict[str, Any]`, 至少包含 `loss`
    Returns
    ----------
    - `Dict[str, float]`: 本 Epoch 的平均指标, 至少包含 `loss`
    """
    if fabric:
        fabric.call('on_train_epoch_start', epoch=epoch_idx)

    losses = []
    for batch in rich_progress(train_loader, 'Training', color='green'):
        metrics = fn_train_step(
            model=model,
            batch=batch,
            optimizer=optimizer,
            fn_loss=fn_loss,
            fabric=fabric,
            metric_recorder=metric_recorder,
            **train_step_kwargs,
        )
        losses.append(metrics['loss'])
    metrics = metric_recorder.compute() if metric_recorder else {'loss': np.mean(losses)}
    if fabric:
        fabric.call('on_train_epoch_end', metrics=metrics, epoch=epoch_idx)
    return metrics


def val_epoch(
    model: nn.Module,
    val_loader: DataLoader,
    fn_loss: nn.Module,
    epoch_idx: int | None = None,
    fabric: Fabric | None = None,
    metric_recorder: TorchMetricRecorder | None = None,
    fn_val_step: Callable = validation_step,
    **val_step_kwargs: Any,
) -> Dict[str, float]:
    """单个验证轮次

    Parameters
    ----------
    - `model` : `nn.Module`
        - 模型
    - `val_loader` : `DataLoader`
        - 验证数据加载器
    - `fn_loss` : `nn.Module`
        - 损失函数
    - `epoch_idx` : `int | None`, optional
        - 当前轮次索引, 默认为 None
    - `fabric` : `Fabric | None`, optional
        - 可选项, 如果传入了, 则会调用 fabric 的 `callback`
    - `metric_recorder` : `TorchMetricRecorder | None`, optional
        - 用于记录指标的 recorder 实例，默认为 None
    - `fn_val_step` : `(...) -> Dict[str, Any]`, optional
        - 可选项, 用于计算单个验证步骤的函数, 默认为 `validation_step`

    `fn_val_step`:
    ----------
    - 默认不提供, 使用 `procedure.validation_step`; 如果提供了, 则使用提供的函数
    - 接受以下的关键字参数:
        - `['model', 'batch', 'fn_loss', 'fabric', 'metric_recorder']`
    - 返回值: `Dict[str, Any]`, 至少包含 `loss`

    Returns
    ----------
    - `Dict[str, float]`: 本 Epoch 的平均指标, 至少包含 `loss`
    """
    if fabric:
        fabric.call('on_validation_epoch_start', epoch=epoch_idx)
    losses = []
    for batch in rich_progress(val_loader, 'Validating', color='blue'):
        metrics = fn_val_step(
            model=model,
            batch=batch,
            fn_loss=fn_loss,
            fabric=fabric,
            metric_recorder=metric_recorder,
            **val_step_kwargs,
        )
        losses.append(metrics['loss'])
    metrics = metric_recorder.compute() if metric_recorder else {'loss': np.mean(losses)}
    if fabric:
        fabric.call('on_validation_epoch_end', metrics=metrics, epoch=epoch_idx)
    return metrics


def train_loop(
    fabric: Fabric,  # 如果使用 train_loop, 则默认必须用 fabric
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    train_loader: DataLoader,
    val_loader: Optional[DataLoader],
    fn_loss: nn.Module,
    max_epochs: int,
    train_metric_recorder: TorchMetricRecorder | None = None,
    val_metric_recorder: TorchMetricRecorder | None = None,
    lr_scheduler: Optional[torch.optim.lr_scheduler._LRScheduler] = None,
    lr_sched_freq: int = 1,
    lr_sched_interval: str = 'epoch',
) -> Dict[str, List[float]]:
    """基于 Fabric 的 Train Loop; fabric 为必选参数，如果不想用 fabric 可以自行组合 train_epoch etc."""
    # fabric setup
    model, optimizer = fabric.setup(model, optimizer)
    train_loader = fabric.setup_dataloaders(train_loader)
    if val_loader:
        val_loader = fabric.setup_dataloaders(val_loader)

    fabric.call(
        'on_train_start',
        model=model,
        optimizer=optimizer,
        lr_scheduler=lr_scheduler,
        fabric=fabric,
    )

    for epoch in range(max_epochs):
        fabric.call('on_train_epoch_start', epoch=epoch, max_epochs=max_epochs)

        train_metrics = train_epoch(
            model, train_loader, optimizer, fn_loss, fabric, train_metric_recorder
        )

        fabric.call('on_train_epoch_end', metrics=train_metrics, epoch=epoch)

        if val_loader:
            fabric.call('on_validation_epoch_start', epoch=epoch)
            val_metrics = val_epoch(model, val_loader, fn_loss, val_metric_recorder)
            fabric.call('on_validation_epoch_end', metrics=val_metrics, epoch=epoch)
        else:
            val_metrics = None

        if lr_scheduler and lr_sched_interval == 'epoch':
            if (epoch + 1) % lr_sched_freq == 0:
                loss = val_metrics['loss'] if val_metrics else train_metrics['loss']
                step_lr_sched(lr_scheduler, loss)

        fabric.call(
            'on_epoch_end',
            epoch=epoch,
            train_metrics=train_metrics,
            val_metrics=val_metrics,
        )

    fabric.call('on_train_end')

    return {'train': train_metrics, 'val': val_metrics}
