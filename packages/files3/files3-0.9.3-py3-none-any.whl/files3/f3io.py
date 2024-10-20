from files3.f3utils import *
import lz4.frame as lzf
from io import BytesIO
import pickletools
import subprocess
import zipfile
import pickle
import sys
import os
import io

# 目标文件不是F3Inst文件的错误
class NotF3InstError(Exception): ...

# 目标文件无法解包的错误
class NotF3UnpackableError(Exception): ...


# 目标文件丢失源代码文件路径的错误
class LostSourceCodeError(Exception): ...

class _F3Unpickler(pickle._Unpickler):
    @memoize
    def find_class(self, __module_name: str, __global_name: str):
        """
        Find the class by the module name and the global name
        :param __module_name: like __main__
        :param __global_name: like MyClass
        :return:
        """
        # Try to get the target file path
        try:
            if self.rlinkpath:
                tar_file = self.rlinkpath
            elif len(self.metastack) > 1:
                tar_file = self.metastack[1][0]
            else:
                tar_file = self.stack[0]
            tar_file = os.path.abspath(tar_file)
        except:
            raise NotF3InstError(f"Can not get scp. # Meta = {self.metastack}, Stack = {self.stack}")

        # Get the directory of the target file
        tar_dir = os.path.dirname(tar_file)

        # If the module name is '__main__', do the following
        if __module_name == '__main__':
            # Check if the target file exists
            if not os.path.exists(tar_file):
                raise LostSourceCodeError(f"Can not find target source code file (not exist). # target file = {tar_file}")

            # Get the base name of the target file and remove the extension
            tar_name = os.path.basename(tar_file)
            tar_name, _ = os.path.splitext(tar_name)

            # Check if it's an init file
            if tar_name == "__init__":
                tar_name = os.path.basename(tar_dir)
                tar_dir = os.path.dirname(tar_dir)
                if not tar_name:
                    raise ValueError("Source code file:__init__.py file at a disk root.")

            # Set the module name to the base name of the target file
            __module_name = tar_name

        # Add the target directory to the system path
        sys.path.append(tar_dir)

        # Find and return the class
        kclass = super(_F3Unpickler, self).find_class(__module_name, __global_name)

        # Remove the target directory from the system path
        sys.path.pop(-1)

        return kclass

    def load(self, relink_path:str=None):
        self.rlinkpath = relink_path
        scp_obj = super(_F3Unpickler, self).load()  # [scp, obj]

        try:
            scp, obj = scp_obj
        except:
            raise NotF3InstError("Can not parse scp|obj from raw. Please make sure it's created by files3 >= 0.6")

        return obj


f3bytes = bytes
zip_bytes = bytes
f3zip_bytes = bytes


def f3dumps(obj, relink_path:str=None):
    """
    save as [scp, obj]
    * mean if any custom class in obj. we can get it's creater code path before find_class.
    * so it help code to find the real class code.

    :param obj:
    :param scp: Source Code Path(Auto Get)
    :return:
    """
    if relink_path is not None:
        scp = relink_path
    else:
        scp = get_top_target_file_path()
    s = pickle.dumps([scp, obj])
    s = pickletools.optimize(s)
    return lzf.compress(s)

def f3loads(s, *, fix_imports=True, encoding="ASCII", errors="strict",
           buffers=None, relink_path=None):
    """

    :param s:
    :param fix_imports:
    :param encoding:
    :param errors:
    :param buffers:
    :param relink_path: relink path
    :return:
    """
    try:
        s = lzf.decompress(s)
    except:
        raise NotF3InstError("Can not decompress bytes data. Please make sure it's created by files3 >= 0.6")
    if isinstance(s, str):
        raise UnicodeError("Can't load pickle from unicode string")
    file = io.BytesIO(s)
    return _F3Unpickler(file, fix_imports=fix_imports, buffers=buffers,
                      encoding=encoding, errors=errors).load(relink_path)

def packtarget(path:str, *, mode=zipfile.ZIP_STORED, level=None) -> zip_bytes:
    """
    打包目标文件或目录到zip-bytes
    :param path: 目标文件或目录
    :param error: 是否抛出错误
    :return: zip_bytes
    """
    path = os.path.abspath(path)
    dirname, basename = os.path.split(path)

    if not os.path.exists(path):
        raise FileNotFoundError(f"files.pack: File not found: {path}")

    # 创建一个BytesIO对象用于存储zip文件
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', mode, compresslevel=level) as zf:
        if os.path.isfile(path):
            zf.write(path, arcname=basename)
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    # 创建文件的完整路径
                    file_path = os.path.join(root, file)
                    # 相对于arcname的路径
                    arcname_relpath = os.path.relpath(file_path, dirname)
                    # 将文件添加到zip文件中
                    zf.write(file_path, arcname=arcname_relpath)
    # 将buffer的指针移动到开始位置
    buffer.seek(0)
    # 返回zip文件的字节内容
    return buffer.getvalue()


