import numpy as np
import torch
from torch import fft
from torch.nn import functional as F

from zyplib.utils.ensure import ensure_3dims


def _periodogram(X: torch.Tensor, fs, detrend, scaling):
    if X.dim() > 2:
        X = torch.squeeze(X)
    elif X.dim() == 1:
        X = X.unsqueeze(0)

    if detrend:
        X -= X.mean(-1, keepdim=True)

    N = X.size(-1)
    assert N % 2 == 0

    df = fs / N
    dt = df
    f = torch.arange(0, N / 2 + 1) * df  # [0:df:f/2]

    dual_side = fft.fft(X)  # 双边谱
    half_idx = int(N / 2 + 1)
    single_side = dual_side[:, 0:half_idx]
    win = torch.abs(single_side)

    ps = win**2
    if scaling == 'density':  # 计算功率谱密度
        scale = N * fs
    elif scaling == 'spectrum':  # 计算功率谱
        scale = N**2
    elif scaling is None:  # 不做缩放
        scale = 1
    else:
        raise ValueError('Unknown scaling: %r' % scaling)
    Pxy = ps / scale

    Pxy[:, 1:-1] *= 2  # 能量2倍;直流分量不用二倍, 中心频率点不用二倍

    return f, Pxy.squeeze()


def periodogram(X: torch.Tensor, fs=256, detrend=True, scaling='density', no_grad=True):
    """计算信号单边 PSD, 基本等价于 scipy.signal.periodogram

    Parameters:
    ----------
        - `X`:          torch.Tensor, EEG, [T]/[N, T]
        - `fs`:         int, 采样率, Hz
        - `detrend`:    bool, 是否去趋势 (去除直流分量)
        - `scaling`:    { 'density', 'spectrum' }, 可选
            - 'density':    计算功率谱密度 `(V ** 2 / Hz)`
            - 'spectrum':    计算功率谱 `(V ** 2)`
        - `no_grad`:    bool, 是否启用 no_grad() 模式

    Returns:
    ----------
        - `Pxy`:    Tensor, 单边功率谱
    """
    if no_grad:
        with torch.no_grad():
            return _periodogram(X, fs, detrend, scaling)
    else:
        return _periodogram(X, fs, detrend, scaling)


def _get_window(window, nwlen, device):
    if window == 'hann':
        window = torch.hann_window(
            nwlen, dtype=torch.float32, device=device, periodic=False
        )
    elif window == 'hamming':
        window = torch.hamming_window(
            nwlen, dtype=torch.float32, device=device, periodic=False
        )
    elif window == 'blackman':
        window = torch.blackman_window(
            nwlen, dtype=torch.float32, device=device, periodic=False
        )
    elif window == 'boxcar':
        window = torch.ones(nwlen, dtype=torch.float32, device=device)
    else:
        raise ValueError('Invalid Window {}' % window)
    return window


def _pwelch(X: torch.Tensor, fs, detrend, scaling, window, nwlen, nhop):
    X = ensure_3dims(X, newaxis='channel')
    if scaling == 'density':
        scale = fs * (window * window).sum().item()
    elif scaling == 'spectrum':
        scale = window.sum().item() ** 2
    else:
        raise ValueError('Unknown scaling: %r' % scaling)
    # --------------- Fold and windowing --------------- #
    N, T = X.size(0), X.size(-1)
    X = X.view(N, 1, 1, T)
    X_fold = F.unfold(X, (1, nwlen), stride=nhop)  # [N, 1, 1, T] -> [N, nwlen, win_cnt]
    if detrend:
        X_fold -= X_fold.mean(1, keepdim=True)  # 各个窗口各自detrend
    window = window.view(1, -1, 1)  # [1, nwlen, 1]
    X_windowed = X_fold * window  # [N, nwlen, win_cnt]
    win_cnt = X_windowed.size(-1)

    # --------------- Pwelch --------------- #
    X_windowed = X_windowed.transpose(1, 2).contiguous()  # [N, win_cnt, nwlen]
    X_windowed = X_windowed.view(N * win_cnt, nwlen)  # [N * win_cnt, nwlen]
    f, pxx = _periodogram(
        X_windowed, fs, detrend=False, scaling=None
    )  # [N * win_cnt, nwlen // 2 + 1]
    pxx /= scale
    pxx = pxx.view(N, win_cnt, -1)  # [N, win_cnt, nwlen // 2 + 1]
    pxx = torch.mean(pxx, dim=1)  # [N, nwlen // 2 + 1]
    return f, pxx


