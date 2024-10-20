from . import _Any
from . import _GraphAttrSyncContextHandler

from ._basis import BaseGraphAttrContext


class GraphAttrSyncContext(BaseGraphAttrContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphAttrSyncContextHandler(*args, **kwargs)

    def schema(self, **kwargs):
        return self.__handler__.schema(**kwargs)

    def create_property(self, **kwargs):
        return self.__handler__.create_property(**kwargs)

    def create_vertex(self, **kwargs):
        return self.__handler__.create_vertex(**kwargs)

    def create_edge(self, **kwargs):
        return self.__handler__.create_edge(**kwargs)

    def append_property(self, property_name: str, action: str, **kwargs):
        return self.__handler__.append_property(property_name, action, **kwargs)

    def append_vertex(self, name: str, action: str, **kwargs):
        return self.__handler__.append_vertex(name, action, **kwargs)

    def append_edge(self, name: str, action: str, **kwargs):
        return self.__handler__.append_edge(name, action, **kwargs)

    def query_properties(self, **kwargs):
        return self.__handler__.query_properties(**kwargs)

    def query_property(self, name: str):
        return self.__handler__.query_property(name)

    def query_vertexes(self, **kwargs):
        return self.__handler__.query_vertexes(**kwargs)

    def query_vertex(self, name: str):
        return self.__handler__.query_vertex(name)

    def query_edges(self, **kwargs):
        return self.__handler__.query_edges(**kwargs)

    def query_edge(self, name: str):
        return self.__handler__.query_edge(name)

    def delete_property(self, name: str):
        return self.__handler__.delete_property(name)

    def delete_vertex(self, name: str):
        return self.__handler__.delete_vertex(name)

    def delete_edge(self, name: str):
        return self.__handler__.delete_edge(name)
