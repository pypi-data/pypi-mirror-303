from collections import Counter

import numpy as np

from zyplib.utils.ensure import ensure_npy
from zyplib.utils.print import print_info


def summary_labels(y: np.ndarray, just_print: bool = False) -> Counter:
    y = ensure_npy(y)
    y = y.squeeze()
    if y.ndim != 1:
        raise ValueError('y.ndim must be 1')

    counter = Counter(y)

    if not just_print:
        return counter

    print_info(counter)
