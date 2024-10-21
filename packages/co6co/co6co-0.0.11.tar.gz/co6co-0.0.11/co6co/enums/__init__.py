from enum import Enum, unique
# from abc import ABC, abstractclassmethod  抽象
from typing import List, Dict

from co6co import T


@unique  # 帮助检查 保证没有重复值
class Base_Enum  (Enum):
    """
    枚举[key, val]
    """
    key: T
    val: T

    def __new__(cls, key: T, value: T):
        obj = object.__new__(cls)
        obj.key = key
        obj.val = value  # value 为元组 (en_name,cn_name,val)
        return obj

    @classmethod
    def to_dict_list(cls) -> List[Dict]:
        status = [{'uid': i.name, 'key': i.key, 'value': i.val} for i in cls]
        return status 
    
    @classmethod
    def key2enum(cls, key):
        """
        key 转枚举 
        """
        for i in cls:
            if i.key==key:return i
        return None
    
    @classmethod
    def val2enum(cls, value):
        """
        val 转枚举 
        """
        for i in cls:
            if i.val==value:return i
        return None
    
    @classmethod
    def value_of(cls, value):
        """
        枚举的字符串 转枚举
        demo(Base_Enum):
            chanel="ch",1
        字符串 为 chanel 
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")

    def getValue(self) -> T:
        return self.val

    def getKey(self) -> T:
        return self.key


@unique
class Base_EC_Enum(Enum):
    """
    枚举[key:英文 ,name:中文 ,val:数字] 
    """
    key: T
    label: T
    val: T

    def __new__(cls, key: T, label: T, value: T):
        obj = object.__new__(cls)
        obj.key = key
        obj.label = label
        obj.val = value  # value 为元组 (en_name,cn_name,val)
        return obj

    @classmethod
    def to_dict_list(cls) -> List[Dict]:
        status = [{'uid': i.name, "key": i.key,
                   'label': i.label, 'value': i.val} for i in cls]
        return status

    def getValue(self) -> T:
        return self.val

    def getKey(self) -> T:
        return self.key

    def getLabel(self) -> T:
        return self.label
