import sys


def parse_cli_args():
    """解析任意命令行中 key=value 形式的参数

    只要是后面跟着的 --argname=argvalue 都会被解析到字典中
    """

    def _parse_str_to_value(value: str):
        try:
            return int(value)
        except ValueError:
            ...

        try:
            return float(value)
        except ValueError:
            ...

        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'

        try:
            return eval(value)
        except Exception:
            ...

        return value

    args = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            key, value = arg.split('=')
            if key.startswith('--'):
                key = key[2:]
            args[key] = _parse_str_to_value(value)
    return args