def unpacktarget(data:zip_bytes, extract_path:str=None, overwrite=False) -> zipfile.ZipFile|None:
    """
    解压zip字节流到指定目录

    :param data: zip文件的字节流
    :param extract_path: 解压目标目录, 如果传入None则返回ZipFile对象.
    :param overwrite: 是否覆盖已存在的文件, 仅在extract_path不为None时有效
    :return: None|ZipFile
    """
    if extract_path is not None:
        # 确保目标目录存在
        extract_path = os.path.abspath(extract_path)
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

    # 使用BytesIO将字节流转换为文件对象
    try:
        zf = zipfile.ZipFile(BytesIO(data), 'r')
    except zipfile.BadZipFile:
        raise NotF3UnpackableError("Can not unpack the target data. Please make sure it's created by files.pack.")

    # 返回ZipFile对象或是解压到目标路径
    if extract_path is None:
        return zf
    else:
        for file in zf.namelist():
            file_path = os.path.join(extract_path, file)
            if os.path.exists(file_path) and not overwrite:
                raise FileExistsError(f"files.unpack: File already exists: {file_path}\n\nIf you want to overwrite, please set overwrite=True.")
            zf.extract(file, extract_path)


def bytes2py(data:f3bytes, *, info:str='') -> str:
    """
    将bytes数据转换为python代码
    """
    _ = '\n# '.join(info.split('\n'))
    code = (f"# This code is generated by files3\n"
            f"# {_}\n\n"
        "F3DATA = (b''\n")

    length = len(data)
    num_per_line = 256
    for i in range(0, length, num_per_line):
        _txt = "b'"
        for b in data[i:i+num_per_line]:
            _txt += f"\\x{b:02x}"
        _txt += "'"
        code += f"{_txt}\n"

    return code + ")\n"

def packtargetpy(path:str, *, mode=zipfile.ZIP_STORED, level=None) -> str:
    """
    打包目标文件或目录到python代码
    """
    data = packtarget(path, mode=mode, level=level)
    data = f3dumps(data)
    return bytes2py(data, info=f"target source path: {os.path.abspath(path)}")


def py2bytes(code:str) -> f3bytes:
    """
    将python代码转换为bytes数据
    """
    env = {}
    exec(code, env)
    if 'F3DATA' not in env:
        raise ValueError("Can not find 'F3DATA' in the code.")
    return env['F3DATA']

def unpacktargetpy(code:str, extract_path:str=None, overwrite=False, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None) -> zipfile.ZipFile|None:
    """
    解压python代码到指定目录
    """
    data = py2bytes(code)
    data = f3loads(data, fix_imports=fix_imports, encoding=encoding, errors=errors, buffers=buffers)
    return unpacktarget(data, extract_path, overwrite)


def testc(cmd: str) -> bool:
    """
    测试命令是否存在，不显示输出。
    """
    with subprocess.Popen(f"where {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        return proc.wait() == 0


class F3SegmentTail:
    """
    允许向文件尾部添加一段16 + len(TAIL_IDENTITY)字节的数据
    第一个字节: 0:远古版本, z: zip文件, f: f3文件
    """
    TAIL_IDENTITY = b'.\x00F3'
    TAIL_LENGTH = len(TAIL_IDENTITY)
    def __init__(self):
        # assert length < 255, "The length must be less than 255"
        self._bytearray = bytearray(16)

    @property
    def data(self):
        return bytes(self._bytearray)

    @data.setter
    def data(self, value:bytes):
        if not isinstance(value, bytes):
            raise TypeError("Data must be bytes")
        if len(value) > 16:
            raise ValueError(f"Data length must be less than {16}")
        self._bytearray[:len(value)] = value

    def clear(self):
        self._bytearray = bytearray(16)

    def parse(self, fio:io.BufferedIOBase, *, clear=True) -> bool:
        """
        从文件中解析尾部f3segmentTail数据到自身
        成功返回True，否则返回False
        """
        if clear:
            self.clear()
        if isinstance(fio, str):
            fio = open(fio, 'rb')

        _initial = fio.tell()

        # 读取文件末尾TAIL_LENGTH长度的数据
        fio.seek(-self.TAIL_LENGTH, io.SEEK_END)
        tail = fio.read(self.TAIL_LENGTH)
        # 如果读取的数据不是TAIL_IDENTITY，则返回False
        if tail != self.TAIL_IDENTITY:
            fio.seek(_initial)
            return False
        # 读取数据
        fio.seek(-self.TAIL_LENGTH - 16, io.SEEK_END)
        self._bytearray = bytearray(fio.read(16))
        fio.seek(_initial)
        return True

    def write(self, fio:io.BufferedIOBase):
        """
        将自身数据写入文件末尾
        """
        if isinstance(fio, str):
            fio = open(fio, 'ab')
        fio.write(self._bytearray)
        fio.write(self.TAIL_IDENTITY)

    @property
    def zf(self):
        return self._bytearray[0]

    @zf.setter
    def zf(self, value:bool):
        self._bytearray[0] = int(value)

import time
if __name__ == '__main__':
    print(testc('python'))
    print(testc('adwakhdks'))

