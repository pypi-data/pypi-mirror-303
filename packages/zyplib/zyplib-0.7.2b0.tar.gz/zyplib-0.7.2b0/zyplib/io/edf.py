import math
from collections import OrderedDict
from datetime import datetime
from typing import List, TypedDict

import numpy as np


class EDFHeader(TypedDict):
    version: str
    patient_id: str
    recording_id: str
    start_date: str
    start_time: str
    header_bytes: int
    reserved: str
    n_records: int
    duration: float
    n_signals: int
    label: List[str]
    transducer_type: List[str]
    physical_dimension: List[str]
    physical_min: List[float]
    physical_max: List[float]
    digital_min: List[int]
    digital_max: List[int]
    prefiltering: List[str]
    samples_per_record: List[int]
    ns_reserved: List[str]


class EDF:
    def __init__(self, edf_file_path: str, convert_header=True) -> None:
        self.edf_file_path = edf_file_path
        self._is_edf_plus = False
        self.header = {}
        self._read_edf_header(convert_header)
        self._check_edf_plus()
        self._label_and_srate(self.header)

    def _read_edf_header(self, convert=True):
        with open(self.edf_file_path, 'r+', encoding='iso-8859-1') as f:
            header = OrderedDict(())

            item_names = [
                'version',
                'patient_id',
                'recording_id',
                'start_date',
                'start_time',
                'header_bytes',
                'reserved',
                'n_records',
                'duration',
                'n_signals',
            ]
            item_bytes = [8, 80, 80, 8, 8, 8, 44, 8, 8, 4]
            for name, bytes in zip(item_names, item_bytes):
                header[name] = f.read(bytes)
            ns = int(header['n_signals'])
            item_names = [
                'label',
                'transducer_type',
                'physical_dimension',
                'physical_min',
                'physical_max',
                'digital_min',
                'digital_max',
                'prefiltering',
                'samples_per_record',
                'ns_reserved',
            ]
            item_bytes = [16, 80, 8, 8, 8, 8, 8, 80, 8, 32]
            for name, bytes in zip(item_names, item_bytes):
                header[name] = [f.read(bytes) for _ in range(ns)]

        def convert_type(name):
            if name == 'header_bytes':
                header[name] = int(header[name])
            elif name == 'n_signals':
                header[name] = int(header[name])
            elif name == 'n_records':
                header[name] = int(header[name])
            elif name == 'duration':
                header[name] = float(header[name])
            elif name == 'samples_per_record':
                header[name] = [int(x) for x in header[name]]
            elif name == 'physical_min':
                header[name] = [float(x) for x in header[name]]
            elif name == 'physical_max':
                header[name] = [float(x) for x in header[name]]
            elif name == 'digital_min':
                header[name] = [int(x) for x in header[name]]
            elif name == 'digital_max':
                header[name] = [int(x) for x in header[name]]

        if convert:
            for name, value in header.items():
                if isinstance(value, list):
                    header[name] = [x.strip() for x in value]
                else:
                    header[name] = value.strip()
                convert_type(name)
        self.header = header
        return header

    def _check_edf_plus(self):
        """检查 EDF+ 格式

        - 处理 subsecond
        """
        self.header['subsecond'] = 0
        header = self.header
        if header['label'][-1] == 'EDF Annotations':
            self._is_edf_plus = True
            record_samples = sum(header['samples_per_record'][:-1])
            record_bytes = record_samples * 2
            header_bytes = header['header_bytes']
            with open(self.edf_file_path, 'rb') as f:
                f.seek(header_bytes + record_bytes)  # move to first byte of annotations
                TAL = f.read(header['samples_per_record'][-1] * 2)  # read all annotations
                # print(TAL)
            subsecond_byte = TAL.split(b'\x14\x14')[0]
            subsecond = subsecond_byte.decode('ascii')[
                1:
            ]  # convert to string, and ommit the first character '+'
            # print(offset)
            self.header['subsecond'] = float(subsecond)

    @property
    def start_datetime(self):
        """获取 EDF 文件的开始时间

        Returns
        ----------
            - `datetime.datetime` : 开始时间
        """
        header = self.header
        start_date = header['start_date']
        start_time = header['start_time']
        subsecond = header['subsecond']  # float in seconds
        start_datetime = datetime.strptime(
            f'{start_date} {start_time}', '%d.%m.%y %H.%M.%S'
        )
        # add subsecond to start_datetime
        start_datetime = start_datetime.replace(microsecond=int(subsecond * 1e6))
        return start_datetime

    def _label_and_srate(self, header):
        """获取 Header 中的标签和采样率
        
            自动去除 Annotation 标签，并计算采样率
        
            Parameters
            ----------
                - `header` : dict\\
                    `read_edf_header` 返回的字典
                    
            Returns
            ----------
                - `labels` : ndarray; 标签列表
                - `srate` : ndarray; 采样率s
        """
        self.data_signal_idx = [
            i
            for i in range(len(header['label']))
            if header['label'][i] != 'EDF Annotations'
        ]
        self.label = np.array(header['label'])[self.data_signal_idx]
        self.srate = (
            np.array(header['samples_per_record'])[self.data_signal_idx]
            / header['duration']
        )

    def read_signal(self, start_record=0, end_record=None, channels=None):
        """读取 EDF 文件的信号数据

        Args:
        ----------
            - start_record (int, optional): 从第几个记录开始读取. Defaults to 0.
            - end_record (int, optional): 读取到第几个记录结束. Defaults to None.
            - channels (list, optional): 读取哪些通道. Defaults to None.

        Returns:
        ----------
            - signals: list of np.ndarray, 信号数据
        """
        offset = self.header['header_bytes']
        num_signals = self.header['n_signals']  # C
        num_records = self.header['n_records']  # T
        samples_per_record: list = self.header['samples_per_record']  # N/T

        bytes_per_record = sum(samples_per_record) * 2

        end_record = num_records if end_record is None else end_record
        num_records = end_record - start_record

        # 确定读取的通道
        if channels:
            if 'EDF Annotations' in channels:
                raise ValueError('"EDF Annotations" channel is not supported.')
            data_signal_idx = [self.header['label'].index(x) for x in channels]
        else:
            data_signal_idx = self.data_signal_idx
        # 输入的通道信息的顺序
        signal_idx_order = {x: i for i, x in enumerate(data_signal_idx)}

        signals = [
            np.zeros(samples_per_record[i] * num_records, dtype=np.int16)
            for i in data_signal_idx
        ]

        per_byte = 2
        with open(self.edf_file_path, 'rb+') as f:
            f.seek(offset)
            f.seek(start_record * bytes_per_record, 1)
            for r in range(num_records):
                for s in range(num_signals):
                    spr = samples_per_record[s]
                    if s in data_signal_idx:
                        data_bytes = f.read(spr * per_byte)
                        signal = np.frombuffer(data_bytes, dtype=np.int16)
                        i = signal_idx_order[s]
                        signals[i][r * spr : (r + 1) * spr] = signal
                    else:
                        f.seek(spr * per_byte, 1)

        pmin = np.array(self.header['physical_min'])[data_signal_idx]
        pmax = np.array(self.header['physical_max'])[data_signal_idx]
        dmin = np.array(self.header['digital_min'])[data_signal_idx]
        dmax = np.array(self.header['digital_max'])[data_signal_idx]
        for i in range(len(signals)):
            scale = (pmax[i] - pmin[i]) / (dmax[i] - dmin[i])
            dc = pmax[i] - scale * dmax[i]
            signals[i] = signals[i] * scale + dc

        return signals

    def read_range_signal(self, start_t=0, end_t=None, channels=None):
        if start_t == 0 and end_t is None:
            return self.read_signal(channels=channels)

        duration = self.header['duration']
        samples_per_record = self.header['samples_per_record']
        start_record = int(start_t // duration)
        start_record_offset = start_t % duration
        if math.isclose(end_t % duration, 0):
            # 如果整除的话，ceil 会导致少读取一段，所以需要额外的处理
            end_record = int(end_t // duration) + 1
        else:
            end_record = math.ceil(end_t / duration)
        end_record_offset = duration - end_t % duration
        sr_channels = [
            samples_per_record[self.header['label'].index(x)] for x in channels
        ]

        signals = self.read_signal(start_record, end_record, channels)

        for i in range(len(signals)):
            signal = signals[i]
            sr = sr_channels[i]
            sig_len = len(signal)
            start = int(start_record_offset * sr)
            end = sig_len - int(end_record_offset * sr)
            signals[i] = signal[start:end]
        return signals

    def read_annotation(self):
        """读取 EDF 文件的注释

        Returns:
        ----------
            - annotations: list of dict, 注释数据
        """
        ...


def read_edf_header(fpath: str, convert_header=True):
    """读取 EDF 文件的 Header 信息


    Parameters
    ----------
        - `fpath` : str
            - EDF 文件路径
        - `convert_header` : bool, optional
            - 是否转换 Header 中的数据类型

    Returns
    ----------
        - `OrderedDict` : dict
            - header 对象
    """
    edf = EDF(fpath, convert_header)
    return edf.header
