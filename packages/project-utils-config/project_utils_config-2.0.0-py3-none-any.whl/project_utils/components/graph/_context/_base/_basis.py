from . import _T1
from . import _ABC
from . import _Any
from . import _Graph
from . import _BaseGraph
from . import _abstractmethod

from ._conf import BaseGraphConfContext
from ._attributes import BaseGraphAttrContext


class BaseGraphContext(_BaseGraph, _ABC):
    __auth__: _T1
    __model__: _Any
    __conf__: BaseGraphConfContext
    __attr__: BaseGraphAttrContext

    def __init__(self, graph: _Graph, model: _Any, auth: _T1 = None):
        self.__config__ = graph
        self.__model__ = model
        self.__auth__ = auth

    @_abstractmethod
    def graphs(self):
        """列出数据库中全部的图"""
