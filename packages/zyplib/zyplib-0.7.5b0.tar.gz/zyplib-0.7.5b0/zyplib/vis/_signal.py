from typing import Callable, Literal

import matplotlib.pyplot as plt
import numpy as np


def plot_signals(
    signals: np.ndarray,
    srate: int,
    labels: list[str] | None = None,
    new_fig: bool = True,
    show=True,
    save_path=None,
    interval: float | Literal['auto'] = 'auto',
    fn_value_fmt: Callable[[float], str] | None = lambda x: f'{x:.2f}',
    cmap: str | Callable[[int], str] | None = 'black',
):
    """绘制多通道信号波形图

    Parameters
    ----------
    - `signals` : `np.ndarray`, [n_channels, n_samples]; 信号数据
    - `labels` : `list[str]`; 每个信号的标签
    - `srate` : `int`; 采样率
    - `new_fig` : `bool`, optional
        - 是否创建一个新的 figure。默认为 True
    - `show` : `bool`, optional
        - 是否显示绘图。默认为 True
    - `save_path` : `str`, optional
        - 保存绘图的路径。如果为 None，则不保存绘图。默认为 None
    - `interval` : `float | Literal['auto']`, optional
        - 不同通道在 Y 轴上的间隔, 默认 'auto' 表示自动计算
    - `fn_value_fmt` : `Callable[[float], str]`, optional
        - 用于格式化信号值的函数。默认为 `lambda x: f'{x:.2f}'`
    - `cmap` : `str | Callable[[int], str] | None`, optional
        - 用于绘制信号的 colormap。默认为 'black'
        - 也可以为一个 `int -> str` 的函数，int 为通道索引
    """
    n_channels, n_samples = signals.shape
    time = np.linspace(0, n_samples / srate, n_samples)

    labels = labels or [f'Ch{i}' for i in range(n_channels)]

    # 计算间隔
    if interval == 'auto':
        interval = 1.5 * np.max(np.abs(signals))

    # detrends
    signals = np.apply_along_axis(lambda x: x - np.mean(x), 1, signals)
    y_centers = np.arange(n_channels) * interval

    if new_fig:
        plt.figure(figsize=(15, n_channels * 2))
    for i in range(n_channels):
        c = cmap(i) if callable(cmap) else cmap
        plt.plot(time, signals[i] + y_centers[i], label=labels[i], color=c)

    plt.xlabel('Time (s)')
    plt.title('Multi-channel Signal Plot')
    plt.grid(True)

    # 左侧标注通道名称
    plt.yticks(y_centers, labels)

    # Y 轴右侧标注 signal 的 min/max
    ax = plt.gca()
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(y_centers)
    min_max_labels = [
        f'{fn_value_fmt(signals[i].min())}~{fn_value_fmt(signals[i].max())}'
        for i in range(n_channels)
    ]
    ax2.set_yticklabels(min_max_labels)
    # ax2.set_ylabel('Min / Max')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)

    if show:
        plt.show()
