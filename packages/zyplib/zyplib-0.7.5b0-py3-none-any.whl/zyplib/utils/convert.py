from typing import List, Union

import numpy as np
import mne
from .ensure import ensure_npy
from zyplib.annotation.event import Event


def to_mne_raw(data, srate: float, channels: List[str], events: List[Event] = None):
    info = mne.create_info(channels, srate, ch_types='eeg', verbose=False)
    raw = mne.io.RawArray(data, info)
    if events is not None:
        onset = np.array([event.onset for event in events])
        duration = np.array([event.duration for event in events])
        description = np.array([event.name for event in events])
        raw.set_annotations(
            mne.Annotations(onset=onset, duration=duration, description=description)
        )
    return raw
