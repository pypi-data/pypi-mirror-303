from . import _T3
from . import _Any
from . import _ABCMeta
from . import _TypeVar
from . import _abstractmethod

from ._labels import BaseGraphAttrEdgeCollection
from ._labels import BaseGraphAttrVertexCollection
from ._properties import BaseGraphAttrIndexCollection
from ._properties import BaseGraphAttrPropertyCollection

EC = _TypeVar("EC", bound=BaseGraphAttrEdgeCollection, covariant=True)
VC = _TypeVar("VC", bound=BaseGraphAttrVertexCollection, covariant=True)
IC = _TypeVar("IC", bound=BaseGraphAttrIndexCollection, covariant=True)
PC = _TypeVar("PC", bound=BaseGraphAttrPropertyCollection, covariant=True)


class BaseGraphAttr(metaclass=_ABCMeta):
    __objects__: _T3
    __properties__: PC
    __indexes__: IC
    __vertexes__: VC
    __edges__: EC

    def context(self, context: _T3):
        self.__objects__ = context
        self.__properties__.__objects__ = context
        self.__indexes__.__objects__ = context
        self.__vertexes__.__objects__ = context
        self.__edges__.__objects__ = context

    @_abstractmethod
    def schema(self, **kwargs):
        ...

    @_abstractmethod
    def create_property(self, **kwargs):
        ...

    @_abstractmethod
    def append_property(self, **kwargs):
        ...

    @_abstractmethod
    def query_property(self, **kwargs):
        ...

    @_abstractmethod
    def delete_property(self, **kwargs):
        ...

    @_abstractmethod
    def create_vertex(self, **kwargs):
        ...

    @_abstractmethod
    def append_vertex(self, **kwargs):
        ...

    @_abstractmethod
    def query_vertex(self, **kwargs):
        ...

    @_abstractmethod
    def delete_vertex(self, **kwargs):
        ...

    @_abstractmethod
    def create_edge(self, **kwargs):
        ...

    @_abstractmethod
    def append_edge(self, **kwargs):
        ...

    @_abstractmethod
    def query_edge(self, **kwargs):
        ...

    @_abstractmethod
    def delete_edge(self, **kwargs):
        ...

    @_abstractmethod
    def create_index(self, **kwargs):
        ...

    @_abstractmethod
    def delete_index(self, **kwargs):
        ...

    @_abstractmethod
    def query_index(self, **kwargs):
        ...
