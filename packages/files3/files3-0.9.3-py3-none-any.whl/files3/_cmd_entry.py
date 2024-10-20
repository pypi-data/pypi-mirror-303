import argparse
import os
import subprocess
import sys
import ctypes
import tempfile
import time
import winreg
from files3.f3info import PF_DTYPE, F3Info
from files3.f3bool import F3Bool
from files3.f3shell import F3Shell as files


def _read_inst(_dir, _fname, _type):
    try:
        _f = files(_dir, _type)
    except Exception as err:
        print(f"Failed to create Files parser. -For {err}")
        return False

    _fullpath = os.path.join(_dir, _fname + _type)
    #print(_fullpath)
    if not os.path.exists(_fullpath):
        print(f"File:{_fname}{_type} not exists under:{_dir}.")
        return False

    # _ = _f.get(_fname)
    try:
        _ = _f.get(_fname)
    except Exception as err:
        print(f"Failed to load & parse target. -For {err}")
        return False

    if isinstance(_, F3Bool):
        print("File can't be a Files3File -For got the 'pfFalse'.")
        return False

    # 注入txt到临时目录
    with tempfile.NamedTemporaryFile('w+t', suffix='.txt', delete=False) as f:
        f.write(f'PythonInstance: {_fname}\n' + str(_))

    # open target
    path = os.path.abspath(f.name)
    os.system(f"start {path}")
    return True


# add cmd
_cmd_show_doc_ = """
show files3 data by txt browser
f3 [fname] 
f3 [fname] [type]
f3 [fname] -i [dir]
f3 [fname] [type] -i [dir]
@example:
    f3 a [.inst]  # default type is .inst | default dir is ''
    f3 a .obj
    # f3 a obj  # is error
    f3 a -i /datum
    f3 a .obj -i /datum
"""


def _cmd_show():
    """
    f3 [fname]
    f3 [fname] [ftype]
    f3 [fname] -i [dir]
    f3 [fname] [ftype] -i [dir]
    :return:
    """
    parser = argparse.ArgumentParser("Files3.CMDFilePreview")
    parser.add_argument('fname', help="Instance File's name", type=str)
    parser.add_argument('-t', '--type', help="Instance File's user-defined type. (like .XXX)", default=PF_DTYPE, type=str)
    parser.add_argument('-d', '--dir', help="Files3 entry's directory.", default="")
    try:
        args = parser.parse_args()
    except Exception as err:
        print(f"Failed to parse arguments. -For: {err}\n\n{_cmd_show_doc_}")
        return False
    # print("debug:", args)
    # get dir fname type
    return _read_inst(args.dir, args.fname, args.type)


_cmd_open_doc_ = """
open files3 data by txt browser
f3open [fpath]
@example:
    f3open /datum/a.inst
    f3open /datum/a.obj
    f3open /datum/a  # is error
"""


def _cmd_open():
    """
    f3open [fpath]
    :return:
    """
    # print(sys.argv)
    parser = argparse.ArgumentParser("Files3.CMDFileOpen")
    parser.add_argument('fpath', help="Instance File's path(like a/b/c.xxx)", type=str)
    try:
        args = parser.parse_args()
    except Exception as err:
        print(f"Failed to parse arguments. -For: {err}\n\n{_cmd_open_doc_}")
        return False

    try:
        dir, fname, ftype = F3Info.SplitPath(args.fpath)
    except Exception as err:
        print(f"Failed to locate File. -For: {err}\n\n{_cmd_open_doc_}")
        return False

    return _read_inst(dir, fname, ftype)


_cmd_assoc_doc_ = """
assoc specific file type to f3open
f3assoc [ftype]
@example:
    f3assoc .inst
    f3assoc .obj
    f3assoc .inst .obj  # is error
*Program will provide you the .exepath in anycase. If it is not effect, please assoc .exepath with your file type by hand.
"""


