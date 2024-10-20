from . import _ABC
from . import _Graph
from . import _BaseGraph
from . import _abstractmethod


class BaseGraphAttrOperation(_BaseGraph, _ABC):
    def __init__(self, graph: _Graph):
        self.__config__ = graph

    @_abstractmethod
    def schema(self, **kwargs):
        """Schema"""

    @_abstractmethod
    def create_property(self, **kwargs):
        """创建一个 PropertyKey"""

    @_abstractmethod
    def append_property(self, **kwargs):
        """为已存在的 PropertyKey 添加或移除 userdata"""

    @_abstractmethod
    def query_properties(self, **kwargs):
        """获取所有的 PropertyKey"""

    @_abstractmethod
    def query_property(self, **kwargs):
        """根据name获取PropertyKey"""

    @_abstractmethod
    def delete_property(self, **kwargs):
        """根据 name 删除 PropertyKey"""

    @_abstractmethod
    def create_vertex(self, **kwargs):
        """创建一个VertexLabel"""

    @_abstractmethod
    def append_vertex(self, **kwargs):
        """为已存在的VertexLabel添加properties或userdata，或者移除userdata（目前不支持移除properties）"""

    @_abstractmethod
    def query_vertexes(self, **kwargs):
        """获取所有的VertexLabel"""

    @_abstractmethod
    def query_vertex(self, **kwargs):
        """根据name获取VertexLabel"""

    @_abstractmethod
    def delete_vertex(self, **kwargs):
        """根据name删除VertexLabel"""

    @_abstractmethod
    def create_edge(self, **kwargs):
        """创建一个EdgeLabel"""

    @_abstractmethod
    def append_edge(self, **kwargs):
        """ 为已存在的EdgeLabel添加properties或userdata，或者移除userdata（目前不支持移除properties）"""

    @_abstractmethod
    def query_edges(self, **kwargs):
        """获取所有的EdgeLabel"""

    @_abstractmethod
    def query_edge(self, **kwargs):
        """根据name获取EdgeLabel"""

    @_abstractmethod
    def delete_edge(self, **kwargs):
        """根据name删除EdgeLabel """
