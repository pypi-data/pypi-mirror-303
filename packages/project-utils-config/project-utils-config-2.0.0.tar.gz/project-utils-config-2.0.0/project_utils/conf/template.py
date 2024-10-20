import os

from pathlib import Path
from loguru import logger
from typing import Optional
from loguru._logger import Logger
from configparser import ConfigParser
from abc import ABCMeta, abstractmethod

from ._base_config import BaseConfig, BaseSystem


class ConfigTemplate(metaclass=ABCMeta):
    base_type: str = "BASE"
    system_field: str = "SYSTEM"
    system_class: BaseSystem = BaseSystem

    __log_app: Logger = logger
    __instance__: Optional = None
    __base_config: BaseConfig = BaseConfig()

    __parser: ConfigParser
    __system: system_class

    def __parser_init(self, config_path: str, encoding: str = "utf-8"):
        parser: ConfigParser = ConfigParser()
        parser.read(config_path, encoding=encoding)
        return parser

    def __init_config(self, base_url: str):
        self.__base_config.load_path(base_url, **self.__parser[self.base_type])
        self.__system = self.system_class(**self.__parser[self.system_field])

    def __init_log(self, rotation: str = "1 hours", retention: str = "3 days", encoding: str = "utf-8"):
        log_url: str = self.config_object.base_config.log_url
        log_name: str = "log_{time:%Y%m%d%H}.log"
        log_path: str = os.path.join(log_url, log_name)
        self.__log_app.add(log_path, rotation=rotation, retention=retention, encoding=encoding)

    def elasticsearch_init(self):
        ...

    def __init__(self, base_url: str, config_path: str, encoding: str = "utf-8", rotation: str = "1 hours",
                 retention: str = "3 days"):
        self.__parser = self.__parser_init(config_path, encoding)
        self.__init_config(base_url)
        self.__init_log(rotation=rotation, retention=retention, encoding=encoding)
        self.config_init()
        self.elasticsearch_init()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    @classmethod
    def create_config(
            cls,
            base_path: str = __file__,
            config_url: str = "config/config.ini",
            encoding: str = "utf-8",
            rotation: str = "1 hours",
            retention: str = "3 days"
    ):
        base_url: str = Path(base_path).parent.parent.parent.__str__()
        config_path: str = os.path.join(base_url, config_url)
        return cls(base_url, config_path, encoding, rotation, retention)

    @abstractmethod
    def config_init(self):
        ...

    @property
    def parser(self):
        return self.__parser

    @property
    def config_object(self):
        return self.__base_config

    @property
    def log_app(self):
        return self.__log_app

    @property
    def system(self):
        return self.__system

    @property
    def printf(self):
        return self.__log_app

    @property
    def printl(self):
        return self.__log_app