def _cmd_assoc():
    """
    f3assoc [ftype]
    目前确定的注册表位置:
        计算机/HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
            {EXTENSION}下创建 默认value = {PROG_ID}|(REG_SZ):str
            {EXTENSION}/OpenWithProgids下创建 默认value  = {BACKEND_PROG_ID}|(REG_SZ):str  # 可选
        *计算机/HKEY_CURRENT_USER/Software/Classes/{EXTENSION}/OpenWithProgids  # same as HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
        计算机/HKEY_CLASSES_ROOT/{PROG_ID}/shell/open/command
            {PROG_ID}下创建 默认value = {Description}|(REG_SZ):str
            {PROG_ID}/DefaultIcon下创建 默认value = {abs_exepath},0|(REG_SZ):str
            {PROG_ID}/shell下不创建value
            {PROG_ID}/shell/open下不创建value
            {PROG_ID}/shell/open/command下创建 默认value = "{abs_exepath}" "%1"|(REG_SZ):str
        *计算机/HKEY_CURRENT_USER/Software/Classes/{PROG_ID}/shell/open/command  # same as HKEY_CLASSES_ROOT/{PROG_ID}/shell/open/command
        # ApplicationAssociationToasts 是一个 Windows 注册表项，它的作用是存储用户对文件关联的选择和偏好。
        计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/ApplicationAssociationToasts下创建特定value:
            {PROG_ID}_{EXTENSION} = 0|(REG_DWORD):int
        计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/Explorer/FileExts/{EXTENSION}/OpenWithProgids
            {EXTENSION}下创建 默认value = |(REG_SZ):str  # 空的
            {EXTENSION}/OpenWithProgids下创建特定value: {PROG_ID} = |(REG_NONE):?  # 空的
    至此, 完成了文件类型的注册和关联
    因此,需要的参数有:
    EXTENSION, PROG_ID, Description, abs_exepath
    :return:
    """
    raw_argv = sys.argv
    # 检查admin权限
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("CMD is not admin. Do you want next? (y/n) (Modify registry need admin permission)")
        _ = input()
        if _.lower() == "y":
            _ = ctypes.windll.shell32.ShellExecuteW(None, "runas", raw_argv[0], " ".join(raw_argv[1:]), None, 1)
            if _ <= 32:
                print("Failed to run as admin. -For: ShellExecuteW return code is {}".format(_))
            else:
                print("Finished.")
        else:
            print("Canceled.")
        return False

    parser = argparse.ArgumentParser("Files3.CMDAssoc")
    parser.add_argument('ftype', help="Instance File's custom ftype(like .xxx)", type=str)
    try:
        args = parser.parse_args()
        _try = args.ftype  # try to get ftype
    except Exception as err:
        print(f"Failed to parse arguments. -For: {err}\n\n{_cmd_assoc_doc_}")
        return False

    py_exe = sys.executable
    # f3open(under Scripts)
    f3open_exe = os.path.join(os.path.dirname(py_exe), "Scripts", "f3open.exe")
    # Check
    if not os.path.exists(f3open_exe):
        print(f"Failed to locate f3open.exe. -For: {f3open_exe} is not exists")
        return False

    # check extension(whether start with .)
    if not args.ftype.startswith("."):
        print(f"Failed to parse arguments. -For: {args.ftype} is not start with '.'")
        return False

    Description = f"Python Instance"  # Description
    PROG_ID = f"Files3.{args.ftype[1:]}_File"
    EXTENSION = args.ftype
    abs_exepath = os.path.abspath(f3open_exe)
    print(f"Program f3open.exe: {abs_exepath}")



    # HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
    # {EXTENSION}下创建 默认value = {PROG_ID}|(REG_SZ):str
    # {EXTENSION}/OpenWithProgids下创建 默认value  = {BACKEND_PROG_ID}|(REG_SZ):str  # 可选(这里暂选空)
    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, EXTENSION) as key:
        winreg.SetValue(key, "", winreg.REG_SZ, PROG_ID)
        with winreg.CreateKey(key, "OpenWithProgids") as subkey:
            ...

    # *计算机/HKEY_CURRENT_USER/Software/Classes/{EXTENSION}/OpenWithProgids  # same as HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Classes\\{EXTENSION}") as key:
        winreg.SetValue(key, "", winreg.REG_SZ, PROG_ID)
        with winreg.CreateKey(key, "OpenWithProgids") as subkey:
            ...

    # HKEY_CLASSES_ROOT/{PROG_ID}/shell/open/command
    # {PROG_ID}下创建 默认value = {Description}|(REG_SZ):str
    # {PROG_ID}/DefaultIcon下创建 默认value = {abs_exepath},0|(REG_SZ):str
    # {PROG_ID}/shell下不创建value
    # {PROG_ID}/shell/open下不创建value
    # {PROG_ID}/shell/open/command下创建 默认value = "{abs_exepath}" "%1"|(REG_SZ):str
    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, PROG_ID) as key:
        winreg.SetValue(key, "", winreg.REG_SZ, Description)
        with winreg.CreateKey(key, "DefaultIcon") as subkey:
            winreg.SetValue(subkey, "", winreg.REG_SZ, f"{abs_exepath},0")
        with winreg.CreateKey(key, "shell") as subkey:
            with winreg.CreateKey(subkey, "open") as subsubkey:
                with winreg.CreateKey(subsubkey, "command") as subsubsubkey:
                    winreg.SetValue(subsubsubkey, "", winreg.REG_SZ, f'"{abs_exepath}" "%1"')

    # *计算机/HKEY_CURRENT_USER/Software/Classes/{PROG_ID}/shell/open/command  # same as HKEY_CLASSES_ROOT/{PROG_ID}/shell/open/command
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Classes\\{PROG_ID}") as key:
        winreg.SetValue(key, "", winreg.REG_SZ, Description)
        with winreg.CreateKey(key, "DefaultIcon") as subkey:
            winreg.SetValue(subkey, "", winreg.REG_SZ, f"{abs_exepath},0")
        with winreg.CreateKey(key, "shell") as subkey:
            with winreg.CreateKey(subkey, "open") as subsubkey:
                with winreg.CreateKey(subsubkey, "command") as subsubsubkey:
                    winreg.SetValue(subsubsubkey, "", winreg.REG_SZ, f'"{abs_exepath}" "%1"')

    # ApplicationAssociationToasts 是一个 Windows 注册表项，它的作用是存储用户对文件关联的选择和偏好。
    # 计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/ApplicationAssociationToasts下创建特定value:
    # {PROG_ID}_{EXTENSION} = 0|(REG_DWORD):int
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Microsoft\\Windows\\CurrentVersion\\ApplicationAssociationToasts") as key:
        winreg.SetValueEx(key, f"{PROG_ID}_{EXTENSION}", 0, winreg.REG_DWORD, 0)

    # 计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/Explorer/FileExts/{EXTENSION}/OpenWithProgids
    # {EXTENSION}下创建 默认value = |(REG_SZ):str  # 空的
    # {EXTENSION}/OpenWithProgids下创建特定value: {PROG_ID} = |(REG_NONE):?  # 空的
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\{EXTENSION}") as key:
        winreg.SetValue(key, "", winreg.REG_SZ, "")
        with winreg.CreateKey(key, "OpenWithProgids") as subkey:
            ...

    # 创建一个 REG_NONE 类型的项
    subprocess.run(
        ['reg', 'add', f'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\{EXTENSION}\\OpenWithProgids', '/v', PROG_ID,
         '/t', 'REG_NONE', '/d', '', '/f'])

    print(f"Success to assoc {EXTENSION} to {abs_exepath}")
    return True


