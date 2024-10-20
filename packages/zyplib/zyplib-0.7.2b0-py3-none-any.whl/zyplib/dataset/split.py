import random
from typing import Any, List, Union

import numpy as np
from torch.utils.data import DataLoader, Dataset
from torch.utils.data import random_split as torch_random_split


def random_split(
    data: Union[List[Any], np.ndarray],
    proportion: Union[List[float], List[int]],
    seed: int = None,
):
    """
    随机切分数据集; 类似 torch 的 random_split，不过返回的是切分的结果而非 Subset

    示例
    ----------
    ```py
    # first_part 占 70%，second_part 占 30%
    first_part, second_part = random_split(data, proportion=[0.7, 0.3])

    # 或根据具体数量进行划分，例如：
    first_part, second_part = random_split(data, proportion=[7, 3])
    ```

    Parameters
    ----------
    - `data` : `List[Any] | np.ndarray`
        - 需要切分的数据; 一个可以索引的对象
    - `proportion` : `List[float] | List[int]`
        - 切分的比例或每部分的数量:
          - 如果是 `float[]`，需要满足 `sum(proportion) == 1`；
          - 如果是 `int[]`，需要满足 `sum(proportion) == len(data)`。
    - `seed` : `int`, optional
        - 随机种子

    Returns
    -------
    - 切分后的多个部分: `List`
        - 按照比例或数量切分后的数据集部分。
    """

    if seed is not None:
        random.seed(seed)

    data_len = len(data)

    # 判断 proportion 是比例还是数量
    if all(isinstance(p, int) for p in proportion):
        # 如果是 int，确保数量之和等于数据长度
        if sum(proportion) != data_len:
            raise ValueError('整数形式的 proportion 的和必须等于数据总长度')
        sizes = proportion
    elif all(isinstance(p, float) for p in proportion):
        # 如果是 float，确保比例之和为 1
        if not np.isclose(sum(proportion), 1.0):
            raise ValueError('浮点数形式的 proportion 的和必须为 1')
        # 按比例计算每个部分的大小
        sizes = [int(p * data_len) for p in proportion]

        # 为了确保总大小与数据长度一致，调整最后一个部分的大小
        sizes[-1] = data_len - sum(sizes[:-1])
    else:
        raise TypeError('proportion 必须全为 float 或全为 int')

    # 随机打乱数据索引
    indices = list(range(data_len))
    random.shuffle(indices)

    # 根据 sizes 切分数据
    parts = []
    start_idx = 0
    for size in sizes:
        end_idx = start_idx + size
        part_indices = indices[start_idx:end_idx]
        part = (
            [data[i] for i in part_indices]
            if isinstance(data, list)
            else data[part_indices]
        )
        parts.append(part)
        start_idx = end_idx

    return parts


def split_dataset(
    data_set: Dataset, val_proportion: float, n_batch: int
) -> tuple[DataLoader, DataLoader]:
    """Split DataSet into TrainDataLoader and ValDataLoader"""
    n_data = len(data_set)
    n_val = int(n_data * val_proportion)
    n_train = n_data - n_val
    train_set, val_set = torch_random_split(data_set, [n_train, n_val])
    train_data_loader = DataLoader(
        train_set, batch_size=n_batch, drop_last=True, num_workers=1, pin_memory=True
    )
    val_data_loader = DataLoader(
        val_set, batch_size=n_batch, drop_last=True, num_workers=1, pin_memory=True
    )
    return train_data_loader, val_data_loader
