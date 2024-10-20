from . import _Optional
from . import _GraphAttrEdge
from . import _BaseGraphAttrEdgeCollection


class GraphAttrEdgeCollectionAsyncContext(_BaseGraphAttrEdgeCollection):
    CHILD_CLASS = _GraphAttrEdge

    async def create(self, item: CHILD_CLASS):
        return await self.__objects__.create_edge(**item.to_create())

    async def append(self, action: str, edge: _GraphAttrEdge):
        return await self.__objects__.append_edge(action=action, **edge.to_user_data())

    async def query(self, name: _Optional[str] = None):
        if name is None:
            return await self.__objects__.query_edges()
        else:
            return await self.__objects__.query_edge(name)

    async def delete(self, item: CHILD_CLASS):
        return await self.__objects__.delete_edge(item.name)
