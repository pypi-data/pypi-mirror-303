from . import _Any
from . import _GraphAttrSyncOperation

from ._basis import BaseGraphAttrContext


class GraphAttrSyncContextHandler(BaseGraphAttrContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__operation__ = _GraphAttrSyncOperation(graph=self.__config__)

    def schema(self, **kwargs):
        name: str = self.__utils__.before_schema(self.__model__)
        response: dict = self.__operation__.schema(name, self.__auth__)
        return self.__utils__.after_schema(response)

    def create_property(self, **kwargs):
        name: str = self.__utils__.before_create_property(self.__model__)
        response: dict = self.__operation__.create_property(name, kwargs, self.__auth__)
        return self.__utils__.after_create_property(response)

    def create_vertex(self, **kwargs):
        store: str = self.__utils__.before_create_vertex(self.__model__)
        response: dict = self.__operation__.create_vertex(store, self.__auth__, **kwargs)
        return self.__utils__.after_create_vertex(response)

    def create_edge(self, **kwargs):
        store: str = self.__utils__.before_create_edge(self.__model__)
        response: dict = self.__operation__.create_edge(store, self.__auth__, **kwargs)
        return self.__utils__.after_create_edge(response)

    def append_property(self, property_name: str, action: str, **kwargs):
        name: str = self.__utils__.before_append_property(self.__model__)
        response: dict = self.__operation__.append_property(property_name, action, name, self.__auth__, **kwargs)
        return self.__utils__.after_append_property(response)

    def append_vertex(self, name: str, action: str, **kwargs):
        store: str = self.__utils__.before_append_vertex(self.__model__)
        response: dict = self.__operation__.append_vertex(name, action, store, self.__auth__, **kwargs)
        return self.__utils__.after_append_vertex(response)

    def append_edge(self, name: str, action: str, **kwargs):
        store: str = self.__utils__.before_append_edge(self.__model__)
        response: dict = self.__operation__.append_edge(name, action, store, self.__auth__, **kwargs)
        return self.__utils__.after_append_edge(response)

    def query_properties(self, **kwargs):
        name: str = self.__utils__.before_query_properties(self.__model__)
        response: dict = self.__operation__.query_properties(name, self.__auth__)
        return self.__utils__.after_query_properties(response)

    def query_property(self, name: str):
        store: str = self.__utils__.before_query_property(self.__model__)
        response: dict = self.__operation__.query_property(name, store, self.__auth__)
        return self.__utils__.after_query_property(response)

    def query_vertexes(self, **kwargs):
        store: str = self.__utils__.before_query_vertexes(self.__model__)
        response: dict = self.__operation__.query_vertexes(store, self.__auth__)
        return self.__utils__.after_query_vertexes(response)

    def query_vertex(self, name: str):
        store: str = self.__utils__.before_query_vertex(self.__model__)
        response: dict = self.__operation__.query_vertex(name, store, self.__auth__)
        return self.__utils__.after_create_vertex(response)

    def query_edges(self, **kwargs):
        store: str = self.__utils__.before_query_edges(self.__model__)
        response: dict = self.__operation__.query_edges(store, self.__auth__)
        return self.__utils__.after_query_edges(response)

    def query_edge(self, name: str):
        store: str = self.__utils__.before_query_edge(self.__model__)
        response: dict = self.__operation__.query_edge(name, store, self.__auth__)
        return self.__utils__.after_query_edge(response)

    def delete_property(self, name: str):
        store: str = self.__utils__.before_delete_property(self.__model__)
        response: dict = self.__operation__.delete_property(name, store, self.__auth__)
        return self.__utils__.after_delete_property(response)

    def delete_vertex(self, name: str):
        store: str = self.__utils__.before_delete_vertex(self.__model__)
        response: dict = self.__operation__.delete_vertex(name, store, self.__auth__)
        return self.__utils__.after_delete_vertex(response)

    def delete_edge(self, name: str):
        store: str = self.__utils__.before_delete_edge(self.__model__)
        response: dict = self.__operation__.delete_edge(name, store, self.__auth__)
        return self.__utils__.after_delete_edge(response)
