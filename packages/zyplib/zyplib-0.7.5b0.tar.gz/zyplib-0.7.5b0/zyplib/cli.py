import argparse
import sys

from zyplib.utils.cli import parse_cli_args
from zyplib.utils.fs import write_json
from zyplib.utils.print import print_info, print_warning

commands = {}
kv_args = {}


def add_command(name):
    def decorator(func):
        commands[name] = func
        return func

    return decorator


@add_command('new-config-file')
def create_config_file():
    """创建一个 zyplib.config.json 文件"""
    from . import _config

    fname = 'zyplib.config.json'
    write_json(fname, _config.config.asdict())


@add_command('show-config')
def show_config():
    """显示当前配置"""
    from . import _config

    print_info(_config.config.asdict())


@add_command('reset-global-config')
def reset_global_config():
    """重置全局配置"""
    from . import _config
    config = _config.Config()
    print_info(f'重置全局配置为: {config}')
    _config._write_config(config)


@add_command('show-caches')
def show_caches():
    """显示当前缓存, 可选参数 table={true, false}
    """
    from zyplib.utils.cache import display_caches
    show = kv_args.get('table', True)
    display_caches(table=show)


def help_doc():
    docs = []
    for command, func in commands.items():
        docs.append(f'* {command}: {func.__doc__}')
    return '\n'.join(docs)


def main():
    parser = argparse.ArgumentParser(
        description='ZypLib CLI tool',
        epilog=help_doc(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('command', type=str, help='Command to run', nargs='?')
    parser.add_argument('args', nargs=argparse.REMAINDER, help='Additional arguments')

    args = parser.parse_args()

    global kv_args
    kv_args = parse_cli_args()

    command = getattr(args, 'command', None)
    if command and command in commands:
        commands[command]()
    else:
        print_warning(f'未知的命令: {command}')
        print(help_doc())

    sys.exit(0)


if __name__ == '__main__':
    main()
