import random

from typing import List
from abc import ABC, abstractmethod
from faiss import Index, IndexIDMap, index_factory, METRIC_L2

from project_utils.conf import Faiss

from .._base import BaseFaiss, T1


class BaseFaissIndex(BaseFaiss, ABC):
    __index: IndexIDMap

    def __init__(self, config: Faiss, measure: str = METRIC_L2):
        index: Index = index_factory(config.dim, config.param, measure)
        self.__index = IndexIDMap(index)

    def get_faiss_id(self, length: int = 9):
        return int("".join([str(random.randint(0, 9)) for i in range(length)]))

    @property
    def index(self):
        return self.__index

    @abstractmethod
    def add(self, embedding: T1):
        ...

    @abstractmethod
    def add_items(self, embeddings: List[T1]):
        ...

    @abstractmethod
    def remove_from_index(self, faiss_id: int):
        ...

    @abstractmethod
    def remove_from_element(self, faiss_id: int):
        ...

    @abstractmethod
    def remove_from_faiss_id(self, faiss_id: int):
        ...

    @abstractmethod
    def search(self, embedding: T1, top_k: int = 10):
        ...
