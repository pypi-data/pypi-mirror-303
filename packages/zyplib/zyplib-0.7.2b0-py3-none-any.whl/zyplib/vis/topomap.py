import matplotlib.pyplot as plt
import mne
import numpy as np

from zyplib.signal.psd import welch


def topmap(
    data: list[float] | np.ndarray,
    channels: list[str],
    srate: float,
    montage_type='standard_1020',
    show=False,
    save_path=None,
    args_tompomap: dict = None,
):
    """绘制头皮数据的拓扑图。

    Parameters
    ----------
    - `data` : list[float] | np.ndarray
        - 拓扑图上绘制的数据。这应该是一个一维的值数组，每个通道一个值
    - `channels` : list[str]
        - 与数据对应的通道名称列表；长度和 data 长度相同
    - `srate` : float
        - 数据的采样率，单位为 Hz
    - `montage_type` : str, optional
        - 要使用的脑电图 Montage 类型，传入；默认为 'standard_1020'
        - 见 `mne.channels.get_builtin_montages`
    - `show` : bool, optional
        - 是否显示绘图。默认为 False。
    - `save_path` : str, optional
        - 保存绘图的路径。如果为 None，则不保存绘图。默认为 None。
    - `args_tompomap` : dict, optional
        - 要传递给 `mne.viz.plot_topomap` 的其他关键字参数。默认为空。
    """
    info = mne.create_info(ch_names=channels, sfreq=srate, ch_types='eeg')
    montage = mne.channels.make_standard_montage(montage_type)
    info.set_montage(montage)

    mne.viz.plot_topomap(data, info, show=show, cmap='viridis', **args_tompomap)

    if save_path:
        plt.savefig(save_path, format='png', transparent=True)


def pxx_topomap(
    signals: np.ndarray,
    channels: list[str],
    srate: float,
    montage_type='standard_1020',
    show=False,
    save_path=None,
    nperseg=None,
    args_tompomap: dict = None,
):
    """绘制脑电数据功率谱的拓扑图

    提取 signals 的功率谱，并绘制拓扑图

    Parameters
    ----------
    - `signals` : `np.ndarray`
        - 二维脑电信号 `[C, T]`
    - `channels` : list[str]
        - 与数据对应的通道名称列表；长度和 data 长度相同
    - `srate` : float
        - 数据的采样率，单位为 Hz
    - `montage_type` : str, optional
        - 要使用的脑电图 Montage 类型，传入；默认为 'standard_1020'
        - 见 `mne.channels.get_builtin_montages`
    - `show` : bool, optional
        - 是否显示绘图。默认为 False。
    - `save_path` : str, optional
        - 保存绘图的路径。如果为 None，则不保存绘图。默认为 None。
    - `nperseg` : int, optional
        - Welch 窗长。如果不填写默认为 2 * srate，即 2s
    - `args_tompomap` : dict, optional
        - 要传递给 `mne.viz.plot_topomap` 的其他关键字参数。默认为空。
    """
    nperseg = nperseg or 4 * srate
    _, pxx = welch(signals, srate, nperseg=2 * srate)

    # 计算每个通道的平均功率谱
    psds_mean = np.mean(pxx, axis=1)

    topmap(
        psds_mean,
        channels,
        srate,
        montage_type=montage_type,
        show=show,
        save_path=save_path,
        args_tompomap=args_tompomap,
    )
