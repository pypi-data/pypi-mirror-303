import functools
import os
from dataclasses import dataclass
from typing import Any, Callable, Optional, TypeVar

import numpy as np
import torch
from diskcache import Cache, Timeout
from prettytable import PrettyTable

# from prettytable import PrettyTable
from zyplib._config import config
from zyplib.utils.print import print_info, print_warn, type_summary

_configs = {
    'cache_dir': config.DISK_CACHE_DIR,
    'cache_max_size': config.DISK_CACHE_MAX_SIZE, # MB
}


def update_cache_config(cache_dir: str = None, cache_max_size_mb: int | float = None):
    if cache_dir is not None:
        _configs['cache_dir'] = cache_dir
    if cache_max_size_mb is not None:
        _configs['cache_max_size'] = cache_max_size_mb


def cache_factory(cache_dir: str = None) -> Cache:
    """创建缓存对象

    - 如果传入 `cache_dir` 则使用传入的目录作为 diskcache 的缓存目录
    - 如果传入 `cache_dir` 为 None 则使用默认缓存目录
        - 默认缓存目录为 `./cache`, 可以通过 `update_cache_config` 函数设置

    Parameters
    ----------
    - `cache_dir` : `str`, optional
        - 缓存目录; 如果为 None 则使用 _config 中的默认缓存目录

    Returns
    ----------
    - `Cache`
        - 缓存对象
    """
    cache_dir = os.path.join(_configs['cache_dir']) if cache_dir is None else cache_dir
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    size_limit = _configs['cache_max_size'] * 1024 * 1024
    return Cache(cache_dir, size_limit=size_limit)


def get_cache(key: str, default: Any = None, cache_dir: str | None = None):
    """获取缓存

    Parameters
    ----------
    - `key` : `str`
        - 缓存键
    - `default` : `Any`, optional
        - 默认值，当缓存不存在时返回
    - `cache_dir` : `str | None`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录

    Returns
    ----------
    - `Any`
        - 缓存值, 当缓存不存在或者过期时返回默认值
    """
    try:
        with cache_factory(cache_dir) as cache:
            return cache.get(key, default)
    except Timeout as t:
        print_warn(f'Cache[{key}] timeout: {t}')
        return default


def set_cache(
    key: str,
    value: Any,
    expire_seconds: int = None,
    tag: str = None,
    cache_dir: str | None = None,
):
    """设置缓存

    Parameters
    ----------
    - `key` : `str`
        - 缓存键
    - `value` : `Any`
        - 缓存值
    - `expire_seconds` : `int`, optional
        - 缓存过期时间; 如果为 None 则不设置过期时间
    - `tag` : `str`, optional
        - 缓存标签
    - `cache_dir` : `str | None`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录

    Returns
    ----------
    - `bool`
        - 设置成功返回 True, 否则返回 False
    """
    with cache_factory(cache_dir) as cache:
        flag = cache.set(key, value, expire=expire_seconds, tag=tag)
    if not flag:
        print_warn(f'Cache[{key}] set failed')
    return flag


def del_cache(key: str, cache_dir: str | None = None):
    """删除缓存

    Parameters
    ----------
    - `key` : `str`
        - 缓存键
    - `cache_dir` : `str | None`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录
    """
    with cache_factory(cache_dir) as cache:
        cache.delete(key)


def purge_all_cache(cache_dir: str | None = None):
    """清空所有缓存

    Parameters
    ----------
    - `cache_dir` : `str | None`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录
    """
    with cache_factory(cache_dir) as cache:
        cache.clear()


def use_cache(
    key,
    fn_value: Callable[[], Any],
    cache_dir: str | None = None,
    expire_seconds: int = None,
    tag: str = None,
):
    """使用缓存, 如果缓存命中则直接返回缓存值, 否则调用 fn_value 计算值并缓存


    Parameters
    ----------
    - `key` : `str`
        - 缓存键
    - `fn_value` : `Callable[[], Any]`
        - 计算值的函数
    - `cache_dir` : `str | None`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录
    - `expire_seconds` : `int`, optional
        - 缓存过期时间; 如果为 None 则不设置过期时间
    - `tag` : `str`, optional
        - 缓存标签

    Returns
    ----------
    - `Any`
        - 缓存值

    Examples
    ----------
    >>> def fn_value():
    >>>     return 1
    >>> use_cache('key', fn_value)
    """
    with cache_factory(cache_dir) as cache:
        value = cache.get(key, default=None)
        if value is None:
            value = fn_value()
            cache.set(key, value, expire=expire_seconds, tag=tag)
    return value


@dataclass
class CacheItem:
    key: str
    value: Any
    expire_time: int
    tag: str


def list_caches(cache_dir: str | None = None):
    """列出所有缓存; 通过

    Parameters
    ----------
    - `cache_dir` : `str`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录

    Yields
    ----------
    - `CacheItem`: 缓存项
    """
    with cache_factory(cache_dir) as cache:
        keys = list(cache.iterkeys())
        for key in keys:
            obj, expire_time, tag = cache.get(
                key, default=None, expire_time=True, tag=True
            )
            cache_item = CacheItem(key=key, value=obj, expire_time=expire_time, tag=tag)
            yield cache_item


def display_caches(cache_dir: str | None = None, table: bool = True):
    """打印缓存状态

    Parameters
    ----------
    - `cache_dir` : `str`, optional
        - 缓存目录; 如果为 None 则使用 cache_factory 中的默认缓存目录
    - `table` : `bool`, optional
        - 是否使用 PrettyTable 展示; 如果为 False 则使用 print 打印
    """
    with cache_factory(cache_dir) as cache:
        size = cache.volume()
    print_info(f'缓存大小: {size / 1024 / 1024:.2f} MB')

    caches = list_caches(cache_dir)
    if table:
        table = PrettyTable(['Index', 'Key', 'Value', 'Expire', 'Tag'])
        for idx, cache_item in enumerate(caches):
            table.add_row(
                [
                    idx,
                    type_summary(cache_item.key),
                    type_summary(cache_item.value),
                    cache_item.expire_time,
                    cache_item.tag,
                ]
            )
        print_info(f'缓存: {_configs["cache_dir"]}'.center(60, '='))
        print_info(table)
    else:
        print_info(f'缓存: {_configs["cache_dir"]}')
        for idx, cache_item in enumerate(caches, start=1):
            print_info(f'缓存 {idx}'.center(60, '='))
            print_info('Key:', end='\t')
            print(cache_item.key)
            print_info('Value:', end='\t')
            print(cache_item.value)
            print_info('Expire:', end='\t')
            print(cache_item.expire_time)
            print_info('Tag:', end='\t')
            print(cache_item.tag)
            print('')


F = TypeVar('F', bound=Callable)


def make_func_memoize(
    func: F, cache: Cache, name=None, typed=False, expire=None, tag=None, ignore=()
) -> F:
    """接受一个函数对象，为其动态添加 diskcache 的 memoize 功能"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        memoized_func = cache.memoize(
            name=name, typed=typed, expire=expire, tag=tag, ignore=ignore
        )(func)
        return memoized_func(*args, **kwargs)

    return wrapper
