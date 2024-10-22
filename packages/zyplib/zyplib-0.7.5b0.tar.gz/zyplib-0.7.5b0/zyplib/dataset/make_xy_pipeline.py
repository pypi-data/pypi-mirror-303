"""
本模块主要提供了一些数据集导入的 pipeline 相关的函数，是对脑电信号数据导入、预处理流程的高级封装

所有函数均满足:

- 输入: 一些参数，以及一些回调函数
- 输出: 返回数据集 (X, y)

"""

from functools import reduce
from typing import Callable, Protocol, Sequence, runtime_checkable

import numpy as np
from sklearn.model_selection import KFold

from zyplib.dataset.labels import to_onehot
from zyplib.dataset.split import random_split

__all__ = ['basic_pipeline']


@runtime_checkable
class FuncPipeline(Protocol):
    """函数类型，输入文件路径列表，输出数据集 (X, y)"""

    def __call__(self, files: list[str]) -> tuple[np.ndarray, np.ndarray]: ...


@runtime_checkable
class ReadFunction(Protocol):
    def __call__(self, file_path: str) -> np.ndarray: ...


@runtime_checkable
class SegmentFunction(Protocol):
    def __call__(self, signal: np.ndarray) -> np.ndarray: ...


@runtime_checkable
class LabelFunction(Protocol):
    def __call__(self, file_path: str) -> int: ...


@runtime_checkable
class SignalProcessFunction(Protocol):
    def __call__(self, signal: np.ndarray) -> np.ndarray: ...


@runtime_checkable
class EncodeLabelFunction(Protocol):
    def __call__(self, label: list | np.ndarray) -> np.ndarray: ...


def basic_pipeline(
    files: list[str],
    fn_read: ReadFunction,
    fn_segment: SegmentFunction,
    label: LabelFunction,
    fn_before_segment: SignalProcessFunction = None,
    fn_after_segment: SignalProcessFunction = None,
    fn_encode_label: EncodeLabelFunction = lambda y: to_onehot(y, squeeze_2_class=True),
) -> tuple[np.ndarray, np.ndarray]:
    """从文件中读取数据，并自动切片、制作用于训练的数据集

    本 Pipeline 适用于:
    - 从文件中读取完整的脑电
    - 需要对完整脑电进行切分
    - 无特殊标签，只需根据文件进行标记即可
    - 输出: 数据集 (X, y)
        - X: 数据，shape = (N, C, T)
        - y: 标签，shape = (N,)

    Pipeline 流程:
    ----------

    1. 从文件中读取完整的数据 X
    2. 对数据 X 进行预处理
    3. 对数据 X 进行切片
    4. 对数据 X 进行后处理
    5. 制作标签 y
    6. 返回数据集 (X, y)

    Parameters
    ----------
    - `files` : `list[str]`
        - 文件路径列表
    - `fn_read` : `(file_path: str) -> np.ndarray`
        - 文件读取函数
    - `fn_segment` : `(signal: np.ndarray) -> np.ndarray`
        - 数据切片函数
        - 输入一个 `[C, T]` 的信号
        - 输出一个 `[N, C, T]` 的信号
    - `label` : `int | (file_path: str) -> int`
        - 标签，如果为 int，则所有数据标签相同；如果为函数，则根据文件名生成标签
    - `fn_before_segment` : `(signal: [C, T]) -> [C, T]`, optional
        - 数据切片前的处理函数
    - `fn_after_segment` : `(signal: [N, C, T]) -> [N, C, T]`, optional
        - 数据切片后的处理函数
    - `fn_encode_label` : `(label: list | np.ndarray) -> np.ndarray`, optional
        - 标签编码函数, 默认使用 `to_onehot`

    Returns
    ----------
    - `X` : `np.ndarray`, shape = (N, C, T)
        - 数据
    - `y` : `np.ndarray`, shape = (N, n_classes)
        - 标签
    """
    if not files:
        raise ValueError('The files list is empty. Please provide at least one file.')

    fn_before_segment = fn_before_segment or (lambda x: x)
    fn_after_segment = fn_after_segment or (lambda x: x)
    label = label if callable(label) else (lambda _: label)

    # 处理单个文件
    def load_single_file(fpath: str):
        signal = fn_read(fpath)  # 读取数据
        signal = fn_before_segment(signal)  # 数据预处理
        segments = fn_segment(signal)  # 数据切片
        segments = fn_after_segment(segments)
        N = len(segments)
        label_ = label(fpath)  # 制作标签
        return segments, [label_] * N

    # 批量处理所有文件
    results = map(load_single_file, files)

    # 合并数据
    def merge_data(Xy: tuple[list[np.ndarray], list[int]], pair: tuple[np.ndarray, int]):
        Xy[0].append(pair[0])
        Xy[1].extend(pair[1])
        return Xy

    Xy = reduce(merge_data, results, ([], []))

    X = np.concatenate(Xy[0], axis=0)
    y = np.array(Xy[1], dtype=int)

    fn_encode_label = fn_encode_label or (lambda y: to_onehot(y, squeeze_2_class=True))

    y = fn_encode_label(y)

    return X, y


