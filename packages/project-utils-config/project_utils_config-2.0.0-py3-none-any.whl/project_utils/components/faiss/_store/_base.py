from typing import List, Dict
from abc import ABC, abstractmethod

from .._base import BaseFaiss, T2

T3 = List[Dict[str, int]]


class BaseFaissStore(BaseFaiss, ABC):
    __faiss_id_list: List[int]

    def __init__(self):
        self.__faiss_id_list = []

    @property
    def faiss_id_list(self):
        return self.__faiss_id_list

    @abstractmethod
    def add(self, item: T2):
        ...

    @abstractmethod
    def add_items(self, items: List[T2], faiss_ids: List[int]):
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

    def search(self, search_data:T3):
        ...
