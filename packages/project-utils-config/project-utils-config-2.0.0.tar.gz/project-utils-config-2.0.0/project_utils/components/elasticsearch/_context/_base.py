from aiohttp import BasicAuth
from typing import Union, Optional
from abc import ABC, abstractmethod
from requests.auth import HTTPBasicAuth

from ._utils import ContextUtils
from .._base import BaseElasticSearch, ElasticSearch
from .._operation import ElasticSearchOperation, AsyncElasticSearchOperation

T = Union[ElasticSearchOperation, AsyncElasticSearchOperation]


class BaseElasticSearchContext(BaseElasticSearch, ABC):
    operation: T
    T1 = Union[BasicAuth, HTTPBasicAuth, None]
    utils: ContextUtils
    auth: T1

    def __init__(self, es_model: ElasticSearch, model: any, auth: T1):
        self.es_model = es_model
        self.model = model
        self.auth = auth
        self.utils = ContextUtils()

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def drop(self):
        ...

    @abstractmethod
    def indexes(self):
        ...

    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def delete(self):
        ...

    @abstractmethod
    def get(self, doc_id: str):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def batch_insert(self, b: any):
        ...

    @abstractmethod
    def batch_update(self, b: any):
        ...

    @abstractmethod
    def batch_delete(self, mode: str = "match", **query):
        ...

    @abstractmethod
    def all(self, _from: int = 0, _size: int = 10):
        ...

    @abstractmethod
    def filter(self, mode: str = "match", _from: int = 0, _size: int = 10, **query):
        ...

    @abstractmethod
    def filter_by(self, query: dict):
        ...

    @abstractmethod
    def scroll(self, scroll: int, mode: str = "match_all", _from: int = 0, _size: int = 1000, **query):
        ...
