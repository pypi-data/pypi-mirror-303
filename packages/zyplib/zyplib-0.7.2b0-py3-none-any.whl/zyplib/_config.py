import json
import os
from dataclasses import dataclass

BASE_DIR = os.path.expanduser('~/.zyplib')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')


@dataclass
class Config:
    DISK_CACHE_DIR: str = './cache'
    DISK_CACHE_MAX_SIZE: int = 2 * 1024 * 1024 * 1024  # 2GB


def _write_config(config: Config):
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    config_path = os.path.expanduser(CONFIG_PATH)
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config.__dict__, file, indent=4)


def _load_config() -> Config:
    # 获取配置文件路径
    config_path = os.path.expanduser(CONFIG_PATH)

    # 如果配置文件存在，则加载配置文件
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_dict = json.load(file)

        # 覆盖默认配置
        config = Config(**config_dict)
    else:
        # 如果配置文件不存在，返回默认配置
        config = Config()
    _write_config(config)
    return config


# 实例化配置，在模块导入时加载
config = _load_config()
