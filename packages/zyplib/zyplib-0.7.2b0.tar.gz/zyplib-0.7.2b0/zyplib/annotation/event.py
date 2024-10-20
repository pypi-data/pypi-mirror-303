from functools import singledispatch

from dataclasses import dataclass
from typing import List, Dict, Tuple, Union

import numpy as np


@dataclass
class Event:
    name: Union[str, int]
    onset: float
    duration: float


def filter_event(events: List[Event], name: Union[str, int]) -> List[Event]:
    return [event for event in events if event.name == name]


def split_event(events: List[Event]) -> Dict[str, List[Event]]:
    """根据 events 中的事件名称将 events 划分为多个事件列表"""
    events_dict: Dict[str, List[Event]] = {}
    for event in events:
        if event.name not in events_dict:
            events_dict[event.name] = []
        events_dict[event.name].append(event)
    return events_dict


def merge_events(events: list[Event], distance: float) -> list[Event]:
    """将距离小于 distance 的事件合并为一个事件

    本方法无视事件名称, 仅根据 onset 和 duration 进行合并

    Parameters
    ----------
        - `events` : list[Event]
            - _description_
        - `distance` : float
            - _description_

    Returns
    ----------
        - `list[Event]`
            - _description_
    """
    # 1. 将事件按 onset 排序
    events = sorted(events, key=lambda x: x.onset)
    # 2. 合并事件
    merged_events: List[Event] = []
    for event in events:
        if len(merged_events) == 0:
            merged_events.append(event)
        else:
            last_event = merged_events[-1]
            last_event_end = last_event.onset + last_event.duration
            if event.onset - last_event_end > distance:
                merged_events.append(event)
            else:
                last_event.duration = event.onset + event.duration - last_event.onset
    return merged_events


def events_from_array(array: Union[List[List[float]], np.ndarray], name) -> List[Event]:
    """从数组中提取事件列表

    Examples:
    ----------
    >>> events_from_array([[0, 1], [1, 2]], 'spindle')
    >>> events_from_array(np.array([[0, 1], [1, 2]]), 'spindle')

    Parameters
    ----------
        - `array` : Union[List[List[float]], np.ndarray]
            - 原始的事件列表

    Returns
    ----------
        - `List[Event]`
            - 事件对象列表
    """
    events = []
    for l in array:
        events.append(Event(name, l[0], l[1]))
    return events


def events_to_dict(events: List[Event]) -> Dict:
    dic = {
        'Onset': np.array([event.onset for event in events]),
        'Duration': np.array([event.duration for event in events]),
        'Name': np.array([event.name for event in events]),
    }
    return dic


def events_to_list(events: List[Event]) -> List[List[float]]:
    """将事件列表转换为数组

    Parameters
    ----------
        - `events` : List[Event]
            - 事件列表, Evnet 为 zyplib.annotation.type.Event 类型; 单位为秒

    Returns
    ----------
        - `list` : List[[float, float]]
            - 事件列表, [[onset, duration], ...]
    """
    return [[event.onset, event.duration] for event in events]


def events_to_npy(events: List[Event]) -> np.ndarray:
    """将事件列表转换为数组

    Parameters
    ----------
        - `events` : List[Event]
            - 事件列表, Evnet 为 zyplib.annotation.type.Event 类型; 单位为秒

    Returns
    ----------
        - `np.ndarray` : np.ndarray
            - 事件列表, [[onset, duration], ...]
    """
    return np.array(events_to_list(events))
