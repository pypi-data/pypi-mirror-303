from . import _List
from . import _Union
from . import _Optional
from . import _GraphAttrEdge
from . import _GraphAttrProperty
from . import _BaseGraphAttrEdgeCollection
from . import _GraphAttrEdgeCollectionAsyncContext


class GraphAttrEdgeCollectionAsyncModel(_BaseGraphAttrEdgeCollection):
    CHILD_CLASS = _GraphAttrEdge
    __context__: _GraphAttrEdgeCollectionAsyncContext

    def __init__(self):
        super().__init__()
        self.__context__ = _GraphAttrEdgeCollectionAsyncContext()

    async def create(self, item: CHILD_CLASS, created: dict):
        item.id = created['id']
        item.status = created['status']
        self.__data__.add(item)
        return item

    async def append(
            self,
            action: str,
            edge: CHILD_CLASS,
            user_data: _Optional[CHILD_CLASS.Types.UD],
            properties: _Optional[_List[_GraphAttrProperty]] = None,
            nullable_keys: _Optional[_List[_GraphAttrProperty]] = None,
    ):
        edge.user_data = user_data
        if properties:
            edge.properties.add_items(properties)
        if nullable_keys:
            edge.nullable_keys.add_items(nullable_keys)
        return edge

    async def query(self, result: _Union[list, dict], name: _Optional[str] = None):
        if name is None:
            for item in result:
                edge: _GraphAttrEdge = _GraphAttrEdge(**item)
                edge.user_data = item['user_data']
                await self.create(edge, item)
            return self.__data__
        else:
            edge: _GraphAttrEdge = _GraphAttrEdge(**result)
            edge.user_data = result['user_data']
            return edge

    async def delete(self, item: CHILD_CLASS):
        self.__data__.remove_from_element(item)
        return item
