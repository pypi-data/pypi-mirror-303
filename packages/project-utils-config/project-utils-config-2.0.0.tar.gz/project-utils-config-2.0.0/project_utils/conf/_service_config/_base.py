from abc import ABCMeta
from typing import Optional

from project_utils.exception import ServiceConfigException


class BaseServiceConfig(metaclass=ABCMeta):
    # 单例模式
    __instance__: Optional = None
    # 主机名
    __host: str
    # 端口
    __port: int
    # 是否开启 ssl 协议
    __ssl: bool

    def __init__(self, host: str, port: str, ssl: Optional[str] = None):
        assert port.isdigit(), ServiceConfigException("Params port value type require is number,not other type!",
                                                      __file__, trace_line=11)
        self.__host = host
        self.__port = int(port)
        self.__ssl = not not ssl

    @classmethod
    def create_instance(cls):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @property
    def ssl(self):
        return self.__ssl

    def to_url(self, index: Optional[str] = None, path: Optional[str] = None, query_params: Optional[dict] = None):
        result: list = []
        if self.__port == 80 or self.__port == 443:
            result.append("http" if self.port == 80 else "https")
        elif self.__ssl:
            result.append("https")
        else:
            result.append("http")
        result.append(self.__host)
        base_url: str = f"{result[0]}://{result[1]}"
        if self.port != 80 and self.port != 443:
            base_url += f":{self.port}"
        if index:
            base_url += f"/{index.strip('/')}"
        if path:
            base_url += f"/{path.strip('/')}"
        if query_params:
            base_url += "?"
            for key, val in query_params.items():
                base_url += f"{key}={val}&"
            base_url.strip("&")
        return base_url

    def to_dict(self):
        return {
            "host": str(self.__host),
            "port": str(self.__port),
        }
