from collections import Counter
from typing import Optional, Sequence, TypedDict, Union

import numpy as np
import torch
from sklearn.model_selection import KFold
from torch.utils.data import DataLoader, Dataset, Subset
from torch.utils.data import random_split as torch_random_split

from zyplib.utils.ensure import ensure_tensor


class BasicXyDataset(Dataset):
    def __init__(
        self,
        data: Union[np.ndarray, torch.Tensor],
        labels: Union[np.ndarray, torch.Tensor],
    ):
        self.data = ensure_tensor(data, dtype=torch.float32)
        self.labels = ensure_tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]


def make_basic_dataloader(
    xy_train: tuple[np.ndarray, np.ndarray],
    xy_test: Optional[tuple[np.ndarray, np.ndarray]] = None,
    split_val_from_train: Sequence[Union[int, float]] = None,
    batch_size: int = 64,
    shuffle: bool = True,
    num_workers: int = 0,
    pin_memory: bool = False,
    **kwargs,
):
    """从训练和测试数据创建 DataLoader(s)。

    参数
    ----------
    - `xy_train` : `tuple[np.ndarray, np.ndarray]`
        - 包含训练数据和标签的元组。
    - `xy_test` : `tuple[np.ndarray, np.ndarray]`, 可选
        - 包含测试数据和标签的元组，默认为 None。
    - `split_val_from_train` : `tuple[float, float] | tuple[int, int]`, 可选
        - 指定如何将训练数据拆分为训练集和验证集，默认为 None。
        - 如果为 None，则不进行拆分。
    - `batch_size` : `int`, 可选
        - 每个批次的样本数量，默认为 64。
    - `shuffle` : `bool`, 可选
        - 是否在每个 epoch 时打乱数据，默认为 True。
        - 只对训练数据有效；val/test 数据集不进行打乱。
    - `num_workers` : `int`, 可选
        - 用于数据加载的子进程数量，默认为 0。
    - `pin_memory` : `bool`, 可选
        - 如果为 True，数据加载器将把张量复制到 CUDA 固定内存中，默认为 False。
    - `**kwargs` : `dict`, 可选
        - DataLoader 的其他参数，默认为 None。

    返回
    ----------
    - `tuple[DataLoader]`
        - 训练、验证和测试数据集的 DataLoader 元组。
    """
    train_dataset = BasicXyDataset(*xy_train)

    if xy_test is not None:
        test_dataset = BasicXyDataset(*xy_test)
    else:
        test_dataset = None

    # 划分验证集
    if split_val_from_train:
        train_dataset, val_dataset = torch_random_split(
            train_dataset, split_val_from_train
        )
    else:
        val_dataset = None

    def make_dataloader(dataset: Dataset, shuffle: bool):
        if dataset is None:
            return None
        return DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,
            pin_memory=pin_memory,
            **kwargs,
        )

    train_loader = make_dataloader(train_dataset, shuffle=shuffle)
    val_loader = make_dataloader(val_dataset, shuffle=False)
    test_loader = make_dataloader(test_dataset, shuffle=False)

    return tuple(filter(lambda x: x is not None, [train_loader, val_loader, test_loader]))


# alias
make_dataloader_from_xy = make_basic_dataloader


def make_kfold_dataloader(
    *,
    xy: tuple[np.ndarray, np.ndarray] | None = None,
    dataset: Dataset | None = None,
    k: int = 5,
    random_seed: int | None = None,
    batch_size: int = 64,
    num_workers: int = 0,
    pin_memory: bool = False,
    **kwargs,
):
    """根据输入的 xy 或者 dataset 创建 KFold 的 DataLoader(s)。

    > 注意，这里是导入 XY 之后再进行 KFold；一般而言，应该是导入文件的时候就直接进行划分，推荐使用 `make_xy_pipeline` 的 `kfold_pipeline` 函数

    从输入的数据中创建 KFold 的 DataLoader(s)。

    xy 和 dataset 二选一。

    Parameters
    ----------
    - `xy` : `tuple[np.ndarray, np.ndarray]`
        - 包含数据和标签的元组。
    - `dataset` : `Dataset`, 可选
        - 数据集。
    - `k` : `int`, 可选
        - 折数，默认为 5。
    - `random_seed` : `int | None`, 可选
        - 随机种子，默认为 None。
    - `batch_size` : `int`, 可选
        - 每个批次的样本数量，默认为 64。
    - `num_workers` : `int`, 可选
        - 用于数据加载的子进程数量，默认为 0。
    - `pin_memory` : `bool`, 可选
        - 如果为 True，数据加载器将把张量复制到 CUDA 固定内存中，默认为 False。
    - `**kwargs` : `dict`, 可选
        - DataLoader 的其他参数，默认为 None。

    Yields
    ----------
    - `tuple[DataLoader, DataLoader]`
        - 训练和验证数据集的 DataLoader。
    """
    # xy 和 dataset 只能有一个是 None，一个不是 None
    assert (
        xy is not None or dataset is not None
    ), 'xy 和 dataset 只能有一个是 None，一个不是 None'
    if xy is not None:
        dataset = BasicXyDataset(*xy)
    else:
        dataset = dataset

    kf = KFold(n_splits=k, shuffle=True, random_state=random_seed)

    for train_idx, val_idx in kf.split(dataset):
        train_dataset = Subset(dataset, train_idx)
        val_dataset = Subset(dataset, val_idx)
        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            num_workers=num_workers,
            pin_memory=pin_memory,
            **kwargs,
        )
        val_loader = DataLoader(
            val_dataset,
            batch_size=batch_size,
            num_workers=num_workers,
            pin_memory=pin_memory,
            **kwargs,
        )
        yield train_loader, val_loader


class LabelCounter(TypedDict):
    number: int
    ratio: float


def count_dataloader_labels(loader: DataLoader) -> dict[int, LabelCounter]:
    """检查数据加载器是否平衡"""
    all_labels = []
    for _, labels in loader:
        labels = labels.numpy()
        all_labels.extend(np.squeeze(labels).tolist())

    counter = Counter(all_labels)
    total_samples = sum(counter.values())
    return {
        label: {'number': number, 'ratio': number / total_samples}
        for label, number in counter.items()
    }
