"""
文件系统相关工具
"""

import json
import os
import shutil
from pathlib import Path
from typing import Literal, Union

import yaml

from .print import print_debug

FilePath = Union[Path, str]


def expand_user(path: FilePath) -> FilePath:
    return Path(path).expanduser()


def expand_relative(path: FilePath) -> FilePath:
    """完全基于调用文件位置而非工作目录的相对路径

    >>> expand_relative('../data/')  # 在 /home/ 下运行的 /home/user/a/test.py 文件
    >>> /home/user/data/
    """
    file_dir = Path(__file__).parent
    return file_dir.joinpath(path).resolve()


def ensure_dir(dir: str, if_not_empty: Literal['keep', 'clean', 'error'] = 'keep', verbose: bool = False):
    """检查用于保存日志、Checkpoint 等的目录如果 dir 不存在，则创建

    Parameters
    ----------
    - `dir` : `str`
        - 目录
    - `if_not_empty` : `Literal['keep', 'clean', 'error']`, optional
        - 如果目录不为空，则执行的操作
        - `"keep"` | `"clean"` | `"error"`
    - `verbose` : `bool`, optional
        - 是否打印日志，默认为 False
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    elif any(os.scandir(dir)):
        if if_not_empty is None or if_not_empty == 'keep':
            if verbose:
                print_debug(f'ensure_dir: exists {dir}.')
        elif if_not_empty == 'clean':
            if verbose:
                print_debug(f'ensure_dir: clean up {dir}.')
            shutil.rmtree(dir)
            os.makedirs(dir)
        elif if_not_empty == 'error':
            raise Exception(f'目录 {dir} 不为空!')
        else:
            raise ValueError(f'check_dir 参数错误: if_not_empty = {if_not_empty}')


def file_reader(file_path: FilePath, encoding: str = 'utf-8', binary: bool = False):
    mode = 'rb' if binary else 'r'
    return open(file_path, mode, encoding=None if binary else encoding)


def read_file(
    file_path: FilePath,
    encoding: str = 'utf-8',
    binary: bool = False,
    readlines: bool = False,
) -> Union[str, list[str]]:
    with file_reader(file_path, encoding, binary) as f:
        if readlines:
            return f.readlines()
        return f.read()


def file_writer(file_path: FilePath, encoding: str = 'utf-8', binary: bool = False):
    mode = 'wb' if binary else 'w'
    return open(file_path, mode, encoding=None if binary else encoding)


def write_file(
    file_path: FilePath,
    content: Union[str, bytes],
    encoding: str = 'utf-8',
    binary: bool = False,
):
    ensure_dir(os.path.dirname(file_path))
    with file_writer(file_path, encoding, binary) as f:
        f.write(content)


def read_json(file_path: FilePath, encoding: str = 'utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)


def write_json(file_path: FilePath, data: dict, encoding: str = 'utf-8'):
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_yaml(file_path: FilePath, throw_error: bool = True):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        if throw_error:
            raise e
        return {}


def write_yaml(file_path: FilePath, data: dict):
    ensure_dir(os.path.dirname(file_path))
    def str_presenter(dumper, data):
        if len(data.splitlines()) > 1:  # check for multiline string
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter)

    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
