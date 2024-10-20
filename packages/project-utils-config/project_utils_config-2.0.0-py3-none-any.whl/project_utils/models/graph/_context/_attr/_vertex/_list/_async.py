from . import _Optional
from . import GraphAttrVertex
from . import _BaseGraphAttrVertexCollection


class GraphAttrVertexCollectionAsyncContext(_BaseGraphAttrVertexCollection):
    CHILD_CLASS = GraphAttrVertex

    async def create(self, item: CHILD_CLASS):
        return await self.__objects__.create_vertex(**item.to_create())

    async def append(self, action: str, vertex: CHILD_CLASS):
        return await self.__objects__.append_vertex(action=action, **vertex.to_user_data())

    async def query(self, name: _Optional[str] = None):
        if name is None:
            return await self.__objects__.query_vertexes()
        else:
            return await self.__objects__.query_vertex(name)

    async def delete(self, item: CHILD_CLASS):
        return await self.__objects__.delete_vertex(item.name)
