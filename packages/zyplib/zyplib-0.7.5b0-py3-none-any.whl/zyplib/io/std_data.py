from typing import Any, Dict, List, Literal, Optional, Tuple, Union
from dataclasses import dataclass, field
import re

import h5py
import mne
import numpy as np

from .misc import match_channels_regex
from zyplib.annotation.event import Event, events_to_dict


@dataclass
class StandardData:
    Data: List[np.ndarray] = field(default_factory=list)
    Channels: List[str] = field(default_factory=list)
    TimeLength: float = -1
    Srate: List[float] = field(default_factory=list)
    Events: List[Event] = field(default_factory=list)
    Description: str = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_std_type = False

    def _as_std_type_(self):
        """按照标准格式来存储

        1. Channels: list，存储通道信息
        2. Data: list or ndarry，存储数据
            - 按照 float32 格式存储
            - 采样率最大不超过 256Hz
        3. Events：事件标签信息
        4. Srate: list, 各个通道的采样率
        5. Class：文件类型，数据or标签
        """
        if self._is_std_type:
            return

        if isinstance(self.Channels, np.ndarray):
            self.Channels = self.Channels.tolist()

        # 保证 Srate 是一个 list of int
        if isinstance(self.Srate, np.ndarray):
            self.Srate = self.Srate.squeeze().astype(int).tolist()
        if isinstance(self.Srate, (int, float)):
            self.Srate = [int(self.Srate)] * len(self.Channels)

        # 如果 Data 为 ndarray, 且为 float64, 则变为 float32
        if isinstance(self.Data, np.ndarray):
            self.Data = self.Data.astype(np.float32)
        elif isinstance(self.Data, list) and isinstance(self.Data[0], np.ndarray):
            for i in range(len(self.Channels)):
                data = self.Data[i].astype(np.float32)
                self.Data[i] = data

        if self.Data is not None:
            self.TimeLength = len(self.Data[0]) / self.Srate[0]

        self._is_std_type = True

    def dump_h5(self, path):
        self._as_std_type_()
        with h5py.File(path, 'w') as f:
            # 保存元数据字段到Group
            group = f.create_group('meta')
            group.attrs['Channels'] = self.Channels if self.Channels is not None else []
            group.attrs['Srate'] = self.Srate if self.Srate is not None else []
            group.attrs['TimeLength'] = self.TimeLength
            group.attrs['Description'] = self.Description

            # 保存data字段到Dataset
            data_group = f.create_group('Data')
            if self.Data is not None:
                for i, ndarr in enumerate(self.Data):
                    data_group.create_dataset(str(i), data=ndarr)

            events_group = f.create_group('Events')
            if not self.Events:
                dic = events_to_dict(self.Events)
                events_group.create_dataset('Onset', data=dic['Onset'])
                events_group.create_dataset('Duration', data=dic['Duration'])
                events_group.create_dataset('Name', data=dic['Name'])

    @staticmethod
    def load_h5(
        path, meta_only=False, match_channels: List[Union[str, re.Pattern]] = None
    ) -> 'StandardData':
        """读取 std-h5 文件

            Parameters
            ----------
                - `path` : str\\
                    h5 文件的路径
                - `meta_only` : bool, optional\\
                    是否只读取元数据
                - `match_channels` : List[Union[str, re.Pattern]], optional\\
                    正则表达式列表, 见 match_channels_regex

            Returns
            ----------
                - `StandardData`\\
                    _description_
        """
        with h5py.File(path, 'r') as f:
            # 读取元数据字段
            meta = f['meta']
            std_data = StandardData()
            std_data.Channels: List = meta.attrs['Channels'].tolist()
            std_data.Srate = meta.attrs['Srate'].tolist()
            std_data.TimeLength = meta.attrs['TimeLength']
            std_data.Description = meta.attrs['Description']

            events_group = f['Events']
            if len(events_group.keys()) > 0:
                dic = {}
                dic['onset'] = events_group['Onset'][()]
                dic['duration'] = events_group['Duration'][()]
                dic['name'] = events_group['Name'][()]
                std_data.Events.append(Event(**dic))

            if match_channels is not None:
                matched_ch_names, matched_ch_index = match_channels_regex(
                    std_data.Channels, match_channels
                )
                std_data.Channels = matched_ch_names
                std_data.Srate = [std_data.Srate[i] for i in matched_ch_index]
                include_idx = matched_ch_index
            else:
                include_idx = [i for i in range(len(std_data.Channels))]

            # 读取data字段
            if not meta_only:
                data_group = f['Data']
                std_data.Data = []
                for i in include_idx:
                    std_data.Data.append(data_group[str(i)][()])

        return std_data

    @property
    def data_array(self) -> np.ndarray:
        """将 Data 转换为 numpy.ndarray"""
        return np.array(self.Data)

    @property
    def is_srate_indentical(self) -> bool:
        """所有通道的采样率是否一致"""
        return len(self.Srate) == 0 or len(set(self.Srate)) == 1

    def to_mne_raw(self):
        """转换为 mne.io.Raw 对象"""
        channels, data, srate = self.Channels, self.Data, self.Srate

        if not self.is_srate_indentical:
            raise ValueError('All channels must have same srate')

        sr = srate[0] if len(srate) > 0 else 1
        info = mne.create_info(channels, sr, ch_types='eeg', verbose=False)
        raw = mne.io.RawArray(data, info)
        if len(self.Events) > 0:
            events_dict = events_to_dict(self.Events)
            raw.set_annotations(
                mne.Annotations(
                    onset=events_dict['Onset'],
                    duration=events_dict['Duration'],
                    description=events_dict['Name'],
                )
            )
        return raw
