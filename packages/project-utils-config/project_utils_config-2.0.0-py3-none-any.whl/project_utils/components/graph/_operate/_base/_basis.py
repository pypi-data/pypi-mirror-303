from . import _T1
from . import _ABC
from . import _Graph
from . import _BaseGraph
from . import _abstractmethod

class BaseGraphOperation(_BaseGraph, _ABC):
    def __init__(self, graph: _Graph):
        self.__config__ = graph

    @_abstractmethod
    def graphs(self, auth: _T1 = None):
        """列出数据库中全部的图"""
