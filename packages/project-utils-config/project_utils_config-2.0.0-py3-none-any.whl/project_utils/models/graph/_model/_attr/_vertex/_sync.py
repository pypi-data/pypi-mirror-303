from . import _List
from . import _Union
from . import _Optional
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _BaseGraphAttrVertexCollection
from . import _GraphAttrVertexCollectionSyncContext


class GraphAttrVertexCollectionSyncModel(_BaseGraphAttrVertexCollection):
    CHILD_CLASS = _GraphAttrVertex
    __context__: _GraphAttrVertexCollectionSyncContext

    def __init__(self):
        super().__init__()
        self.__context__ = _GraphAttrVertexCollectionSyncContext()

    def create(self, item: CHILD_CLASS, created: dict):
        item.id = created['id']
        self.__data__.add(item)
        return item

    def append(
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

    def query(self, result: _Union[list, dict], name: _Optional[str] = None):
        if name is None:
            for item in result:
                vertex: _GraphAttrVertex = _GraphAttrVertex(**item)
                vertex.user_data = item['user_data']
                self.create(vertex, item)
            return self.__data__
        else:
            vertex: _GraphAttrVertex = _GraphAttrVertex(**result)
            vertex.user_data = result['user_data']
            return vertex

    def delete(self, item: CHILD_CLASS):
        return self.__data__.remove_from_element(item)
