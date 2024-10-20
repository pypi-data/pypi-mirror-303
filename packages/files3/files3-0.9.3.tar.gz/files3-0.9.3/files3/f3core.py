import os.path
import shutil
import pickle
import typing

from files3.f3utils import *
from files3.f3info import *
from files3.f3bool import *
from files3.f3io import *


class FolderCreateError(Exception): ...

class FileMoveError(Exception): ...

class FileRenameError(Exception): ...


class F3Core(metaclass=Singleton):
    f3seg = F3SegmentTail()
    def has(self, info: F3Info, key: str, skey:str=None) -> F3Bool:
        """
        Has a pyfile file exists. Returns True successfully, or False if the target file doesnot exists

        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated

        """
        _path = info(key, skey)
        if os.path.exists(_path): return F3True
        return F3False

    def set(self, info:F3Info, key: str, pyobject: object, skey:str=None, *, error:bool=False, _sys_relink=None) -> F3Bool:
        """
        Set a new pyfile file. Returns True successfully

        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param pyobject: python对象   python object
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool Whether raise General Exception.
        """
        _path = info(key)
        if skey is not None:
            if os.path.isfile(_path):  # 已有文件，需要转换为文件夹
                rname = create_random_name(16)
                # create folder
                dirname = os.path.dirname(_path)
                basename = os.path.basename(_path)
                folder = os.path.join(dirname, rname)
                try:
                    os.mkdir(folder)
                except:
                    if error: raise FolderCreateError(f"Can not create folder: {folder}")
                    return F3False

                # move file to folder
                try:
                    os.rename(_path, os.path.join(folder, '_' + info.stype))
                except:
                    if error: raise FileMoveError(f"Can not move file to folder: {folder}")
                    return F3False

                # rename folder
                try:
                    os.rename(folder, os.path.join(dirname, basename))
                except:
                    if error: raise FileRenameError(f"Can not rename folder: {folder}")
                    return F3False

            elif not os.path.exists(_path):
                try:
                    os.mkdir(_path)
                except:
                    if error: raise FolderCreateError(f"Can not create folder: {_path}")
                    return F3False

                # set to None
                s = f3dumps(None)
                open(os.path.join(_path, '_' + info.stype), "wb").write(s)

            # set to sub key
            _path = info(key, skey)
        elif os.path.isdir(_path):
            _path = info(key, '_')

        # body
        try:
            s = f3dumps(pyobject, relink_path=_sys_relink)
            open(_path, "wb").write(s)
            return F3True
        except Exception as err:
            if isinstance(err, CannotSaveError) or error: raise err
            if isinstance(err, TypeError) and str(err).find("pickle 'module'") != -1:
                raise err
            if isinstance(err, AttributeError) and str(err).startswith("pickle local") != -1:
                raise err
            if isinstance(err, pickle.PickleError):
                raise err
            return F3False

    def delete(self, info:F3Info, key: str, skey:str=None, *, error=False) -> F3Bool:
        """
        Delete pyfile file. Returns True if the target file is successful or does not exist. Returns False if the target file exists and cannot be deleted

        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        """
        _path = info(key, skey)
        if not os.path.exists(_path): return F3True
        try:
            if os.path.isdir(_path):
                shutil.rmtree(_path)
            else:
                os.remove(_path)
            return F3True
        except:
            if error: raise OSError(f"Can not delete target file: {_path}")
            return F3False

    def get(self, info:F3Info, key: str, skey:str=None, *, error:bool=False, _sys_relink=None) -> object:
        """
        增删改查之'查'。成功返回读取到的pyobject，如果目标文件不存在，则返回F3False
        Find data files. The read pyobject is returned successfully. If the target file does not exist, false is returned

        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        :param skey:     sub key, 如果启用了子键，则会将主键目标视作文件夹
        :param error:    bool Whether raise General Exception.
        """
        _path = info(key)
        if skey is not None:
            if os.path.isfile(_path):
                if error: raise TypeError(f"Target file is not a folder: {_path}. When skey = {skey}")
                return F3False
            _path = info(key, skey)
        elif os.path.isdir(_path):
            _path = info(key, '_')

        if not os.path.exists(_path): return F3False
        try:
            s = open(_path, 'rb').read()
            return f3loads(s, relink_path=_sys_relink)
        except Exception as err:
            if isinstance(err, ModuleNotFoundError) or error: raise err
            if isinstance(err, pickle.PickleError):
                raise err
            return F3False
    
    def list(self, info:F3Info, key:str=None, *, error=False) -> list:
        """
        列举目标文件夹下所有目标类型的文件的key。返回一个列表结果
        List all info of keys (In the target folder The key of a file of type). Returns a list result
        :param info:     F3Info inst
        :param key:      文件名称，类似数据库的主键，不能重复
                         File name. It is similar to the primary key of a database and cannot be duplicated
        """
        names = []
        _path = info.path if key is None else info(key)
        if not os.path.exists(_path):
            if error: raise FileNotFoundError(f"Can not find target file: {_path}")
            return names
        if key is None:
            for fnametype in os.listdir(_path):
                if os.path.isfile(os.path.join(_path, fnametype)):
                    fname, type = os.path.splitext(fnametype)
                    if type.lower() == info.type:
                        names.append(fname)
        else:
            for fnametype in os.listdir(_path):
                if os.path.exists(os.path.join(_path, fnametype)):
                    fname, type = os.path.splitext(fnametype)
                    if type.lower() == info.stype:
                        if key is not None and fname == '_':
                            continue
                        names.append(fname)

        # When yield reach return, will cause StopIteration to stop iter.
        # In general case, return the list
        return names

    def iter(self, info:F3Info) -> typing.Iterable:
        for fnametype in os.listdir(info.path):
            if os.path.isfile(os.path.join(info.path, fnametype)):
                fname, type = os.path.splitext(fnametype)
                if type.lower() == info.type:
                    yield fname


    def walk(self, info:F3Info) -> typing.Iterable:
        for fnametype in os.listdir(info.path):
            fullpath = os.path.join(info.path, fnametype)
            fname, type = os.path.splitext(fnametype)
            if type.lower() != info.type:
                continue
            yield fname, ''
            if os.path.isdir(fullpath):
                for sfnametype in os.listdir(fullpath):
                    sfullpath = os.path.join(fullpath, sfnametype)
                    sfname, stype = os.path.splitext(sfnametype)
                    if stype.lower() == info.stype and sfname != '_':
                        yield fname, sfname

    @staticmethod
    def dumps(pyobject: object, *, error=True) -> bytes:
        """
        将python对象转换为二进制数据
        Convert python object to binary data
        """
        try:
            return f3dumps(pyobject)
        except Exception as err:
            if isinstance(err, CannotSaveError) and error: raise err
            if isinstance(err, TypeError) and str(err).find("pickle 'module'") != -1 and error:
                raise err
            if isinstance(err, AttributeError) and str(err).startswith("pickle local") != -1 and error:
                raise err
            if isinstance(err, pickle.PickleError) and error:
                raise err
            return F3False

    @staticmethod
    def loads(s: bytes, *, error=True) -> object:
        """
        将二进制数据转换为python对象
        Convert binary data to python object
        """
        try:
            return f3loads(s)
        except Exception as err:
            if isinstance(err, ModuleNotFoundError) and error: raise err
            if isinstance(err, pickle.PickleError) and error:
                raise err
            if error:
                raise err
            return F3False

