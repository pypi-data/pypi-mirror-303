import inspect
import warnings
import random
import string
import win32api
import win32gui
import win32con

__doc__ = """
f3utils.py
~~~~~~~~~~

This module provides some useful functions and classes.


Functions
---------
create_frames_from_current(current_frame)
    # Create a frame list from the current frame.
get_top_target_file_path()
    # Get the top target file path.
memoize(func)
    # Cache the input and output of the function.
    
Classes
-------
F3Warning(Warning)
    # The warning class of files3.
Singleton(type)
    # The metaclass of files3.
"""

def create_random_name(length: int) -> str:
    """
    Create a random file name.
    :return:
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class F3Warning(Warning):
    ...


class Singleton(type):
    """
    Singleton 是一个元类，用于创建单例对象。
    使用方法是将其作为元类指定给需要实现单例的类。
    """

    def __init__(self, *args, **kwargs):
        # 初始化一个实例变量，用于存储单例对象
        self._instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        # 如果单例对象还未创建，就创建一个
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        # 返回单例对象
        return self._instance


def memoize(func):
    """
    memoize 是一个装饰器，用于缓存函数的输入和输出。
    它创建一个字典，用于存储函数的输入和对应的输出。
    当函数被调用时，它首先检查输入是否已经在字典中，
    如果是，就直接返回对应的输出，否则，就计算输出，
    并将输入和输出存储在字典中，然后返回输出。

    :Note: 假设函数的输入是可哈希的，如果你用它来装饰一个接受不可哈希输入（如列表或字典）的函数，那么它将无法正常工作。
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


def create_frames_from_current(current_frame):
    # 初始化帧列表，将当前帧添加到列表中
    frames = [current_frame]

    # 循环，直到没有更多的帧
    while True:
        # 获取当前帧的上一帧
        current_frame = current_frame.f_back

        # 如果上一帧存在
        if current_frame is not None:
            # 将上一帧添加到帧列表中
            frames.append(current_frame)
        else:
            # 如果上一帧不存在，就跳出循环
            break

    # 返回帧列表的逆序，即从最深的帧到最浅的帧
    return frames[::-1]


def get_top_target_file_path() -> str:
    # 获取当前的堆栈帧
    frame = inspect.currentframe()

    # 从当前帧创建一个帧列表，从最深的帧（索引0）到最浅的帧（索引-1）
    frames = create_frames_from_current(frame)

    # 初始化后备选择帧和可能的帧列表
    backend_select, possible_frames = frame, []

    # 遍历帧列表
    for frame in frames:
        # 获取帧的代码对象
        code = frame.f_code

        # 如果代码对象不存在或者文件名以'<'开头，就跳过当前循环
        if not code or code.co_filename.startswith('<'):
            continue

        # 更新后备选择帧
        backend_select = frame

        # 如果代码对象的名称（转换为小写）是'<module>'，就把当前帧添加到可能的帧列表中
        if code.co_name.lower() == '<module>':
            possible_frames.append(frame)

    # 如果可能的帧列表为空，就发出警告，并返回后备选择帧的文件名
    if not possible_frames:
        warnings.warn(
            F3Warning("Can not find the <module> with a filepath. Return the backend select instead. This may led to unexpected result."))
        return backend_select.f_code.co_filename

    # 返回可能的帧列表中最接近浅层的帧的文件名
    return possible_frames[-1].f_code.co_filename




if __name__ == '__main__':
    ...