def train_test_pipeline(
    train_size: float | int,
    all_files: list[str] | Sequence[list[str]],
    random_seed: int | None = None,
    return_split_files: bool = False,
    *,
    fn_pipeline: FuncPipeline | None = None,
    **basic_pipeline_kwargs,
):
    """在导入文件的时候，自动将不同文件划分为训练集和测试集

    - 需要一个 `fn_pipeline: (list[str]) -> (np.ndarray, np.ndarray)` 的回调函数
        - 输入: 文件路径列表
        - 输出: 数据集 (X, y)
    - 当 `fn_pipeline` 为 `None` 时，使用 `basic_pipeline`, 并且使用后面参数作为 `basic_pipeline` 的参数

    #### 使用自定义的 fn_pipeline

    ```py
    def load_xy(files: list[str]) -> tuple[np.ndarray, np.ndarray]:
        ...

    X_train, X_test, y_train, y_test = train_test_pipeline(
        0.8, all_files, fn_pipeline=load_xy
    )
    ```

    #### 默认使用 basic_pipeline
    ```py
    train_test_pipeline(
        0.8, all_files, fn_read=fn_read, fn_segment=fn_segment, label=label, ...
    )

    # 等价于
    train_test_pipeline(
        0.8, all_files, fn_pipeline=lambda files: basic_pipeline(files, ...)
    )
    ```

    Parameters
    ----------
    - `train_size` : `float | int`
        - 训练集大小
    - `all_files` : `list[str] | Sequence[list[str]]`
        - 所有文件路径列表
        - 如果为 `list[str]`，会直接将 `all_files` 划分为训练集和测试集
        - 如果为 `Sequence[list[str]]`，则视为不同分组的文件列表; 会各自单独划分为训练集和测试集最后再合并在一起
    - `random_seed` : `int | None`, optional
        - 随机种子; 当 `random_seed` 为 `None` 时，不设置随机种子
    - `return_split_files` : `bool`, optional
        - 是否返回训练集和测试集的文件路径列表; 当 `return_split_files` 为 `True` 时，返回训练集和测试集的文件路径列表
    - `fn_pipeline` : `FuncPipeline`, optional
        - 数据处理 pipeline; 当 `fn_pipeline` 为 `None` 时，使用 `basic_pipeline`, 并使用后面的参数作为 pipeline 的参数
    - `basic_pipeline_kwargs` `basic_pipeline` 相同, 包括:
        - `['fn_read', 'fn_segment', 'label', 'fn_before_segment', 'fn_after_segment']`

    Returns
    ----------
    - `X_train` : `np.ndarray`, shape = (N_train, C, T)
        - 训练数据
    - `X_test` : `np.ndarray`, shape = (N_test, C, T)
        - 测试数据
    - `y_train` : `np.ndarray`, shape = (N_train, n_classes)
        - 训练标签
    - `y_test` : `np.ndarray`, shape = (N_test, n_classes)
        - 测试标签
    - `train_files` : `list[str]`, optional
        - 训练集文件路径列表; 当 `return_split_files` 为 `True` 时返回
    - `test_files` : `list[str]`, optional
        - 测试集文件路径列表; 当 `return_split_files` 为 `True` 时返回
    """
    if isinstance(all_files[0], str):
        all_files = [all_files]  # Convert to a single group if it's a flat list

    train_files, test_files = [], []
    for group in all_files:
        N = len(group)
        if isinstance(train_size, int):
            group_train_size = min(train_size, N - 1)  # Ensure at least one test sample
        else:
            group_train_size = int(N * train_size)

        group_test_size = N - group_train_size

        group_train, group_test = random_split(
            group, (group_train_size, group_test_size), seed=random_seed
        )
        train_files.extend(group_train)
        test_files.extend(group_test)

    if fn_pipeline is None:
        fn_pipeline = lambda files: basic_pipeline(files, **basic_pipeline_kwargs)

    X_train, y_train = fn_pipeline(train_files)
    X_test, y_test = fn_pipeline(test_files)

    if return_split_files:
        return X_train, X_test, y_train, y_test, train_files, test_files
    else:
        return X_train, X_test, y_train, y_test


