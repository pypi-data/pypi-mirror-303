# -*- coding:utf-8 -*-
import re
import random
import string
import time
import datetime
from types import FunctionType
import inspect
import os
import io
import sys
from typing import IO, Iterable
from .log import warn


def isBase64(content: str) -> bool:
    _reg = "^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$"
    group = re.match(_reg, content)
    if group != None:
        return True
    return False


def debug():
    frameList = inspect.stack()
    sss = ["{}:{} ->{}".format(i.filename, i.lineno, i.function) for i in frameList]
    print(len(frameList))
    warn('\n' + '\n'.join(sss))


def getRandomStr(length: int, scope: str = string.ascii_letters+string.digits) -> str:
    return ''.join(random.sample(scope, length))


def generate_id(*_):
    return time.time_ns()


def getDateFolder(format: str = "%Y/%m/%d"):
    """
    获得当前日期目录:
    2023/12/01
    """
    time = datetime.datetime.now()
    return f"{time.strftime(format)}"


def isCallable(func):
    return isinstance(func, FunctionType)
    return callable(func)  # 返回true 也不一定能调用成功/返回失败一定调用失败
    return type(func) is FunctionType
    return hasattr(func, "__call__")


def is_async(func):
    """
    方法是否是异步的
    """
    return inspect.iscoroutinefunction(func) or inspect.isasyncgenfunction(func)


def getWorkDirectory():
    """
    获取工作目录
    """
    current_directory = os.getcwd()
    return current_directory


def find_files(root, filterDirFunction, filterFileFunction, *ignoreDirs: str):
    """
    root: 根目录
    filterDirFunction   返回bool的方法,参数 文件夹名
    filterFileFunction  返回bool的方法,参数 文件名
                       可以使用  lambda f:f.endswith(extension)
    RETURN  root  fdirs, ffile

    查找文件或文件夹
    os.path.join(root, file)

    """
    for root, dirs, files in os.walk(root):
        for ignore in ignoreDirs:
            if ignore in dirs:
                dirs.remove(ignore)
        fdirs = list(filter(filterDirFunction, dirs)
                     ) if filterDirFunction != None else dirs
        ffile = list(filter(filterFileFunction, files)
                     ) if filterFileFunction != None else files
        yield root, fdirs, ffile


def get_parent_dir(path: str, rank: int = 1):
    """
    获取上级目录
    """
    result: str = path
    stop = rank+1
    for _ in range(1, stop):
        result = os.path.dirname(result)
    return result


def getApplcationPath(__file__):
    # print("如果脚本被编译成.pyc文件运行或者使用了一些打包工具（如PyInstaller），那么__file__可能不会返回源.py文件的路径，而是编译后的文件或临时文件的路径")
    # 获取当前文件的完整路径
    if getattr(sys, 'frozen', False):
        # 如果应用程序是冻结的，获取可执行文件的路径
        application_path = os.path.dirname(sys.executable)
    else:
        # 否则，获取原始脚本的路径
        application_path = os.path.dirname(os.path.abspath(__file__))

    return application_path


def read_stream(stream: IO[bytes], size: int = -1) -> Iterable[bytes]:
    while True:
        chunk = stream.read(size)
        if not chunk:
            break
        yield chunk


async def write_stream(input: IO[bytes], outputStream: IO[bytes]):
    for chunk in read_stream(input, size=io.DEFAULT_BUFFER_SIZE):
        try:
            # print("**FF读数据", len(chunk))
            outputStream.write(chunk)
            outputStream.flush()
            # print("**输出到stdin*****",len(chunk))
        except Exception as e:
            pass
            # print("**FF异常", e, len(chunk))
    outputStream.close()