def pwelch(
    X: torch.Tensor,
    fs=256,
    detrend=True,
    scaling='density',
    window='hann',
    nwlen=128,
    nhop=None,
    noverlap=None,
    no_grad=True,
):
    """Pwelch 方法，大致相当于 scipy.signal.welch

    Parameters:
    ----------
        - `X`:          torch.Tensor, EEG, [T]/[N, T]
        - `fs`:         int, 采样率, Hz
        - `detrend`:    bool, 是否去趋势 (去除直流分量)
        - `scaling`:    { 'density', 'spectrum' }, 可选
            - 'density':    计算功率谱密度 `(V ** 2 / Hz)`
            - 'spectrum':    计算功率谱 `(V ** 2)`
        - `window`:     str, 窗函数名称
        - `nwlen`:      int, 窗函数长度 (点的个数)
        - `nhop`:       int, 窗函数移动步长, 即 nwlen - noverlap (点的个数)
                        如果为 None 且 noverlap 为 None，则默认为 `nwlen // 2`
        - `noverlap`:   int, 仅当 nhop 为 None 时有效
        - `no_grad`:    bool, 是否启用 no_grad() 模式

    Returns:
    ----------
        - `f'`:    Tensor, 频率
        - `Pxy`:    Tensor, 单边功率谱
    """
    if nhop is None:
        if noverlap is not None:
            nhop = nwlen - noverlap
        else:
            nhop = nwlen // 2
    window = _get_window(window, nwlen, X.device)
    if no_grad:
        with torch.no_grad():
            return _pwelch(X, fs, detrend, scaling, window, nwlen, nhop)
    else:
        return _pwelch(X, fs, detrend, scaling, window, nwlen, nhop)


def _stft(X: torch.Tensor, fs, window, nhop, nfft):
    nfft = window.size(-1)
    # [batch, freq_points, time_points]
    stft_ans = torch.stft(
        X, n_fft=nfft, window=window, hop_length=nhop, return_complex=True
    )
    pxx = torch.abs(stft_ans) ** 2
    f = torch.arange(0, stft_ans.size(-2))
    ts = nhop / fs
    t = torch.arange(0, stft_ans.size(-1)) * ts
    return t, f, pxx


def stft(
    X: torch.Tensor, fs, window='hann', nwlen=256, nhop=None, nfft=512, no_grad=True
):
    """Short Time Fourier Transform

    Parameters:
    ----------
        - `X`:          torch.Tensor, EEG, [T]/[N, T]
        - `fs`:         int, 采样率, Hz
        - `window`:     str, 窗函数名称
        - `nhop`:       int, 窗函数移动步长, 即 nwlen - noverlap (点的个数)
                        如果为 None 且 noverlap 为 None，则默认为 `nwlen // 2`
        - `nfft`:       int, FFT 长度
        - `no_grad`:    bool, 是否启用 no_grad() 模式

    Returns:
    ----------
        - `pxx`: Tensor, 功率谱
    """
    if nhop is None:
        nhop = nwlen // 4
    if nfft < nwlen:
        nfft = nwlen
    window = _get_window(window, nwlen, X.device)
    if no_grad:
        with torch.no_grad():
            return _stft(X, fs, window, nhop, nfft)
    else:
        return _stft(X, fs, window, nhop, nfft)


def sinc(x: torch.Tensor):
    return torch.where(
        x == 0, torch.tensor(1.0, device=x.device, dtype=x.dtype), torch.sin(x) / (x)
    )


def gate_signal(cutoff, half_size=256):
    window = torch.hann_window(2 * half_size, periodic=False)
    time = torch.arange(-half_size, half_size)
    gate = 2 * cutoff * window * sinc(2 * cutoff * np.pi * time)
    gate /= gate.sum()
    return gate
