import os
import random
import shutil
import string
from typing import Optional


def random_string(length=10):
    """生成随机字符串"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class DottableDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self


class RuntimeDir(os.PathLike):
    """管理运行时的临时目录"""

    RUNTIME_BASE_DIR = '.'

    def __init__(self, rm_on_exit=True, dir: Optional[str] = None):
        self.rm_on_exit = rm_on_exit
        self.file_handler = None

        # 如果 dir 为 None, 则会在 RUNTIME_BASE_DIR 下创建一个随机目录
        if dir is None:
            self.rm_on_exit = rm_on_exit
            self._create_dir()
        # 如果 dir 为 str, 则将改目录作为运行时目录
        else:
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.dir = dir

    def _create_dir(self):
        new_dir = os.path.join(self.RUNTIME_BASE_DIR, self._new_dir(self.rm_on_exit))
        while os.path.exists(new_dir):
            new_dir = os.path.join(self.RUNTIME_BASE_DIR, self._new_dir(self.rm_on_exit))
        os.makedirs(new_dir)
        self.dir = new_dir

    @classmethod
    def set_base_dir(cls, base_dir):
        cls.RUNTIME_BASE_DIR = base_dir

    def _new_dir(self, rm_on_exit):
        new_dirname = random_string(8)
        return new_dirname

    def __str__(self) -> str:
        return self.dir

    __fspath__ = __str__

    __repr__ = __str__

    def write_file(self, file_name, content, *args, **wargs):
        """写入文件"""
        with open(os.path.join(self.dir, file_name), *args, **wargs) as self.file_handler:
            self.file_handler.write(content)

    def open_file(self, file_name, *args, **wargs):
        """打开文件"""
        self.file_handler = open(os.path.join(self.dir, file_name), *args, **wargs)
        return self.file_handler

    def delete(self):
        if self.file_handler is not None and not self.file_handler.closed:
            self.file_handler.close()
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)

    def purge(self):
        if self.rm_on_exit:
            self.delete()

    def __del__(self):
        self.purge()
