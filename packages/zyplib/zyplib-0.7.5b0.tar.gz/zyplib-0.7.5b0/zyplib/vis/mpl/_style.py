import os

import matplotlib.pyplot as plt


def register_mpl_styles(plt_use: str | list[str] | None = None):
    """
    注册 matplotlib 内置的样式

    源码
    ----------
    本代码来自: https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/__init__.py
    """
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    styles_path = os.path.join(current_dir_path, 'styles')

    # Reads styles in /styles folder and all subfolders
    stylesheets = {}  # plt.style.library is a dictionary
    for folder, _, _ in os.walk(styles_path):
        new_stylesheets = plt.style.core.read_style_directory(folder)
        stylesheets.update(new_stylesheets)

    # Update dictionary of styles - plt.style.library
    plt.style.core.update_nested_dict(plt.style.library, stylesheets)
    # Update `plt.style.available`, copy-paste from:
    # https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
    plt.style.core.available[:] = sorted(plt.style.library.keys())

    if plt_use is not None:
        plt.style.use(plt_use)
