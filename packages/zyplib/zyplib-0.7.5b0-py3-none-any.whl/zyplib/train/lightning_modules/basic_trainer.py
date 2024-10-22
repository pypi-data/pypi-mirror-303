from functools import partial
from typing import Callable, Dict, Literal, Optional, Union

import lightning as L
import torch
from torch import nn
from torch.optim.lr_scheduler import _LRScheduler
from torchmetrics import Metric, MetricCollection

from zyplib.train.metric.torch_metric import TorchMetricRecorder
from zyplib.train.utils import prefixed_dict


class BasicLightningTrainer(L.LightningModule):
    def __init__(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer,
        fn_loss: nn.Module = None,
        metrics: Optional[Union[MetricCollection, Dict[str, Metric]]] = None,
        before_metric: Optional[
            Union[Literal['sigmoid', 'softmax'], Callable, nn.Module]
        ] = None,
        lr_scheduler: Optional[_LRScheduler] = None,
        lr_sched_freq: int = 1,
        lr_sched_interval: str = 'epoch',
    ):
        """一个基础常用的 LightningModule Trainer

        Parameters
        ----------
        - `model` : `nn.Module`
            - 模型
        - `optimizer` : `torch.optim.Optimizer`
            - 优化器
        - `fn_loss` : `nn.Module`, optional
            - 损失函数
        - `metrics` : `MetricCollection | Dict[str, Metric]`, optional
            - 评估指标
            - 使用 `torchmetrics.MetricCollection` 或 `dict` 类型
        - `before_metric` : `'sigmoid' | 'softmax' | Callable | nn.Module`, optional
            - 在计算评估指标之前的激活函数
            - 例如在二分类问题中，模型最后一层没有激活函数，而在计算评估指标 (即 `metrics`) 之前需要使用 `torch.sigmoid` 激活
        - `lr_scheduler` : `torch.optim.lr_scheduler._LRScheduler`, optional
            - 学习率调度器
        - `lr_sched_freq` : `int`, optional
            - 学习率调度器更新频率
        - `lr_sched_interval` : `str`, optional
            - 学习率调度器更新间隔
        """
        L.LightningModule.__init__(self)

        self.train_metric = TorchMetricRecorder(metrics, before_metric=before_metric)
        self.val_metric = TorchMetricRecorder(metrics, before_metric=before_metric)
        self.test_metric = TorchMetricRecorder(metrics, before_metric=before_metric)

        self.model = model
        self.optimizer = optimizer
        self.fn_loss = fn_loss or nn.BCEWithLogitsLoss()
        self.lr_scheduler = lr_scheduler
        self.lr_sched_freq = lr_sched_freq
        self.lr_sched_interval = lr_sched_interval

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = self.fn_loss(y_hat, y)
        result = self.train_metric.update(y_hat, y, loss=loss.item())
        self.log_dict(prefixed_dict('train_', result), prog_bar=True, on_epoch=True, on_step=False)
        return loss

    def on_train_epoch_end(self) -> None:
        self.train_metric.compute()
        # print('train_result', result)

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = self.fn_loss(y_hat, y)
        result = self.val_metric.update(y_hat, y, loss=loss.item())
        self.log_dict(prefixed_dict('val_', result), prog_bar=True, on_epoch=True, on_step=False)
        return loss

    def on_validation_epoch_end(self) -> None:
        self.val_metric.compute()
        # print('val_result', result)

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = self.fn_loss(y_hat, y)
        result = self.test_metric.update(y_hat, y, loss=loss.item())
        self.log_dict(prefixed_dict('test_', result), prog_bar=True, on_epoch=True, on_step=False)
        return loss

    def on_test_epoch_end(self) -> None:
        self.test_metric.compute()
        # print('test_result', result)

    def configure_optimizers(self):
        if self.lr_scheduler is None:
            return self.optimizer
        return {
            'optimizer': self.optimizer,
            'lr_scheduler': {
                'scheduler': self.lr_scheduler,
                'interval': self.lr_sched_interval,
                'frequency': self.lr_sched_freq,
                'monitor': 'val_loss',
            },
        }