def _cmd_unassoc():
    """
    取消关联
    f3unassoc [ftype]
    :return:
    """
    parser = argparse.ArgumentParser("Files3.CMDUnAssoc")
    parser.add_argument('ftype', help="Instance File's custom ftype(like .xxx)", type=str)
    try:
        args = parser.parse_args()
        _try = args.ftype  # try to get ftype
    except Exception as err:
        print(f"Failed to parse arguments. -For: {err}\n\n{_cmd_assoc_doc_}")
        return False

    # check extension(whether start with .)
    if not args.ftype.startswith("."):
        print(f"Failed to parse arguments. -For: {args.ftype} is not start with '.'")
        return False

    PROG_ID = f"Files3.{args.ftype[1:]}_File"
    EXTENSION = args.ftype

    # 检查admin权限
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Failed to unassoc. -For: Please run this program as administrator.(Modify registry need admin permission)")
        return False

    # HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
    # {EXTENSION}下创建 默认value = {PROG_ID}|(REG_SZ):str
    # {EXTENSION}/OpenWithProgids下创建 默认value  = {BACKEND_PROG_ID}|(REG_SZ):str  # 可选(这里暂选空)
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, EXTENSION)
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    # *计算机/HKEY_CURRENT_USER/Software/Classes/{EXTENSION}/OpenWithProgids  # same as HKEY_CLASSES_ROOT/{EXTENSION}/OpenWithProgids
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"Software\\Classes\\{EXTENSION}")
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    # HKEY_CLASSES_ROOT下尝试删除PROG_ID
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, PROG_ID)
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    # *计算机/HKEY_CURRENT_USER/Software/Classes/{PROG_ID}/shell/open/command  # same as HKEY_CLASSES_ROOT/{PROG_ID}/shell/open/command
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"Software\\Classes\\{PROG_ID}")
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    # ApplicationAssociationToasts 是一个 Windows 注册表项，它的作用是存储用户对文件关联的选择和偏好。
    # 计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/ApplicationAssociationToasts中移除特定value:
    # {PROG_ID}_{EXTENSION}
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Microsoft\\Windows\\CurrentVersion\\ApplicationAssociationToasts") as key:
            winreg.DeleteValue(key, f"{PROG_ID}_{EXTENSION}")
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    # 计算机/HKEY_CURRENT_USER/Software/Microsoft/Windows/CurrentVersion/Explorer/FileExts下尝试删除EXTENSION
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\{EXTENSION}")
    except Exception as err:
        print(f"Failed to unassoc {EXTENSION} to {PROG_ID}. -For: {err}")
        return False

    print(f"Success to unassoc {EXTENSION} to {PROG_ID}")
    return True


if __name__ == '__main__':
    sys.argv = ['f3open', r"C:\Users\Administrator\Desktop\test\a.inst"]
    _cmd_open()
