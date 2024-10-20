from . import _Optional
from . import _GraphAttrEdge
from . import _BaseGraphAttrEdgeCollection


class GraphAttrEdgeCollectionSyncContext(_BaseGraphAttrEdgeCollection):
    CHILD_CLASS = _GraphAttrEdge

    def create(self, item: CHILD_CLASS):
        return self.__objects__.create_edge(**item.to_create())

    def append(self, action: str, edge: _GraphAttrEdge):
        return self.__objects__.append_edge(action=action, **edge.to_user_data())

    def query(self, name: _Optional[str] = None):
        if name is None:
            return self.__objects__.query_edges()
        else:
            return self.__objects__.query_edge(name)

    def delete(self, item: CHILD_CLASS):
        return self.__objects__.delete_edge(item.name)
