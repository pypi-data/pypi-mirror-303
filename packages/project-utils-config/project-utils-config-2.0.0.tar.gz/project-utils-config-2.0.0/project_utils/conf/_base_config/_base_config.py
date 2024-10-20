from typing import Optional

from .._path_config import Path
from .._service_config import Service, ElasticSearch, Faiss, FTP, Graph


class BaseConfig:
    __instance__: Optional = None
    __base_config: Path
    __http_config: Service
    __es_config: ElasticSearch
    __faiss_config: Faiss
    __ftp_config: FTP
    __graph_config: Graph

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def load_path(self, base_url: str, **kwargs):
        self.__base_config = Path(base_url, **kwargs)

    def load_service(self, *args, **kwargs):
        self.__http_config = Service(*args, **kwargs)

    def load_elasticsearch(self, *args, **kwargs):
        self.__es_config = ElasticSearch(*args, **kwargs)

    def load_faiss(self, *args, **kwargs):
        self.__faiss_config = Faiss(*args, **kwargs)

    def load_ftp(self, *args, **kwargs):
        self.__ftp_config = FTP(*args, **kwargs)

    def load_graph(self, *args, **kwargs):
        self.__graph_config = Graph(*args, **kwargs)

    @property
    def base_config(self):
        return self.__base_config

    @property
    def service(self):
        return self.__http_config

    @property
    def es_config(self):
        return self.__es_config

    @property
    def faiss_config(self):
        return self.__faiss_config

    @property
    def ftp_config(self):
        return self.__ftp_config

    @property
    def graph_config(self):
        return self.__graph_config