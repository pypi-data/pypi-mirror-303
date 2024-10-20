from . import _T1
from . import _GraphAttrAsyncOperationHandler

from ._basis import BaseGraphAttrOperation


class GraphAttrAsyncOperation(BaseGraphAttrOperation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphAttrAsyncOperationHandler(*args, **kwargs)

    async def schema(self, store: str, auth: _T1):
        return await self.__handler__.schema(store, auth)

    async def create_property(self, store: str, body: dict, auth: _T1):
        return await self.__handler__.create_property(store, body, auth)

    async def create_vertex(self, store: str, auth: _T1, **kwargs):
        return await self.__handler__.create_vertex(store, auth, **kwargs)

    async def create_edge(self, store: str, auth: _T1, **kwargs):
        return await self.__handler__.create_edge(store, auth, **kwargs)

    async def append_property(self, property_name: str, action: str, store: str, auth: _T1, **kwargs):
        return await self.__handler__.append_property(property_name, action, store, auth, **kwargs)

    async def append_vertex(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        return await self.__handler__.append_vertex(name, action, store, auth, **kwargs)

    async def append_edge(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        return await self.__handler__.append_edge(name, action, store, auth, **kwargs)

    async def query_properties(self, store: str, auth: _T1):
        return await self.__handler__.query_properties(store, auth)

    async def query_property(self, name: str, store: str, auth: _T1):
        return await self.__handler__.query_property(name, store, auth)

    async def query_vertexes(self, store: str, auth: _T1):
        return await self.__handler__.query_vertexes(store, auth)

    async def query_vertex(self, name: str, store: str, auth: _T1):
        return await self.__handler__.query_vertex(name, store, auth)

    async def query_edges(self, store: str, auth: _T1):
        return await self.__handler__.query_edges(store, auth)

    async def query_edge(self, name: str, store: str, auth: _T1):
        return await self.__handler__.query_edge(name, store, auth)

    async def delete_property(self, name: str, store: str, auth: _T1):
        return await self.__handler__.delete_property(name, store, auth)

    async def delete_vertex(self, name: str, store: str, auth: _T1):
        return await self.__handler__.delete_vertex(name, store, auth)

    async def delete_edge(self, name: str, store: str, auth: _T1):
        return await self.__handler__.delete_edge(name, store, auth)
