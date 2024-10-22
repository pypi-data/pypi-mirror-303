import os
from typing import Callable, Optional

from lightning.fabric import Fabric, loggers

from zyplib.utils.time import TIME_FMT, now

from . import trainer
from .callbacks import (
    FabricCallbackProtocol,
    ParseCSVLogfile,
    PrintTrainInfo,
    SaveCheckpoints,
    SaveHparams,
    find_callback,
)
from .procedure import (
    train_epoch,
    train_loop,
    training_step,
    val_epoch,
    validation_step,
)
from .trainer import BasicFabricTrainer

basic_trainer = trainer  # 兼容旧的模块命名

__all__ = [
    'BasicFabricTrainer',
    'default_fabric',
    'train_epoch',
    'train_loop',
    'training_step',
    'val_epoch',
    'validation_step',
    'find_callback',
]


def default_fabric(
    root_dir: str = './',
    dir_name: str = 'lightning_logs',
    version: str | None = None,
    save_every_k: Optional[int] = None,
    save_best: bool = True,
    keep_best_k: Optional[int] = 1,
    monitor: str = 'loss',
    less_is_better: bool = True,
    no_csv_logger: bool = False,
    no_tensorboard_logger: bool = False,
    no_print_info_cb: bool = False,
    no_save_checkpoints_cb: bool = False,
    no_save_hparams_cb: bool = False,
    fn_custom_logger: Optional[Callable[[str], list[loggers.Logger]]] = None,
    fn_custom_callback: Optional[Callable[[str], list[FabricCallbackProtocol]]] = None,
    **fabric_kwargs,
):
    """构建默认的fabric对象

    将 logger 和 checkpoint 保存在 `root_dir/dir_name/version` 目录下
    默认配置为`./lightning_logs/v2024_05_01-12_00_00`

    默认配置如下:
    - Loggers:
        - CSVLogger
        - TensorBoardLogger
    - Callbacks:
        - PrintTrainInfo
        - SaveHparams
        - SaveCheckpoints

    可以通过 `fn_custom_xxx` 参数来添加自定义的 logger 和 callback; 该回调函数传入 now 的时间字符串，需要返回一个 logger 或者 callback 的列表

    Parameters
    ----------
    - `root_dir` : `str`, optional
        - 日志保存的根目录, by default './'
    - `dir_name` : `str`, optional
        - 日志保存的目录名称, by default 'lightning_logs'
    - `version` : `str | None`, optional
        - 日志保存的版本, by default None
        - 默认为 `v{time_str}`
    - `save_every_k` : `Optional[int]`, SaveCheckpoints 的参数
        - 每多少个epoch保存一次模型, by default None
    - `save_best` : `bool`, SaveCheckpoints 的参数
        - _description_, by default True
    - `keep_best_k` : `Optional[int]`, SaveCheckpoints 的参数
        - 保存最好的k个模型, by default 1
    - `monitor` : `str`, SaveCheckpoints 的参数
        - 监控的指标, by default 'loss'
    - `less_is_better` : `bool`, SaveCheckpoints 的参数
        - 是否监控指标越小越好, by default True
    - `no_csv_logger` : `bool`, optional
        - 是否禁用CSVLogger, by default False
    - `no_tensorboard_logger` : `bool`, optional
        - 是否禁用TensorBoardLogger, by default False
    - `no_print_info_cb` : `bool`, optional
        - 是否禁用打印训练信息回调, by default False
    - `no_save_checkpoints_cb` : `bool`, optional
        - 是否禁用保存检查点回调, by default False
    - `no_save_hparams_cb` : `bool`, optional
        - 是否禁用保存超参数回调, by default False
    - `fn_custom_logger` : `(version: string) => Logger[]`, optional
        - 自定义 logger 的函数, by default None
    - `fn_custom_callback`: `(version: string) => FabricCallbackProtocol[]`
        - 自定义 callback 的函数, by default None

    Returns
    ----------
    - `fabric` : `Fabric`
        - Fabric 对象; 注意只返回 fabric，不自动调用 fabric.launch()
    """
    time_str = now(TIME_FMT.DATE_TIME_UNDERSCORE)
    version = version or f'v{time_str}'
    _loggers = []
    _callbacks = []

    # Add loggers if not disabled
    if not no_csv_logger:
        csv = loggers.CSVLogger(root_dir=root_dir, name=dir_name, version=version)
        _loggers.append(csv)
        parser = ParseCSVLogfile(os.path.join(csv.log_dir, 'metrics.csv'))
        _callbacks.append(parser)
    if not no_tensorboard_logger:
        _loggers.append(
            loggers.TensorBoardLogger(
                root_dir=root_dir, name=dir_name, version=version
            )
        )

    if fn_custom_logger:
        custom_loggers = fn_custom_logger(version)
        if isinstance(custom_loggers, list):
            _loggers.extend(custom_loggers)
        else:
            raise ValueError(
                f'fn_custom_logger must return a list of loggers, but got {type(custom_loggers)}'
            )

    # Add callbacks if not disabled
    if not no_print_info_cb:
        _callbacks.append(PrintTrainInfo())
    if not no_save_hparams_cb:
        _callbacks.append(SaveHparams(dir=f'{root_dir}/{dir_name}/{version}'))
    if not no_save_checkpoints_cb:
        _callbacks.append(
            SaveCheckpoints(
                dir=f'{root_dir}/{dir_name}/{version}/checkpoints',
                save_every_k=save_every_k,
                save_best=save_best,
                keep_best_k=keep_best_k,
                monitor=monitor,
                less_is_better=less_is_better,
            )
        )
    if fn_custom_callback:
        custom_callbacks = fn_custom_callback(version)
        if isinstance(custom_callbacks, list):
            _callbacks.extend(custom_callbacks)
        else:
            raise ValueError(
                f'fn_custom_callback must return a list of callbacks, but got {type(custom_callbacks)}'
            )

    fabric = Fabric(loggers=_loggers, callbacks=_callbacks, **fabric_kwargs)
    return fabric
