import os

from typing import Optional


class PathConfig:
    # 单例模式
    __instance__: Optional = None
    __base_url: str
    # 数据目录
    __data_url: Optional[str] = None
    # 日志目录
    __log_url: Optional[str] = None
    # 输出目录
    __output_url: Optional[str] = None
    # 临时目录
    __tmp_url: Optional[str] = None
    # 测试目录
    __test_url: Optional[str] = None

    def __init__(self, base_url: str, **kwargs):
        self.__base_url = base_url
        if "data_url" in kwargs: self.__data_url = os.path.join(base_url, kwargs['data_url'])
        if "log_url" in kwargs: self.__log_url = os.path.join(base_url, kwargs['log_url'])
        if "output_url" in kwargs: self.__output_url = os.path.join(base_url, kwargs['output_url'])
        if "tmp_url" in kwargs: self.__tmp_url = os.path.join(base_url, kwargs['tmp_url'])
        if "test_url" in kwargs: self.__test_url = os.path.join(base_url, kwargs['test_url'])

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    @property
    def base_url(self):
        return self.__base_url

    def __path_wrapper(self, path: str):
        if path and not os.path.exists(path):
            os.mkdir(path)
        return path

    @property
    def data_url(self):
        return self.__path_wrapper(self.__data_url)

    @property
    def log_url(self):
        return self.__path_wrapper(self.__log_url)

    @property
    def output_url(self):
        return self.__path_wrapper(self.__output_url)

    @property
    def tmp_url(self):
        return self.__path_wrapper(self.__tmp_url)

    @property
    def test_url(self):
        return self.__path_wrapper(self.__test_url)


if __name__ == '__main__':
    path = PathConfig("/Users/mylx2014/Project/mylx2014/new-utils/new-utils-config",
                      data_url="data",
                      log_url="logs",
                      output_url="output",
                      tmp_url="tmp",
                      test_url="test"
                      )
    print(path.data_url)
    print(path.log_url)
    print(path.output_url)
    print(path.tmp_url)
    print(path.test_url)
