from abc import ABCMeta
from typing import Optional


class BaseSystem(metaclass=ABCMeta):
    __instance__: Optional = None
    __debug: bool

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self, debug: Optional[str] = None):
        self.__debug = not not debug

    @property
    def debug(self):
        return self.__debug
