from aiohttp import BasicAuth
from typing import Optional, Union
from abc import ABC, abstractmethod
from requests.auth import HTTPBasicAuth

from ._utils import OperationUtils
from .._base import ElasticSearch, BaseElasticSearch


class BaseElasticSearchOperation(BaseElasticSearch, ABC):
    utils: OperationUtils
    T1 = Union[BasicAuth, HTTPBasicAuth, None]

    def __init__(self, es_model: ElasticSearch):
        self.es_model = es_model
        self.utils = OperationUtils()

    @abstractmethod
    def create(self, index: str, settings: Optional[dict] = None, mappings: Optional[dict] = None, auth: T1 = None):
        ...

    @abstractmethod
    def drop(self, index: str, auth: T1 = None):
        ...

    @abstractmethod
    def indexes(self, auth: T1 = None):
        ...

    @abstractmethod
    def show(self, index: str, auth: T1):
        ...

    @abstractmethod
    def insert(self, index: str, doc_id: str, auth: T1, **kwargs):
        ...

    @abstractmethod
    def delete(self, index: str, doc_id: str, auth: T1):
        ...

    @abstractmethod
    def get(self, index: str, doc_id: str, auth: T1):
        ...

    @abstractmethod
    def update(self, index: str, doc_id: str, auth: T1, **data):
        ...

    @abstractmethod
    def batch_insert(self, index: str, auth: T1, params: str):
        ...

    @abstractmethod
    def batch_update(self, index: str, auth: T1, params: str):
        ...

    @abstractmethod
    def batch_delete(self, index: str, auth: T1, mode: str = "match", **query):
        ...

    @abstractmethod
    def all(self, index: str, auth: T1, _from: int = 0, _size: int = 10):
        ...

    @abstractmethod
    def filter(self, index: str, auth: T1, query: dict, mode: str = "match", _from: int = 0, _size: int = 0):
        ...

    @abstractmethod
    def filter_by(self, index: str, auth: T1, query: dict):
        ...

    @abstractmethod
    def scroll(self, index: str, auth: T1, scroll: int, scroll_id: Optional[str] = None, mode: str = "match_all",
               _from: int = 0, _size: int = 1000, **query):
        ...
