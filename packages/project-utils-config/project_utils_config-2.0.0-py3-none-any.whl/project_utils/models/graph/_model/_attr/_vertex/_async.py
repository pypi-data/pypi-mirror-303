from . import _List
from . import _Union
from . import _Optional
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _BaseGraphAttrVertexCollection
from . import _GraphAttrVertexCollectionAsyncContext


class GraphAttrVertexCollectionAsyncModel(_BaseGraphAttrVertexCollection):
    CHILD_CLASS = _GraphAttrVertex
    __context__: _GraphAttrVertexCollectionAsyncContext

    def __init__(self):
        super().__init__()
        self.__context__ = _GraphAttrVertexCollectionAsyncContext()

    async def create(self, item: CHILD_CLASS, created: dict):
        item.id = created['id']
        self.__data__.add(item)
        return item

    async def append(
            self,
            action: str,
            vertex: _GraphAttrVertex,
            properties: _Optional[_List[_GraphAttrProperty]] = None,
            nullable_keys: _Optional[_List[_GraphAttrProperty]] = None,
            user_data: _Optional[_GraphAttrProperty.Types.UD] = None
    ):
        if properties:
            vertex.properties.add_items(properties)
        if nullable_keys:
            vertex.nullable_keys.add_items(nullable_keys)
        if user_data:
            vertex.user_data = user_data
        return vertex

    async def query(self, result: _Union[list, dict], name: _Optional[str] = None):
        if name is None:
            for item in result:
                await self.create(_GraphAttrVertex(**item), item)
            return self.__data__
        else:
            return _GraphAttrVertex(**result)

    async def delete(self, item: CHILD_CLASS):
        return self.__data__.remove_from_element(item)
