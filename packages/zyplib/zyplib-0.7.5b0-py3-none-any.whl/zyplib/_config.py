import json
import os
from dataclasses import asdict, dataclass

BASE_DIR = os.path.expanduser('~/.zyplib')
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')


@dataclass
class Config:
    DISK_CACHE_DIR: str = './cache'
    DISK_CACHE_MAX_SIZE: int = 3 * 1024 # MB

    def asdict(self):
        return asdict(self)


def _write_config(config: Config):
    """写入全局的配置文件"""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    config_path = os.path.expanduser(CONFIG_PATH)
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config.__dict__, file, indent=4)


def _load_config() -> Config:
    # Load global config
    try:
        global_config = _load_global_config()
    except Exception:
        global_config = Config()

    # Load local config and merge with global config
    try:
        local_config = _load_local_config()
    except Exception:
        local_config = {}
    merged_config = {**asdict(global_config), **local_config}

    # Create final config object
    config = Config(**merged_config)
    return config


def _load_global_config() -> Config:
    config_path = os.path.expanduser(CONFIG_PATH)
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config_dict = json.load(file)
        return Config(**config_dict)
    else:
        _write_config(Config())
    return Config()


def _load_local_config() -> dict:
    local_config_path = 'zyplib.config.json'
    if os.path.exists(local_config_path):
        with open(local_config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}


# 实例化配置，在模块导入时加载
config = _load_config()
