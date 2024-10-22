from copy import deepcopy
from typing import Any, Callable, Dict, List, Literal, Optional, Union

import torch
from lightning.fabric import Fabric
from torch import nn
from torch.optim.lr_scheduler import _LRScheduler
from torch.utils.data import DataLoader
from torchmetrics import Metric, MetricCollection

from zyplib.train.fabric.callbacks import FabricLogMetrics
from zyplib.train.metric.torch_metric import TorchMetricRecorder
from zyplib.train.utils import prefixed_dict, step_lr_sched
from zyplib.utils.print import print_info
from zyplib.utils.progress_bar import rich_progress


class BasicFabricTrainer:
    def __init__(
        self,
        fabric: Fabric,
        model: nn.Module,
        optimizer: torch.optim.Optimizer,
        fn_loss: nn.Module = None,
        hparams: Optional[Dict[str, Any]] = None,
        metrics: Optional[Union[MetricCollection, Dict[str, Metric]]] = None,
        before_metric: Optional[
            Union[Literal['sigmoid', 'softmax'], Callable, nn.Module]
        ] = None,
        lr_scheduler: Optional[_LRScheduler] = None,
        lr_sched_freq: int = 1,
        lr_sched_interval: str = 'epoch',
    ):
        self.fabric = fabric
        self.fabric.launch()

        self.hparams = deepcopy(hparams) if hparams is not None else None

        self.train_metric = TorchMetricRecorder(metrics, before_metric=before_metric)
        self.val_metric = TorchMetricRecorder(metrics, before_metric=before_metric)

        self.model = model
        self.optimizer = optimizer
        self.fn_loss = fn_loss or nn.BCEWithLogitsLoss()
        self.lr_scheduler = lr_scheduler
        self.lr_sched_freq = lr_sched_freq
        self.lr_sched_interval = lr_sched_interval

        self.fabric_log_metrics = FabricLogMetrics(fabric)
        self.fabric._callbacks.append(self.fabric_log_metrics)

        self.early_stop = False  # 中断训练, 给 EarlyStopping 使用

    def training_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> Dict[str, Any]:
        self.model.train()
        x, y = batch

        self.optimizer.zero_grad()
        y_pred = self.model(x)
        loss = self.fn_loss(y_pred, y)
        self.fabric.backward(loss)
        self.optimizer.step()

        metrics = self.train_metric.update(y_pred, y, loss.item())
        self._callbacks(
            'on_train_batch_end',
            metrics=metrics,
            y_pred=y_pred,
            batch=batch,
            loss=loss.item(),
            batch_idx=batch_idx,
        )
        return metrics

    def validation_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> Dict[str, Any]:
        self.model.eval()
        with torch.no_grad():
            x, y = batch
            y_pred = self.model(x)
            loss = self.fn_loss(y_pred, y)

        metrics = self.val_metric.update(y_pred, y, loss.item())
        self._callbacks(
            'on_validation_batch_end',
            metrics=metrics,
            y_pred=y_pred,
            batch=batch,
            loss=loss.item(),
            batch_idx=batch_idx,
        )
        return metrics

    def test_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> Dict[str, Any]:
        self.model.eval()
        with torch.no_grad():
            x, y = batch
            y_pred = self.model(x)
            loss = self.fn_loss(y_pred, y)

        metrics = self.val_metric.update(y_pred, y, loss.item())
        self._callbacks(
            'on_test_batch_end',
            metrics=metrics,
            y_pred=y_pred,
            batch=batch,
            loss=loss.item(),
            batch_idx=batch_idx,
        )
        return metrics

    def train_epoch(self, train_loader: DataLoader, epoch_idx: int) -> Dict[str, float]:
        for batch_idx, batch in enumerate(
            rich_progress(train_loader, 'Training', color='green')
        ):
            self.training_step(batch, batch_idx)
        metrics = self.train_metric.compute()
        return metrics

    def val_epoch(self, val_loader: DataLoader, epoch_idx: int) -> Dict[str, float]:
        for batch_idx, batch in enumerate(
            rich_progress(val_loader, 'Validating', color='blue')
        ):
            self.validation_step(batch, batch_idx)
        metrics = self.val_metric.compute()
        return metrics

    def test_epoch(self, test_loader: DataLoader, epoch_idx: int) -> Dict[str, float]:
        for batch_idx, batch in enumerate(
            rich_progress(test_loader, 'Testing', color='blue')
        ):
            self.test_step(batch, batch_idx)
        metrics = self.val_metric.compute()
        return metrics

    def fit(
        self,
        train_loader: DataLoader,
        val_loader: Optional[DataLoader] = None,
        max_epochs: int = 10,
    ) -> Dict[str, List[float]]:
        self._callbacks('on_fit_start', max_epochs=max_epochs)

        self.model, self.optimizer = self.fabric.setup(self.model, self.optimizer)
        train_loader = self.fabric.setup_dataloaders(train_loader)
        if val_loader:
            val_loader = self.fabric.setup_dataloaders(val_loader)

        self._callbacks(
            'on_train_start',
            max_epochs=max_epochs,
            hparams=self.hparams,
            model=self.model,
            optimizer=self.optimizer,
            lr_scheduler=self.lr_scheduler,
            fabric=self.fabric,
        )

        for epoch in range(max_epochs):
            if self.early_stop:
                print_info('停止训练')
                break

            self._callbacks('on_train_epoch_start', epoch=epoch, max_epochs=max_epochs)

            train_metrics = self.train_epoch(train_loader, epoch)

            self._callbacks('on_train_epoch_end', metrics=train_metrics, epoch=epoch)

            if val_loader:
                self._callbacks('on_validation_epoch_start', epoch=epoch)

                val_metrics = self.val_epoch(val_loader, epoch)

                self._callbacks(
                    'on_validation_epoch_end', metrics=val_metrics, epoch=epoch
                )
            else:
                val_metrics = None

            if self.lr_scheduler and self.lr_sched_interval == 'epoch':
                if (epoch + 1) % self.lr_sched_freq == 0:
                    loss = train_metrics['loss']
                    if val_metrics:
                        loss = val_metrics['loss']
                    step_lr_sched(self.lr_scheduler, loss)

            self._callbacks(
                'on_epoch_end',
                epoch=epoch,
                train_metrics=train_metrics,
                val_metrics=val_metrics,
            )

        self._callbacks('on_train_end')
        self._callbacks('on_fie_end')

    def test(self, test_loader: DataLoader) -> Dict[str, float]:
        self._callbacks('on_test_start', dataloader=test_loader)
        test_loader = self.fabric.setup_dataloaders(test_loader)
        result = self.test_epoch(test_loader, 0)
        self._callbacks('on_test_end', metrics=result)
        return result

    def _callbacks(self, hook_name: str, **kwargs):
        """调用 fabric 的 callbacks

        Parameters
        ----------
        - `hook_name` : `str`
            - 钩子名称
        - `kwargs` : `Dict[str, Any]`
            - 传入的 hook 参数
        """
        self.fabric.call(hook_name, trainer=self, **kwargs)
