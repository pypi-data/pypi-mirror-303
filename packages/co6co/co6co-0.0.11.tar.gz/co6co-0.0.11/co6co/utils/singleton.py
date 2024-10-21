
from __future__ import annotations
from datetime import datetime
from typing import Type, TypeVar

T = TypeVar('T')


class Singleton:
    """
    单例模式
    //todo 子类继承后怎么返回资料对象
    """
    _instance: T = None
    createTime = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.createTime = datetime.now()
        pass
