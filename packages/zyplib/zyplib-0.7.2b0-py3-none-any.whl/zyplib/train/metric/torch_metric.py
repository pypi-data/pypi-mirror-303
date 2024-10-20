from typing import Callable, Dict, List, Literal, Optional, Union

# import matplotlib.pyplot as plt
import torch
from torch import nn
from torchmetrics import Metric, MetricCollection


class TorchMetricRecorder:
    def __init__(
        self,
        metrics: Optional[Union[MetricCollection, Dict[str, Metric]]],
        before_metric: Optional[
            Union[Literal['sigmoid', 'softmax'], Callable, nn.Module]
        ] = None,
    ):
        """添加基于 `torchmetrics` 的日志评估指标的功能

        Parameters
        ----------
        - `metrics` : `MetricCollection | Dict[str, Metric]`, optional
            - 评估指标
            - 使用 `torchmetrics.MetricCollection` 或 `dict` 类型
        - `before_metric` : `'sigmoid' | 'softmax' | Callable | nn.Module`, optional
            - 在计算评估指标之前的激活函数
            - 例如在二分类问题中，模型最后一层没有激活函数，而在计算评估指标 (即 `metrics`) 之前需要使用 `torch.sigmoid` 激活
        """
        if before_metric == 'sigmoid':
            self.before_metric = torch.sigmoid
        elif before_metric == 'softmax':
            self.before_metric = torch.softmax
        else:
            self.before_metric = before_metric

        if metrics is None:
            self.metrics = MetricCollection({})
        elif isinstance(metrics, dict):
            self.metrics = MetricCollection(metrics)
        else:
            self.metrics = metrics

        self.step_history = {metric_name: [] for metric_name in self.metrics.keys()}
        self.step_history['loss'] = []
        self.epoch_history = []

        self.current_epoch = 0
        self.current_step = 0

        self.epoch_metrics = {
            metric_name: metric.clone() for metric_name, metric in self.metrics.items()
        }
        self.epoch_losses = []

    def update(self, y_hat, y, loss: Optional[float] = None):
        """更新某个 step 的评估指标

        Parameters
        ----------
        - `y_hat` : `torch.Tensor`
            - 预测值
        - `y` : `torch.Tensor`
            - 真实值
        - `loss` : `float?`, optional
            - 损失值, 注意是 `float` 类型, 需要使用 `item()` 方法获取
        """
        result = {}

        if self.before_metric is not None:
            y_hat_activated = self.before_metric(y_hat)
        else:
            y_hat_activated = y_hat

        # Log loss if provided
        if loss is not None:
            if isinstance(loss, torch.Tensor):
                loss = loss.item()
            self.step_history['loss'].append(loss)
            self.epoch_losses.append(loss)
            result['loss'] = loss

        # Compute and log metrics
        for metric_name, metric in self.metrics.items():
            step_metric_value = metric(y_hat_activated, y)
            result[metric_name] = step_metric_value.item()
            self.step_history[metric_name].append(step_metric_value.item())

            # Update epoch-level metrics
            self.epoch_metrics[metric_name].update(y_hat_activated, y)

        self.current_step += 1
        return result

    def compute(self):
        """计算一个 epoch 的评估指标; 在每个 epoch 结束时调用"""
        epoch_metrics = {}

        # Compute epoch-level loss
        if self.epoch_losses:
            epoch_loss = sum(self.epoch_losses) / len(self.epoch_losses)
            epoch_metrics['loss'] = epoch_loss
            # self.fn_logging('epoch_loss', epoch_loss)

        # Compute and log epoch-level metrics
        for metric_name, metric in self.epoch_metrics.items():
            epoch_metric_value = metric.compute()
            epoch_metrics[metric_name] = epoch_metric_value.item()
            # self.fn_logging(f'epoch_{metric_name}', epoch_metric_value.item())
            metric.reset()

        self.epoch_history.append(epoch_metrics)
        self.current_epoch += 1
        self.current_step = 0
        self.epoch_losses = []
        return epoch_metrics

    def get_history(
        self, metric_name: str, level: Literal['step', 'epoch'] = 'step'
    ) -> List[float]:
        if level == 'step':
            return self.step_history[metric_name]
        elif level == 'epoch':
            return [
                epoch[metric_name] for epoch in self.epoch_history if metric_name in epoch
            ]
        else:
            raise ValueError("Level must be either 'step' or 'epoch'")
