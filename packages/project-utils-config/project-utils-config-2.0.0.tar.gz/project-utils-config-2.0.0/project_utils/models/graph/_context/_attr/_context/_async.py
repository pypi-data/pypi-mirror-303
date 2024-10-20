from . import _Optional
from . import _BaseGraphAttr
from . import _GraphAttrEdge
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _GraphAttrEdgeCollectionAsyncContext
from . import _GraphAttrIndexCollectionAsyncContext
from . import _GraphAttrVertexCollectionAsyncContext
from . import _GraphAttrPropertyCollectionAsyncContext


class GraphAttrAsyncContext(_BaseGraphAttr):
    def __init__(self):
        self.__properties__ = _GraphAttrPropertyCollectionAsyncContext()
        self.__vertexes__ = _GraphAttrVertexCollectionAsyncContext()
        self.__edges__ = _GraphAttrEdgeCollectionAsyncContext()
        self.__indexes__ = _GraphAttrIndexCollectionAsyncContext()

    async def schema(self, **kwargs):
        return await self.__objects__.schema(**kwargs)

    async def create_property(self, prop: _GraphAttrProperty):
        return await self.__properties__.create(prop)

    async def create_vertex(self, vertex: _GraphAttrVertex):
        return await self.__vertexes__.create(vertex)

    async def create_edge(self, edge: _GraphAttrEdge):
        return await self.__edges__.create(edge)

    async def append_property(self, action: str, prop: _GraphAttrProperty, user_data: _GraphAttrProperty.Types.UD):
        return await self.__properties__.append(action, prop, user_data)

    async def append_vertex(self, action: str, vertex: _GraphAttrVertex):
        return await self.__vertexes__.append(action, vertex)

    async def append_edge(self, action: str, edge: _GraphAttrEdge):
        return await self.__edges__.append(action, edge)

    async def query_property(self, name: _Optional[str] = None, **kwargs):
        return await self.__properties__.query(name)

    async def query_vertex(self, name: _Optional[str] = None):
        return await self.__vertexes__.query(name)

    async def query_edge(self, name: _Optional[str] = None):
        return await self.__edges__.query(name)

    async def delete_property(self, prop: _GraphAttrProperty):
        return await self.__properties__.delete(prop)

    async def delete_vertex(self, vertex: _GraphAttrVertex):
        return await self.__vertexes__.delete(vertex)

    async def delete_edge(self, edge: _GraphAttrEdge):
        return await self.__edges__.delete(edge)

    async def create_index(self, **kwargs):
        ...

    async def delete_index(self, **kwargs):
        ...

    async def query_index(self, **kwargs):
        ...
