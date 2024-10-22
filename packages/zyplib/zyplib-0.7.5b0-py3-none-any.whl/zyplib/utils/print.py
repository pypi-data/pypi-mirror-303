from typing import Any, Literal


def type_summary(obj: Any) -> str:
    """返回对象的类型摘要

    此函数接受任何类型的对象，并返回一个字符串，描述该对象的类型和一些基本信息。

    Examples
    --------

    >>> type_summary("hello")
    'hello'
    >>> type_summary(42)
    '42'
    >>> type_summary(3.14159)
    '3.142'
    >>> type_summary([1, 2, 3])
    'int[3]'
    >>> type_summary({'a': 1, 'b': 2})
    "dict[str: int]"
    >>> import numpy as np
    >>> type_summary(np.array([1, 2, 3]))
    'ndarray@int64(3,)'
    """
    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, float):
        return f'{obj:.3f}'
    elif isinstance(obj, list):
        if len(obj) == 0:
            return '[]'
        else:
            # int[3]
            item_type = type(obj[0])
            return f'{item_type.__name__}[{len(obj)}]'
    elif isinstance(obj, tuple):
        return tuple([type_summary(k) for k in obj])
    elif isinstance(obj, dict):
        if len(obj) == 0:
            return f'{type(obj).__name__}[]'
        else:
            key_type = type(next(iter(obj.keys())))
            value_type = type(next(iter(obj.values())))
            return f'{type(obj).__name__}[{key_type.__name__}: {value_type.__name__}]'
    elif hasattr(obj, 'shape') and hasattr(obj, 'dtype'):
        return f'{type(obj).__name__}@{obj.dtype}{obj.shape}'
    else:
        return type(obj).__name__


COLOR_MAP = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'gray': '\033[90m',
    'reset': '\033[0m',
}


COLOR_TYPE = Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'gray']


def colored(text: str, color: COLOR_TYPE):
    """为文本添加颜色


    Parameters
    ----------
    - `text` : `str`
        - 原始文本
    - `color` : `COLOR_TYPE`
        - 颜色类型
        - `"red"` | `"green"` | `"yellow"` | `"blue"` | `"magenta"` | `"cyan"` | `"white"` | `"gray"`
    """
    return f"{COLOR_MAP[color]}{text}{COLOR_MAP['reset']}"


def print_colored(color: COLOR_TYPE, *args, **kwargs):
    """打印带颜色的文本

    Parameters
    ----------
    - `color` : `COLOR_TYPE`
        - 颜色类型
        - `"red"` | `"green"` | `"yellow"` | `"blue"` | `"magenta"` | `"cyan"` | `"white"` | `"gray"`
    """

    total_text = ' '.join([str(arg) for arg in args])
    print(colored(total_text, color), **kwargs)


def print_debug(*args, **kwargs):
    """打印调试信息（白色）"""
    print_colored('gray', *args, **kwargs)


def print_info(*args, **kwargs):
    """打印信息（青色）"""
    print_colored('cyan', *args, **kwargs)


def print_warn(*args, **kwargs):
    """打印警告信息（黄色）"""
    print_colored('yellow', *args, **kwargs)


def print_warning(*args, **kwargs):
    """打印警告信息（黄色）"""
    print_colored('yellow', *args, **kwargs)


def print_error(*args, **kwargs):
    """打印错误信息（红色）"""
    print_colored('red', *args, **kwargs)
