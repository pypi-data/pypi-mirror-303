from typing import List
from faiss import METRIC_L2
from abc import ABC, abstractmethod

from .._base import BaseFaiss, T1, T2
from .._index import FaissIndex
from .._store import FaissStore
from project_utils.conf import Faiss


class BaseFaissAPP(BaseFaiss, ABC):
    __faiss_config: Faiss
    __faiss_index: FaissIndex
    __faiss_store: FaissStore

    def __init__(self, dim: str = "1024", param: str = "Flat", measure: str = METRIC_L2):
        self.__faiss_config = Faiss(dim, param)
        self.__faiss_index = FaissIndex(self.__faiss_config, measure=measure)
        self.__faiss_store = FaissStore()

    @property
    def faiss_config(self):
        return self.__faiss_config

    @property
    def faiss_index(self):
        return self.__faiss_index

    @property
    def faiss_store(self):
        return self.__faiss_store

    @abstractmethod
    def add(self, embedding: T1, item: T2):
        ...

    @abstractmethod
    def add_items(self, embeddings: List[T1], items: List[T2]):
        ...

    @abstractmethod
    def remove_from_index(self, index: int):
        ...

    @abstractmethod
    def remove_from_element(self, element: T2):
        ...

    @abstractmethod
    def remove_from_faiss_id(self, faiss_id: int):
        ...

    @abstractmethod
    def search(self, embedding: T1, top_k: int=10):
        ...