def kfold_pipeline(
    k: int,
    all_files: list[str],
    random_seed: int | None = None,
    yield_split_files: bool = False,
    *,
    fn_pipeline: FuncPipeline | None = None,
    **basic_pipeline_kwargs,
):
    """在导入文件的时候，自动将不同文件划分为 k 折, 通过 `yield` 返回每次的 XY 数据

    - 需要一个 `fn_pipeline: (list[str]) -> (np.ndarray, np.ndarray)` 的回调函数
        - 输入: 文件路径列表
        - 输出: 数据集 (X, y)
    - 当 `fn_pipeline` 为 `None` 时，使用 `basic_pipeline`, 并且使用后面参数作为 `basic_pipeline` 的参数

    Parameters
    ----------
    - `k` : `int`
        - 折数
    - `all_files` : `list[str]`
        - 所有文件路径列表
    - `random_seed` : `int | None`, optional
        - 随机种子; 当 `random_seed` 为 `None` 时，不设置随机种子
    - `yield_split_files` : `bool`, optional
        - 是否返回训练集和验证集的文件路径列表; 当 `yield_split_files` 为 `True` 时，返回训练集和验证集的文件路径列表
    - `fn_pipeline` : `FuncPipeline`, optional
        - 数据处理 pipeline; 当 `fn_pipeline` 为 `None` 时，使用 `basic_pipeline`, 并使用后面的参数作为 pipeline 的参数
    - `basic_pipeline_kwargs` `basic_pipeline` 相同, 包括:
        - `['fn_read', 'fn_segment', 'label', 'fn_before_segment', 'fn_after_segment']`

    Yields
    ----------
    - `X_train` : `np.ndarray`, shape = (N_train, C, T)
        - 训练数据
    - `X_val` : `np.ndarray`, shape = (N_val, C, T)
        - 验证数据
    - `y_train` : `np.ndarray`, shape = (N_train, n_classes)
        - 训练标签
    - `y_val` : `np.ndarray`, shape = (N_val, n_classes)
        - 验证标签
    - `train_files` : `list[str]`, optional
        - 训练集文件路径列表; 当 `yield_split_files` 为 `True` 时返回
    - `val_files` : `list[str]`, optional
        - 验证集文件路径列表; 当 `yield_split_files` 为 `True` 时返回
    """
    kf = KFold(n_splits=k, shuffle=True, random_state=random_seed)

    if fn_pipeline is None:
        fn_pipeline = lambda files: basic_pipeline(files, **basic_pipeline_kwargs)

    for train_idx, val_idx in kf.split(all_files):
        train_files = [all_files[i] for i in train_idx]
        val_files = [all_files[i] for i in val_idx]

        X_train, y_train = fn_pipeline(train_files)
        X_val, y_val = fn_pipeline(val_files)

        if yield_split_files:
            yield X_train, X_val, y_train, y_val, train_files, val_files
        else:
            yield X_train, X_val, y_train, y_val
