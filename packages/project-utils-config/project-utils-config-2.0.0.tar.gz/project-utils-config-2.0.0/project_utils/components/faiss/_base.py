from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, List, Optional

from project_utils.models.faiss import FaissBaseModel

T1 = List[float]
T2 = TypeVar("T2", bound=FaissBaseModel)


class BaseFaiss(Generic[T2], metaclass=ABCMeta):
    @abstractmethod
    def add(self,**kwargs):
        ...

    @abstractmethod
    def add_items(self,**kwargs):
        ...

    @abstractmethod
    def remove_from_index(self,**kwargs):
        ...

    @abstractmethod
    def remove_from_faiss_id(self,**kwargs):
        ...

    @abstractmethod
    def remove_from_element(self,**kwargs):
        ...

    @abstractmethod
    def search(self,**kwargs):
        ...
