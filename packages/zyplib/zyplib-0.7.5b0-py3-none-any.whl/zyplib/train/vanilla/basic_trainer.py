from typing import Any, Callable, Dict, List, Literal, Optional, Union

import torch
from torch import nn
from torch.optim.lr_scheduler import _LRScheduler
from torch.utils.data import DataLoader
from torchmetrics import Metric, MetricCollection

from zyplib.train.metric.torch_metric import TorchMetricRecorder
from zyplib.train.utils import step_lr_sched, use_device
from zyplib.utils.print import print_info
from zyplib.utils.progress_bar import rich_progress


class BasicTrainer:
    def __init__(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer,
        fn_loss: nn.Module = None,
        metrics: Optional[Union[MetricCollection, Dict[str, Metric]]] = None,
        device: str = 'cuda' if torch.cuda.is_available() else 'cpu',
        lr_scheduler: Optional[_LRScheduler] = None,
        lr_sched_freq: int = 1,
        lr_sched_interval: str = 'epoch',
        before_metric: Optional[
            Union[Literal['sigmoid', 'softmax'], Callable, nn.Module]
        ] = None,
    ):
        self.train_metric = TorchMetricRecorder(metrics, before_metric=before_metric)
        self.val_metric = TorchMetricRecorder(metrics, before_metric=before_metric)

        self.model = use_device(model, device)
        self.optimizer = optimizer
        self.fn_loss = fn_loss or nn.BCEWithLogitsLoss()
        self.device = device
        self.lr_scheduler = lr_scheduler
        self.lr_sched_freq = lr_sched_freq
        self.lr_sched_interval = lr_sched_interval

    def training_step(self, batch: tuple[torch.Tensor, torch.Tensor]) -> Dict[str, Any]:
        self.model.train()
        x, y = use_device(batch[0], self.device), use_device(batch[1], self.device)

        self.optimizer.zero_grad()
        y_pred = self.model(x)
        loss = self.fn_loss(y_pred, y)
        loss.backward()
        self.optimizer.step()

        return self.train_metric.update(y_pred, y, loss.item())

    def validation_step(self, batch: Dict[str, torch.Tensor]) -> Dict[str, Any]:
        self.model.eval()
        with torch.no_grad():
            x, y = use_device(batch[0], self.device), use_device(batch[1], self.device)
            y_pred = self.model(x)
            loss = self.fn_loss(y_pred, y)

        return self.val_metric.update(y_pred, y, loss.item())

    def train_epoch(self, train_loader: DataLoader) -> Dict[str, float]:
        for batch in rich_progress(train_loader, 'Training', color='green'):
            self.training_step(batch)
        return self.train_metric.compute()

    def val_epoch(self, val_loader: DataLoader) -> Dict[str, float]:
        for batch in rich_progress(val_loader, 'Validating', color='blue'):
            self.validation_step(batch)
        return self.val_metric.compute()

    def fit(
        self,
        train_loader: DataLoader,
        val_loader: Optional[DataLoader] = None,
        num_epochs: int = 10,
    ) -> Dict[str, List[float]]:
        for epoch in range(num_epochs):
            print_info(f'Epoch {epoch+1}/{num_epochs}'.center(50, '='))
            train_metrics = self.train_epoch(train_loader)

            if val_loader:
                val_metrics = self.val_epoch(val_loader)
            else:
                val_metrics = None

            print_info('\tTrain: ', end='')
            self._print_epoch_summary(train_metrics)
            if val_loader:
                print_info('\tVal: ', end='')
                self._print_epoch_summary(val_metrics)
            print()

            if self.lr_scheduler and self.lr_sched_interval == 'epoch':
                if (epoch + 1) % self.lr_sched_freq == 0:
                    loss = train_metrics['loss']
                    if val_metrics:
                        loss = val_metrics['loss']
                    step_lr_sched(self.lr_scheduler, loss)

    def test(self, test_loader: DataLoader) -> Dict[str, float]:
        result = self.val_epoch(test_loader)
        print_info('\tTest: ', end='')
        self._print_epoch_summary(result)
        return result

    def _print_epoch_summary(self, metrics: Dict[str, float]):
        for key, value in metrics.items():
            print_info(f'\t{key}: {value:.4f}', end='')
        print()
