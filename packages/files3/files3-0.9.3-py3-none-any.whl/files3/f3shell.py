import os
import re
import shutil
import typing
import zipfile
from files3.f3info import F3Info, PF_DTYPE
from files3.f3bool import *
from files3.f3core import F3Core
from files3.f3utils import *
from files3.f3io import testc
from files3.f3io import packtarget, unpacktarget
from files3.f3io import f3bytes, zip_bytes, f3zip_bytes
from files3.f3io import bytes2py, py2bytes, packtargetpy, unpacktargetpy

function = type(lambda: ...)


class RetypeFailedError(Exception): ...

class RelinkFailedError(Exception): ...

class F3Shell(object):
    _F3INSTS = ['_f3info',
                'set', 'get', 'has', 'delete',
                'retype', 'relink',
                'keys', 'values', 'items',
                'hash', "list",
                "dumps", "loads",
                "pack", "unpack"
                ]
    _F3BACKEND = F3Core()

    def __init__(self, path="", type=PF_DTYPE, sub_type=PF_DTYPE):
        self._f3info = F3Info(path, type, sub_type)

    def _shell_magic_filter_(self, item, type=True, listes=[]):
        """
        标准筛选支持:（sysfunc .protected.）
        1.str
        2.... or slice[:](仅限全选)
        3.re.Pattern 对每个key(type == False)或是fname(type == True)
        4.func(name, type)->bool 将返回True的结果对应的item选中
        5.[]  各个条件间相并
        :param item:
        :param type: whether suffix or not. If False, only select self.info.type
        :param listes: 递归用，用户勿传     Recursive use, users do not pass
        :return: [] of '$name + $type'
        """
        _end = self._f3info.type if type else ""
        # 第一轮筛选 -- 简单筛选
        if isinstance(item, slice) or item is ...:
            return self._F3BACKEND.list(self._f3info)
        elif isinstance(item, str):
            return [item + _end]

        _return = []
        # 第二轮筛选 -- advanced筛选
        if not listes:
            listes = os.listdir()
        if isinstance(item, function):
            for fname in listes:
                _key, _type = os.path.splitext(fname)
                if type or self._f3info.type == _type:
                    try:
                        _value = item(_key)
                    except Exception as err:
                        print(f"Bad filter function: {item}. Cause error: {err}\n\nPlease check your function(fname)->bool and it's code.")
                    if bool(_value) == True:
                        _return += [(_key + _end) if not type else fname]

        elif isinstance(item, re.Pattern):
            for fname in listes:
                _key, _type = os.path.splitext(fname)
                if type or self._f3info.type == _type:
                    if item.match(_key if not type else fname):
                        _return += [(_key + _end) if not type else fname]
        elif isinstance(item, list):
            for _item in item:
                _return += self._shell_magic_filter_(_item, type, listes)
        else:
            raise Exception("Unkown item - " + str(item))
        return list(set(_return))

    def __getitem__(self, item):
        if isinstance(item, tuple):
            if len(item) != 2:
                raise ValueError("Tuple must have 2 elements(key:str, skey:str). But got " + str(item))
            return self.get(item[0], item[1], error=True)
        _return = []
        for key in self._shell_magic_filter_(item, type=False):
            _return += [self.get(key, error=True)]
        return F3False if not _return else (_return[0] if len(_return) == 1 else _return)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise ValueError("Tuple must have 2 elements(key:str, skey:str). But got " + str(key))
            self.set(key[0], value, key[1], error=True)
            return
        for key in self._shell_magic_filter_(key, type=False):
            self.set(key, value, error=True)

    def __getattr__(self, item):
        return self.get(item, error=True)

    def __setattr__(self, key, value):
        if key not in self._F3INSTS and not (key[:2] != '__' and key[-2:] == '__'):
            self.__setitem__(key, value)
        else:
            super(F3Shell, self).__setattr__(key, value)

    def __delitem__(self, key):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise ValueError("Tuple must have 2 elements(key:str, skey:str). But got " + str(key))
            self.delete(key[0], key[1], error=True)
            return
        for key in self._shell_magic_filter_(key, type=False):
            self.delete(key, error=True)

    def __delattr__(self, item):
        self.delete(item, error=True)

    def __len__(self):
        return len(list(self.keys()))

    def __contains__(self, item):
        _return = True
        for key in self._shell_magic_filter_(item, type=False):
            _return *= self.has(item, error=True)
        return bool(_return)

    def __iter__(self):
        return self.keys()

    def keys(self) -> typing.Iterable:
        return F3Shell._F3BACKEND.iter(self._f3info)

    def values(self) -> typing.Iterable:
        for key in self.keys():
            yield self.get(key, error=True)

    def items(self) -> typing.Iterable:
        for key in self.keys():
            yield key, self.get(key, error=True)

    def has(self, key: str, skey: str = None, *, error: False = False) -> F3Bool:
        """
        成功返回F3True，如果目标文件不存在，则返回F3False
        Has a pyfile file exists. Returns True successfully, or False if the target file doesnot exists

        :param info:     InfoPackage inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool  whether raise error.
        :return: F3Bool
        """
        if not isinstance(key, str):
            if error: raise TypeError(f"files.has: The key must be str. got {type(key)}")
            return F3False
        if not isinstance(skey, str) and skey is not None:
            if error: raise TypeError(f"files.has: The skey must be str or None. got {type(skey)}")
            return F3False
        skey = skey or None
        return F3Shell._F3BACKEND.has(self._f3info, key, skey)

    def set(self, key: str, pyobject: object, skey: str = None, *, error=False) -> F3Bool:
        """
        存储python对象到目标文件夹下。成功返回F3True，如果目标文件被锁定或占用，则返回F3False
        Storing Python objects to pyfile under specific path in InfoPackage. Returns True successfully. If the target file is locked or occupied, returns False

        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param pyobject: python对象   python object
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool  whether raise error.
        :return: F3Bool
        """
        if not isinstance(key, str):
            if error: raise TypeError(f"files.set: The key must be str. got {type(key)}")
            return F3False
        if not isinstance(skey, str) and skey is not None:
            if error: raise TypeError(f"files.set: The skey must be str or None. got {type(skey)}")
            return F3False
        skey = skey or None
        return F3Shell._F3BACKEND.set(self._f3info, key, pyobject, skey, error=error)

    def get(self, key: str, skey: str = None, *, error=False) -> object | F3Bool:
        """
        成功返回读取到的pyobject，如果目标文件不存在，则返回F3False
        Find data files. The read pyobject is returned successfully. If the target file does not exist, false is returned

        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool  whether raise error.
        :return: object|F3Bool
        """
        if not isinstance(key, str):
            if error: raise TypeError(f"files.get: The key must be str. got {type(key)}")
            return F3False
        if not isinstance(skey, str) and skey is not None:
            if error: raise TypeError(f"files.get: The skey must be str or None. got {type(skey)}")
            return F3False
        skey = skey or None

        # 如果skey但是为file，那么应当返回F3False
        if skey is not None and os.path.isfile(self._f3info(key)):
            return F3False

        return F3Shell._F3BACKEND.get(self._f3info, key, skey, error=error)

    def delete(self, key: str, skey: str = None, *, error=False) -> F3Bool:
        """
        成功或目标文件不存在则返回F3True，如果目标文件存在而无法删除，则返回F3False
        Delete pyfile file. Returns True if the target file is successful or does not exist. Returns False if the target file exists and cannot be deleted

        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool  whether raise error.
        :return: F3Bool
        """
        if not isinstance(key, str):
            if error: raise TypeError(f"files.delete: The key must be str. got {type(key)}")
            return F3False
        if not isinstance(skey, str) and skey is not None:
            if error: raise TypeError(f"files.delete: The skey must be str or None. got {type(skey)}")
            return F3False
        skey = skey or None
        return F3Shell._F3BACKEND.delete(self._f3info, key, skey, error=error)

    def list(self, key: str = None, *, error=False) -> list | F3Bool:
        """
        列举目标文件夹下所有目标类型的文件的key。返回一个列表结果
        List all info of keys (In the target folder The key of a file of type). Returns a list result
        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
            * 如果不指定，则默认列举所有主键
            * 如果指定，则列举目标主键下的所有子键
            * key的类型错误时，会抛出异常或是返回F3False
        :param error:    bool  whether raise error.
        :return: list of keys|skeys, key的类型错误时，(且error=False)返回F3False
        """
        if not isinstance(key, str) and key is not None:
            if error: raise TypeError(f"files.list: The key must be str or None. got {type(key)}")
            return F3False
        key = key or None
        return self._F3BACKEND.list(self._f3info, key, error=error)

    def walk(self, *, error=False) -> typing.Iterable:
        """
        递归列举目标文件夹下所有目标类型的文件的key。返回一个迭代器结果
        Recursively list all info of keys (In the target folder The key of a file of type). Returns an iterator result
        :param error:    bool  whether raise error.
        :return: a iterator of (mkey:str, skey:str)
        """
        return self._F3BACKEND.walk(self._f3info)  # error=error

    def retype(self, new_type: str | tuple[str, str], *mkeys: str, overwrite: bool = False, error: bool = False) -> type(list) | F3Bool:
        """
        修改工作目录下的现有一些文件的后缀到新的后缀
        Modify the suffix of some existing files in the working directory to a new suffix
        :param new_type: 新的后缀格式。
            * 如果为tuple，则第一个元素为主键的新后缀，第二个元素为子键的新后缀
            * 如果new_type类型错误或是 tuple长度不为2，则会抛出异常或是返回F3False
        :param mkeys: 目标的主键，如果不指定，则默认全部文件
            * 不支持tuple[str, str]格式，此处只支持str
        :param overwrite: 是否覆盖已存在的文件
        :param error: bool  whether raise error.
        :return:
            failed list: 由于异常而未能成功retype的文件路径(error为False时)
        """
        faileds = []

        # check type
        if isinstance(new_type, tuple):
            if len(new_type) != 2:
                if error: raise TypeError(f"files.retype: The new_type must be tuple[str, str]. got new_type's length = {len(new_type)}")
                return F3False
            new_type, new_stype = new_type
        elif isinstance(new_type, str):
            new_stype = PF_DTYPE
        else:
            if error: raise TypeError(f"files.retype: The new_type must be str or tuple[str, str]. got {type(new_type)}")
            return F3False

        # body loop
        new_type = F3Info.NewType(new_type, new_stype)
        for k in key:
            # check k type
            if isinstance(k, tuple):
                if error: raise TypeError(f"files.retype: The mkey: tuple type is not supported in this function. got {k}")
                faileds.append(k)
                continue

            # body
            _path = self._f3info(k)
            dirname, basename = os.path.split(_path)
            fname, ftype = os.path.splitext(basename)
            _newpath = os.path.join(dirname, fname + new_type)

            # check old&new path
            if not os.path.exists(_path):
                if error: raise FileNotFoundError(f"files.retype: Target src path is not exists: {k}")
                err_list.append(k)
                continue
            if os.path.exists(_newpath) and not overwrite:
                if error: raise FileExistsError(f"files.retype: Target dst path is already exists: {k}. Please set overwrite=True")
                faileds.append(k)
                continue

            # move
            try:
                if os.path.isdir(_path):
                    shutil.move(_path, _newpath)

                    # 遍历修改其中的子键文件的后缀
                    for sfname in os.listdir(_newpath):
                        sname, stype = os.path.splitext(sfname)
                        if stype != new_stype:
                            shutil.move(os.path.join(_newpath, sfname), os.path.join(_newpath, sname + new_stype))
                else:
                    shutil.move(_path, _newpath)
            except Exception as err:
                if error: raise RetypeFailedError(f"files.retype: Retype {k}{self._f3info.type} failed. \n\tCaused error: {err}")
                faileds.append(k)

        return faileds

    def relink(self, new_scp: str, *keys: str | tuple[str, str], error=False) -> type(list) | F3Bool:
        """
        修改工作目录下的现有一些文件的源文件路径到新的路径
        * 该函数只与保存自定义对象有关
        * 例如对象A由F:\python_lib1\my_a.py定义，那么生成的f3bytes会指向该py文件
        * 如果将my_a.py移动到了F:\python_lib2\my_a.py，那么原来的f3bytes就会失效，此时就需要使用relink函数重新绑定
        * 如果目标对象是由site-packages下的包定义的，那么不需要使用relink函数。只要保证目标包存在即可
        :param new_scp: new source code path
            * new_scp指定的目标不存在时，返回F3False或是抛出异常
        :param keys: 指定的目标key, str or tuple[str, str]. 前者表示单个主键，后者表示主键和子键
            * 不指定则该函数不会执行任何操作
        :param error: bool  whether raise error.
        :return: failed list: error为False时，返回由于名称重复而未能成功relink的文件名(带原始后缀)
        """
        err_list = []

        # check type
        if not isinstance(new_scp, str):
            if error: raise TypeError(f"files.relink: The new_scp must be str. got {type(new_scp)}")
            return F3False

        # chec exists
        if not os.path.exists(new_scp):
            if error: raise FileNotFoundError(f"files.relink: The new_scp path is not exists: {new_scp}")
            return F3False

        # body loop
        for k in keys:
            # check k type
            if isinstance(k, tuple):
                k, skey = k
            else:
                skey = None

            # body
            _path = self._f3info(k, skey)
            if not os.path.exists(_path):
                if error: raise FileNotFoundError(f"files.relink: Target path is not exists: {k}")
                err_list.append(k)
                continue
            try:
                obj = self._F3BACKEND.get(self._f3info, k, _sys_relink=new_scp, error=True)
                self._F3BACKEND.set(self._f3info, k, obj, error=True)
            except Exception as err:
                if error: raise RelinkFailedError(f"files.relink: Relink {k}{self._f3info.type} failed. \n\tCaused error: {err}")
                err_list.append((k, err))
        return err_list

    def hash(self, key: str, skey: str = None, *, error=False) -> int:
        """
        获取目标的文件指纹
        :param key: 文件名称，类似数据库的主键，不能重复
        :param skey: sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error: bool  whether raise error.
        :return:
        """
        # check
        if not isinstance(key, str):
            if error: raise TypeError(f"files.hash: The key must be str. got {type(key)}")
            return F3False
        if not isinstance(skey, str) and skey is not None:
            if error: raise TypeError(f"files.hash: The skey must be str or None. got {type(skey)}")
            return F3False
        skey = skey or None

        # body
        _path = self._f3info(key, skey)
        if os.path.isdir(_path):
            return hash(self.pack(_path, error=error))
        return hash(open(_path, 'rb').read())


    @classmethod
    def dumps(cls, obj: object, *, error=True) -> f3bytes | F3Bool:
        """
        将python对象转换为f3格式的bytes
        :param obj: python对象, 但是不能是F3Bool
        :return: f3bytes, 失败返回F3False
        """
        # body
        try:
            return F3Core.dumps(obj)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def loads(cls, data: f3bytes, *, error=True) -> object | F3Bool:
        """
        将f3格式的bytes转换为python对象
        :param data: f3bytes
        :return: any, 失败返回F3False
        """
        # check
        if not isinstance(data, f3bytes):
            if error: raise TypeError(f"files.loads:'data' must be bytes. got {type(data)}")
            return F3False

        # body
        try:
            return F3Core.loads(data)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def pack(cls, path: str, *, mode=zipfile.ZIP_STORED, level=None, error=True) -> f3bytes | F3Bool:
        """
        将目标目录打包为f3bytes
        :param path: 目标文件或目录的路径
        :return: f3bytes, 失败返回F3False
            * 如果使用loads加载该返回值，将会得到一个zip_bytes对象(可以保存为zip文件的那种)
        """
        # check
        if not isinstance(path, str):
            if error: raise TypeError(f"files.pack:'path' must be str. got {type(path)}")
            return F3False

        # body
        try:
            s = packtarget(path, mode=mode, level=level)
            return F3Core.dumps(s)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def unpack(cls, data: f3bytes, path: str = None, *, error=True, overwrite: bool = False) -> F3Bool | zipfile.ZipFile:
        """
        解包f3bytes到目标目录或是返回ZipFile实例
        :param data: f3bytes格式的数据。
            * 如果目标data不是由pack函数生成的，将会导致解包失败异常
        :param path: '解压到...'的路径. 如果为None, 返回值为zipfile.ZipFile实例
        :param overwrite: bool, 是否覆盖已存在的文件(仅在path不为None时有效)
        :return: F3Bool|ZipFile
        """
        # checks
        if not isinstance(data, zip_bytes):
            if error: raise TypeError(f"files.unpack:'data' must be bytes. got {type(data)}")
            return F3False
        if path is not None and not isinstance(path, str):
            if error: raise TypeError(f"files.unpack:'path' must be str or None. got {type(path)}")
            return F3False

        # body
        try:
            s = F3Core.loads(data)
            res = unpacktarget(s, path, overwrite=overwrite)
            return res if path is None else F3True
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def bytes2py(cls, data: f3bytes, *, info:str=None, error=True) -> str|F3Bool:
        """
        将bytes数据转换为python代码
        :param data: bytes
        :param error: bool  whether raise error.
        :return: str|F3Bool, 失败返回F3False
        """
        if not isinstance(data, f3bytes):
            if error: raise TypeError(f"files.bytes2py:'data' must be bytes. got {type(data)}")
            return F3False
        if not isinstance(info, str) and info is not None:
            if error: raise TypeError(f"files.bytes2py:'info' must be str or None. got {type(info)}")
            return F3False
        info = info or ""
        try:
            return bytes2py(data, info=info)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def py2bytes(cls, code: str, *, error=True) -> f3bytes|F3Bool:
        """
        将python代码转换为bytes数据
        :param code: str 由bytes2py生成的python代码
        :param error: bool  whether raise error.
        :return: f3bytes|F3Bool, 失败返回F3False
        """
        if not isinstance(code, str):
            if error: raise TypeError(f"files.py2bytes:'code' must be str. got {type(code)}")
            return F3False
        try:
            return py2bytes(code)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def packpy(cls, path:str, *, mode=zipfile.ZIP_LZMA, level=9, error=True) -> str|F3Bool:
        """
        打包目标文件或目录到python代码
        :param path: str 目标文件或目录的路径
        :param error: bool  whether raise error.
        :return: str|F3Bool, 失败返回F3False
        """
        if not isinstance(path, str):
            if error: raise TypeError(f"files.packpy:'path' must be str. got {type(path)}")
            return F3False
        try:
            return packtargetpy(path, mode=mode, level=level)
        except Exception as err:
            if error: raise err
            return F3False

    @classmethod
    def unpackpy(cls, code:str, extract_path:str=None, overwrite=False, *, error=True) -> zipfile.ZipFile|None:
        """
        解压python代码到指定目录
        :param code: str 由packpy生成的python代码
            * 如果目标code不是由packpy函数生成的，可能会导致解包失败异常
        :param extract_path: str 解压到...的路径. 如果为None, 返回值为zipfile.ZipFile实例
        :param overwrite: bool 是否覆盖已存在的文件
        :param error: bool  whether raise error.
        :return: zipfile.ZipFile|None
        """
        if not isinstance(code, str):
            if error: raise TypeError(f"files.unpackpy:'code' must be str. got {type(code)}")
            return F3False
        try:
            return unpacktargetpy(code, extract_path, overwrite, error=error)
        except Exception as err:
            if error: raise err
            return F3False


    class prefab:
        @classmethod
        def testc(cls, cmd: str) -> bool:
            """
            测试命令是否存在，不显示输出。
            :param cmd: str
            :return: bool
            """
            if not isinstance(cmd, str):
                raise TypeError(f"files.testc:'cmd' must be str. got {type(cmd)}")

            return testc(cmd)

        @classmethod
        def aspy(cls, path: str, *, error=False, overwrite=False) -> F3Bool:
            """
            打包目标到同名.py文件
            * 不会覆盖目标，如果目标已存在，将抛出异常
            """
            path = os.path.abspath(path)
            dirnam, basename = os.path.split(path)
            fname, ftype = os.path.splitext(basename)
            _pypath = os.path.join(dirnam, fname + '.py')
            if os.path.exists(_pypath) and not overwrite:
                if error: raise FileExistsError(f"Target .py file already exists: {_pypath}")
                return F3False

            with open(_pypath, 'wb') as f:
                bs = F3Shell.pack(path, mode=zipfile.ZIP_LZMA, level=9, error=error)
                f.write(bs)
            return F3True

        @classmethod
        def astarget(cls, path: str, *, error=False, overwrite=False) -> F3Bool:
            """
            检测目标是否存在，如果不存在，则解压同名.py文件
            * 不会覆盖目标，如果目标已存在，将抛出异常
            """
            path = os.path.abspath(path)
            if os.path.exists(path) and not overwrite:
                return F3True
            dirname, basename = os.path.split(path)
            fname, ftype = os.path.splitext(basename)
            _pypath = os.path.join(dirname, fname + '.py')

            # check py file
            if not os.path.exists(_pypath):
                if error: raise FileNotFoundError(f"Target file not found: {_pypath}")
                return F3False

            with open(_pypath, 'rb') as f:
                bs = f.read()
                return F3Shell.unpack(bs, dirname, overwrite=overwrite, error=error)

    # nickname
    p = prefab

if __name__ == '__main__':
    ...
