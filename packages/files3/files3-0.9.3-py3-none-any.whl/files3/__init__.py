import os
import re
import sys
import time

# 内核工具                            backend
from files3.f3core import F3Core
from files3.f3bool import F3Bool, F3True, F3False
from files3.f3info import PF_DTYPE as _PF_DTYPE
from zipfile import ZIP_STORED, ZIP_DEFLATED, ZIP_LZMA, ZIP_BZIP2
from files3._cmd_entry import _cmd_open, _cmd_show, _cmd_assoc, _cmd_unassoc

# 加壳工具(主要用于用户交互)           shell tool(user frendly API)
from files3.f3shell import F3Shell

# 测试工具                            test tool
from files3.f3test import QuickTest as F3QuickTest, AdvancedTest as F3AdvancedTest

# 别名                                default
files = F3Shell
f3 = files

# 别名                                default
prefab = F3Shell.prefab
f3p = prefab

__version__ = '0.9.x'

# f3 [fname]
# f3 [fname] [ftype]
# f3 [fname] -i [dir]
# f3 [fname] [ftype] -i [dir]
def cmd_show():
    if not _cmd_show():
        os.system("pause")

# f3open [fpath]
def cmd_open():
    if not _cmd_open():
        os.system("pause")

# f3assoc [ftype]  # ftype带有·
def cmd_assoc():
    if not _cmd_assoc():
        os.system("pause")

# f3unassoc [ftype]  # ftype带有·
def cmd_unassoc():
    if not _cmd_unassoc():
        os.system("pause")

def f3test():
    """
    Test function
    :return:
    """
    while True:
        choice = input("What do you wanto try? (input number)\n\t1. Quick Test\n\t2. General Test\n\t3. Advanced Test\n\t0. Finish\n")
        if int(choice) == 1:
            result = F3QuickTest()
            print(result)
        elif int(choice) == 2:
            f = files(os.getcwd())  # Choose path to manage *.inst

            ## write
            f.set('a', 1)
            # f.a = 1
            # f['a'] = 1

            ## read
            print('a:', f.get('a'))
            # print(f.a)
            # print(f['a'])

            ## delete
            # f.delete('a')
            # del f.a
            # del f['a']

            ### Special
            f['b', 'c'] = 10  # Set multiple files to a same value
            print("all:", f[...])

            print("\nF3Inst:")
            for k in f:
                print(f"{k}: {f[k]}")

        elif int(choice) == 3:
            result = F3AdvancedTest()
            print(result)
        else:
            break

        # Remove all
        f = files()
        del f[...]

        print('----------- ' * 4)


if __name__ == '__main__':
    f3test()

