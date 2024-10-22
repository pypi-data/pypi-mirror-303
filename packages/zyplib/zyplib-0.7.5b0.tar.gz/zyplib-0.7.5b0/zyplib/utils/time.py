import time
from datetime import datetime, timedelta, timezone
from timeit import default_timer as timer
from typing import Optional

from .print import colored


class TIME_FMT:
    YEAR = '%Y'
    YEAR_SHORT = '%y'
    MONTH = '%m'
    DAY = '%d'
    HOUR = '%H'
    MINUTE = '%M'
    SECOND = '%S'

    DATE = f'{YEAR}-{MONTH}-{DAY}'
    TIME = f'{HOUR}:{MINUTE}:{SECOND}'
    DATE_TIME = f'{DATE} {TIME}'
    DATE_TIME_CONDENSED = f'{YEAR}{MONTH}{DAY}{HOUR}{MINUTE}{SECOND}'
    DATE_TIME_UNDERSCORE = f'{YEAR}_{MONTH}_{DAY}-{HOUR}_{MINUTE}_{SECOND}'


def format_time(ts: float, fmt: str = TIME_FMT.DATE_TIME, time_zone: int = 8):
    """格式化时间为字符串

    Parameters
    ----------
    - `ts` : `float`
        - 时间戳, time.time() 的返回值
    - `fmt` : `str`, optional
        - 格式化字符串，默认为 `TIME_FMT.DATE_TIME`
    - `time_zone` : `int`, optional
        - 时区，默认为东八区

    Returns
    ----------
    - `str`
        - 格式化后的时间字符串
    """
    td = timedelta(hours=time_zone)
    tz = timezone(td)
    dt = datetime.fromtimestamp(ts, tz)
    dt = dt.strftime(fmt)
    return dt


def format_time_delta(seconds: float) -> str:
    delta = timedelta(seconds=seconds)
    return str(delta)[:-3]


def now(fmt: str = TIME_FMT.DATE_TIME, time_zone: int = 8) -> str:
    """获取当前时间

    >>> print(now())
    2024-10-12 16:00:00

    Parameters
    ----------
    - `fmt` : `str`, optional
        - 格式化字符串，默认为 `TIME_FMT.DATE_TIME`
    - `time_zone` : `int`, optional
        - 时区，默认为东八区

    Returns
    ----------
    - `str`
        - 当前时间字符串
    """
    ts = time.time()
    return format_time(ts, fmt, time_zone)


class TicToc:
    def __init__(self):
        self._tic = 0
        self._toc = 0
        self._elapsed = 0

    def tic(self):
        self._tic = timer()

    def toc(self):
        self._toc = timer()
        self._elapsed = self._toc - self._tic

    @property
    def elapsed(self):
        delta = timedelta(seconds=self._elapsed)
        return str(delta)[:-3]

    def print_elapsed(self, name: Optional[str] = None):
        if name is None:
            name = 'It'
        else:
            name = colored(name, 'yellow')
        print(f'{name} took {colored(self.elapsed, "cyan")}')


def print_elapsed(func):
    """打印函数执行时间

    ```python
    @print_elapsed
    def my_func():
        import time
        time.sleep(1)
    ```

    >>> my_func()
    my_func took 0:00:01.007 seconds

    Parameters
    ----------
    - `func` : `Callable`
        - 被装饰的函数

    Returns
    ----------
    - `Callable`
        - 装饰后的函数
    """

    def wrapper(*args, **kwargs):
        tictoc = TicToc()
        tictoc.tic()
        result = func(*args, **kwargs)
        tictoc.toc()
        tictoc.print_elapsed(func.__name__)
        return result

    return wrapper
