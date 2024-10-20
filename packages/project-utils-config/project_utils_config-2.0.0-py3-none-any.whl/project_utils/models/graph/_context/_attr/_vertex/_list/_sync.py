from . import _Optional
from . import GraphAttrVertex
from . import _BaseGraphAttrVertexCollection


class GraphAttrVertexCollectionSyncContext(_BaseGraphAttrVertexCollection):
    CHILD_CLASS = GraphAttrVertex

    def create(self, vertex: CHILD_CLASS):
        return self.__objects__.create_vertex(**vertex.to_create())

    def append(self, action: str, vertex: CHILD_CLASS):
        return self.__objects__.append_vertex(action=action, **vertex.to_user_data())

    def query(self, name: _Optional[str] = None):
        if name is None:
            return self.__objects__.query_vertexes()
        else:
            return self.__objects__.query_vertex(name)

    def delete(self, item: CHILD_CLASS):
        return self.__objects__.delete_vertex(item.name)
