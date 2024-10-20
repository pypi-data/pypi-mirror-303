from . import _Any
from . import _GraphAttrAsyncContextHandler

from ._basis import BaseGraphAttrContext


class GraphAttrAsyncContext(BaseGraphAttrContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphAttrAsyncContextHandler(*args, **kwargs)

    async def schema(self, **kwargs):
        return await self.__handler__.schema(**kwargs)

    async def create_property(self, **kwargs):
        return await self.__handler__.create_property(**kwargs)

    async def create_vertex(self, **kwargs):
        return await self.__handler__.create_vertex(**kwargs)

    async def create_edge(self, **kwargs):
        return await self.__handler__.create_edge(**kwargs)

    async def append_property(self, property_name: str, action: str, **kwargs):
        return await self.__handler__.append_property(property_name, action, **kwargs)

    async def append_vertex(self, name: str, action: str, **kwargs):
        return await self.__handler__.append_vertex(name, action, **kwargs)

    async def append_edge(self, name: str, action: str, **kwargs):
        return await self.__handler__.append_edge(name, action, **kwargs)

    async def query_properties(self):
        return await self.__handler__.query_properties()

    async def query_property(self, name: str):
        return await self.__handler__.query_property(name)

    async def query_vertexes(self, **kwargs):
        return await self.__handler__.query_vertexes(**kwargs)

    async def query_vertex(self, name: str):
        return await self.__handler__.query_vertex(name)

    async def query_edges(self, **kwargs):
        return await self.__handler__.query_edges(**kwargs)

    async def query_edge(self, name: str):
        return await self.__handler__.query_edge(name)

    async def delete_property(self, name: str):
        return await self.__handler__.delete_property(name)

    async def delete_vertex(self, name: str):
        return await self.__handler__.delete_vertex(name)

    async def delete_edge(self, name: str):
        return await self.__handler__.delete_edge(name)
