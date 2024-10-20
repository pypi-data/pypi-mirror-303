from . import _Any
from . import _GraphAttrAsyncOperation

from ._basis import BaseGraphAttrContext


class GraphAttrAsyncContextHandler(BaseGraphAttrContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__operation__ = _GraphAttrAsyncOperation(graph=self.__config__)

    async def schema(self, **kwargs):
        store: str = self.__utils__.before_schema(self.__model__)
        response: dict = await self.__operation__.schema(store, self.__auth__)
        return self.__utils__.after_schema(response)

    async def create_property(self, **kwargs):
        name: str = self.__utils__.before_create_property(self.__model__)
        response: dict = await self.__operation__.create_property(name, kwargs, self.__auth__)
        return self.__utils__.after_create_property(response)

    async def create_vertex(self, **kwargs):
        store: str = self.__utils__.before_create_vertex(self.__model__)
        response: dict = await self.__operation__.create_vertex(store, self.__auth__, **kwargs)
        return self.__utils__.after_create_vertex(response)

    async def create_edge(self, **kwargs):
        store: str = self.__utils__.before_create_edge(self.__model__)
        response: dict = await self.__operation__.create_edge(store, self.__auth__, **kwargs)
        return self.__utils__.after_create_edge(response)

    async def append_property(self, property_name: str, action: str, **kwargs):
        name: str = self.__utils__.before_append_property(self.__model__)
        response: dict = await self.__operation__.append_property(property_name, action, name, self.__auth__, **kwargs)
        return self.__utils__.after_append_property(response)

    async def append_vertex(self, name: str, action: str, **kwargs):
        store: str = self.__utils__.before_append_vertex(self.__model__)
        response: dict = await self.__operation__.append_vertex(name, action, store, self.__auth__, **kwargs)
        return self.__utils__.after_create_vertex(response)

    async def append_edge(self, name: str, action: str, **kwargs):
        store: str = self.__utils__.before_append_edge(self.__model__)
        response: dict = await self.__operation__.append_edge(name, action, store, self.__auth__, **kwargs)
        return self.__utils__.after_append_edge(response)

    async def query_properties(self, **kwargs):
        store: str = self.__utils__.before_query_properties(self.__model__)
        response: dict = await self.__operation__.query_properties(store, self.__auth__)
        return self.__utils__.after_query_properties(response)

    async def query_property(self, name: str):
        store: str = self.__utils__.before_query_property(self.__model__)
        response: dict = await self.__operation__.query_property(name, store, self.__auth__)
        return self.__utils__.after_query_property(response)

    async def query_vertexes(self, **kwargs):
        store: str = self.__utils__.before_query_vertexes(self.__model__)
        response: dict = await self.__operation__.query_vertexes(store, self.__auth__)
        return self.__utils__.after_query_vertexes(response)

    async def query_vertex(self, name: str):
        store: str = self.__utils__.before_query_vertex(self.__model__)
        response: dict = await self.__operation__.query_vertex(name, store, self.__auth__)
        return self.__utils__.after_create_vertex(response)

    async def query_edges(self, **kwargs):
        store: str = self.__utils__.before_query_edges(self.__model__)
        response: dict = await self.__operation__.query_edges(store, self.__auth__)
        return self.__utils__.after_query_edges(response)

    async def query_edge(self, name: str):
        store: str = self.__utils__.before_query_edge(self.__model__)
        response: dict = await self.__operation__.query_edge(name, store, self.__auth__)
        return self.__utils__.after_query_edge(response)

    async def delete_property(self, name: str):
        store: str = self.__utils__.before_delete_property(self.__model__)
        response: dict = await self.__operation__.delete_property(name, store, self.__auth__)
        return self.__utils__.after_delete_property(response)

    async def delete_vertex(self, name: str):
        store: str = self.__utils__.before_delete_vertex(self.__model__)
        response: dict = await self.__operation__.delete_vertex(name, store, self.__auth__)
        return self.__utils__.after_delete_vertex(response)

    async def delete_edge(self, name: str):
        store: str = self.__utils__.before_delete_edge(self.__model__)
        response: dict = await self.__operation__.delete_edge(name, store, self.__auth__)
        return self.__utils__.after_delete_edge(response)
