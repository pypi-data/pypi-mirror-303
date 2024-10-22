from typing import Protocol

import numpy as np
import pandas as pd

from zyplib.utils.ensure import ensure_3dims, ensure_npy, ensure_scalar


# @runtime_checkable
class EEGFeatureFunction(Protocol):
    """输入脑电信号 [N, C, T], 输出:

    1. 标量
    2. 向量 [N,]
    3. 矩阵 [N, C] 或 [N, K]
    4. 三维张量 [N, C, K]
    """

    def __call__(self, signal: np.ndarray) -> np.ndarray | float: ...


def make_tabular(
    signals: np.ndarray,
    fn_features: list[EEGFeatureFunction] | dict[str, EEGFeatureFunction],
    return_feat_names: bool = False,
) -> np.ndarray | tuple[np.ndarray, list[str]]:
    """将脑电信号转换为表格数据

    此函数接收脑电信号数据和一系列特征提取函数，将每个特征函数应用于输入信号，
    并将结果组合成一个表格形式的特征矩阵。

    Parameters
    ----------
    - `signals` : `np.ndarray`
        - 脑电信号, 形状为 (n_samples, n_channels, n_times)
        - 如果输入是2维数组, 将被视为 `(1, n_channels, n_times)`
    - `fn_features` : `list[EEGFeatureFunction] | dict[str, EEGFeatureFunction]`， 特征函数, 可以是以下两种形式之一
        1. 函数列表：每个函数应接受形状为 [n_samples, n_channels, n_times] 的 numpy 数组，
           并返回标量、一维数组或与输入兼容的多维数组
        2. 字典：键为特征名称，值为特征函数
    - `return_feat_names` : `bool`, optional
        - 是否返回特征名称, 默认为 False

    Returns
    ----------
    - `np.ndarray | tuple[np.ndarray, list[str]]`
        - 如果 `return_feat_names` 为 False：
            返回表格数据, 形状为 (n_samples, n_features)
        - 如果 `return_feat_names` 为 True：
            返回一个元组, 包含表格数据和特征名称列表

    Notes
    ----------
    1. 特征函数的返回值处理：
       - 标量：被广播到所有样本
       - 一维数组 `[N,]`：必须与样本数量匹配，每个元素对应一个样本的特征
       - 二维数组 `[N, K]` 或 `[N, C]`：
         * 如果第二维等于通道数，假定为每个通道的特征
         * 否则，假定为每个样本的 K 个特征
       - 三维数组 `[N, C, K]`：被解释为每个样本、每个通道的 K 个特征

    2. 特征名称生成规则：
       - 标量或一维数组：使用函数名或字典键
       - 二维数组：
         * 通道特征：`'name_ch{j}'`，j 为通道索引
         * 多特征：`'name{i}'`，i 为特征索引
       - 三维数组：`'name{i}_ch{j}'`，i 为特征索引，j 为通道索引

    Examples
    ----------
    >>> import numpy as np
    >>> from zyplib.feature.tabular import make_tabular
    >>>
    >>> # 创建示例数据
    >>> signals = np.random.rand(10, 4, 1000)  # 10 个样本，4 个通道，1000 个时间点
    >>>
    >>> # 定义一些特征函数
    >>> def mean_feature(x):
    ...     return np.mean(x, axis=-1)
    >>>
    >>> def std_feature(x):
    ...     return np.std(x, axis=-1)
    >>>
    >>> # 使用函数列表
    >>> features, names = make_tabular(signals, [mean_feature, std_feature], return_feat_names=True)
    >>> print(features.shape)  # 输出: (10, 8)
    >>> print(names)  # 输出: ['mean_feature_ch0', 'mean_feature_ch1', ..., 'std_feature_ch3']
    >>>
    >>> # 使用字典
    >>> feature_dict = {'Mean': mean_feature, 'Std': std_feature}
    >>> features, names = make_tabular(signals, feature_dict, return_feat_names=True)
    >>> print(features.shape)  # 输出: (10, 8)
    >>> print(names)  # 输出: ['Mean_ch0', 'Mean_ch1', ..., 'Std_ch3']
    """
    signals = ensure_npy(signals)
    signals = ensure_3dims(signals, newaxis='batch')

    n_batch, n_channels, n_times = signals.shape

    # 特征名称, 如果为字典，特征名称就为 key name, 否则为 function 的名称
    if isinstance(fn_features, dict):
        feature_list = list(fn_features.items())
    else:
        feature_list = [(func.__name__, func) for func in fn_features]

    # 使用 fn_features 计算特征
    features = []
    feature_names = []

    for name, func in feature_list:
        feat = func(signals)

        if isinstance(feat, tuple):
            raise ValueError(f'{func} 返回多个值, 不符合要求!')

        scalar = ensure_scalar(feat)
        if scalar is not None:
            # fn 返回标量，则直接加入特征向量中
            features.append(np.full((n_batch, 1), scalar))
            feature_names.append(name)
            continue

        feat = np.squeeze(feat)

        if feat.ndim == 1:
            # fn 返回向量 [N,]，则将向量展平后加入特征向量中
            assert feat.shape[0] == n_batch
            features.append(feat.reshape(-1, 1))
            feature_names.append(name)
        elif feat.ndim == 2:
            # fn 返回 [N, K] 或者 [N, C] 的二维数组，则将特征拼接起来
            # feature name: name{i...k}_ch{j...c}
            assert feat.shape[0] == n_batch

            if feat.shape[1] == n_channels:
                features.append(feat)
                feature_names.extend([f'{name}_ch{j}' for j in range(n_channels)])
            else:
                features.append(feat)
                feature_names.extend([f'{name}{i}' for i in range(feat.shape[1])])
        elif feat.ndim == 3:
            # fn 返回 [N, C, K] 的三维数组，则将特征拼接起来
            # feature name: name{i...k}_ch{j...c}
            assert feat.shape[0] == n_batch and feat.shape[1] == n_channels
            feat_reshaped = feat.reshape(n_batch, -1)
            features.append(feat_reshaped)
            feature_names.extend(
                [
                    f'{name}{i}_ch{j}'
                    for j in range(n_channels)
                    for i in range(feat.shape[2])
                ]
            )
        else:
            raise ValueError(f'Unsupported feature shape: {feat.shape}')

    # 最后全部堆叠起来
    features = np.hstack(features)

    # 输出 (n_batch, n_features)
    if return_feat_names:
        return features, feature_names
    else:
        return features
