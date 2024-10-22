"""
Matplotlib 相关的绘图工具
"""

from typing import Callable, Protocol

import matplotlib.pyplot as plt
import numpy as np

from ._style import register_mpl_styles


class MplFigureCallback(Protocol):
    """matplotlib 图表的最终处理函数类型; 比如可以在绘图后调用 `plt.show()` 等"""

    def __call__(self, fig: plt.Figure | None = None) -> None: ...


def mpl_figure_show(fig: plt.Figure | None = None):
    """显示 matplotlib 图表"""
    plt.show()


def make_grids(
    row: int = 1,
    col: int = 1,
    figsize: tuple = None,
    tight_layout: bool = True,
    fn_finalize: MplFigureCallback = mpl_figure_show,
    **subplots_kwargs,
):
    """创建 matplotlib 的子图网格，并逐个返回子图

    >>> for i, j, ax in make_grids(2, 3):
    ...     ax.plot(np.random.randn(100))

    >>> save_fig = lambda fig: fig.savefig('fig.png')
    >>> for i, j, ax in make_grids(2, 3, fn_finalize=save_fig):
    ...     ax.plot(np.random.randn(100))

    Parameters
    ----------
    - `row` : `int`, optional
        - 行数, 默认为 1
    - `col` : `int`, optional
        - 列数, 默认为 1
    - `figsize` : `tuple`, optional
        - 图形大小 (宽, 高), 单位为英寸, 默认为 None (使用 matplotlib 默认大小)
    - `tight_layout` : `bool`, optional
        - 是否使用 tight_layout, 默认为 True
    - `fn_finalize` : `MplFigureCallback`, optional
        - 图表的最终处理函数, 默认为 `mpl_figure_show`, 即简单地调用 `plt.show()`
    - `subplots_kwargs` : `dict`, optional
        - 其他参数, 传递给 `plt.subplots`

    Yields
    ----------
    - `int, int, plt.Axes`: `row`, `col`, `axes`
    """
    fig, axes = plt.subplots(row, col, figsize=figsize, **subplots_kwargs)

    if tight_layout:
        fig.tight_layout()

    # 确保 axes 始终是二维数组
    if row == 1 and col == 1:
        axes = np.array([[axes]])
    elif row == 1 or col == 1:
        axes = axes.reshape(row, col)

    for i in range(row):
        for j in range(col):
            yield i, j, axes[i, j]

    if fn_finalize:
        fn_finalize(fig)
