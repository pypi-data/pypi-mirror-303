from . import _T1
from . import _GraphAttrSyncOperationHandler

from ._basis import BaseGraphAttrOperation


class GraphAttrSyncOperation(BaseGraphAttrOperation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphAttrSyncOperationHandler(*args, **kwargs)

    def schema(self, name: str, auth: _T1):
        return self.__handler__.schema(name, auth)

    def create_property(self, name: str, body: dict, auth: _T1):
        return self.__handler__.create_property(name, body, auth)

    def create_vertex(self, store: str, auth: _T1, **kwargs):
        return self.__handler__.create_vertex(store, auth, **kwargs)

    def create_edge(self, store: str, auth: _T1, **kwargs):
        return self.__handler__.create_edge(store, auth, **kwargs)

    def append_property(self, property_name: str, action: str, graph_name: str, auth: _T1, **kwargs):
        return self.__handler__.append_property(property_name, action, graph_name, auth, **kwargs)

    def append_vertex(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        return self.__handler__.append_vertex(name, action, store, auth, **kwargs)

    def append_edge(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        return self.__handler__.append_edge(name, action, store, auth, **kwargs)

    def query_properties(self, store: str, auth: _T1):
        return self.__handler__.query_properties(store, auth)

    def query_property(self, name: str, store: str, auth: _T1):
        return self.__handler__.query_property(name, store, auth)

    def query_vertexes(self, store: str, auth: _T1):
        return self.__handler__.query_vertexes(store, auth)

    def query_vertex(self, name: str, store: str, auth: _T1):
        return self.__handler__.query_vertex(name, store, auth)

    def query_edges(self, store: str, auth: _T1):
        return self.__handler__.query_edges(store, auth)

    def query_edge(self, name: str, store: str, auth: _T1):
        return self.__handler__.query_edge(name, store, auth)

    def delete_property(self, name: str, store: str, auth: _T1):
        return self.__handler__.delete_property(name, store, auth)

    def delete_vertex(self, name: str, store: str, auth: _T1):
        return self.__handler__.delete_vertex(name, store, auth)

    def delete_edge(self, name: str, store: str, auth: _T1):
        return self.__handler__.delete_edge(name, store, auth)
