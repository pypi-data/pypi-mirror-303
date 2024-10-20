from . import _T3
from . import _Optional
from . import _BaseGraphAttr
from . import _GraphAttrEdge
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _GraphAttrEdgeCollectionSyncContext
from . import _GraphAttrIndexCollectionSyncContext
from . import _GraphAttrVertexCollectionSyncContext
from . import _GraphAttrPropertyCollectionSyncContext


class GraphAttrSyncContext(_BaseGraphAttr):
    def __init__(self):
        self.__edges__ = _GraphAttrEdgeCollectionSyncContext()
        self.__indexes__ = _GraphAttrIndexCollectionSyncContext()
        self.__vertexes__ = _GraphAttrVertexCollectionSyncContext()
        self.__properties__ = _GraphAttrPropertyCollectionSyncContext()

    def context(self, context: _T3):
        self.__objects__ = context
        self.__edges__.__objects__ = context
        self.__indexes__.__objects__ = context
        self.__vertexes__.__objects__ = context
        self.__properties__.__objects__ = context

    def schema(self, **kwargs):
        return self.__objects__.schema(**kwargs)

    def create_property(self, prop: _GraphAttrProperty):
        return self.__properties__.create(prop)

    def create_vertex(self, vertex: _GraphAttrVertex):
        return self.__vertexes__.create(vertex)

    def create_edge(self, edge: _GraphAttrEdge):
        return self.__edges__.create(edge)

    def append_property(self, action: str, prop: _GraphAttrProperty, user_data: _GraphAttrProperty.Types.UD):
        return self.__properties__.append(action, prop, user_data)

    def append_vertex(self, action: str, vertex: _GraphAttrVertex):
        return self.__vertexes__.append(action, vertex)

    def append_edge(self, action: str, edge: _GraphAttrEdge):
        return self.__edges__.append(action, edge)

    def query_property(self, name: _Optional[str] = None):
        return self.__properties__.query(name)

    def query_vertex(self, name: _Optional[str] = None):
        return self.__vertexes__.query(name)

    def query_edge(self, name: _Optional[str] = None):
        return self.__edges__.query(name)

    def delete_property(self, prop: _GraphAttrProperty):
        return self.__properties__.delete(prop)

    def delete_vertex(self, vertex: _GraphAttrVertex):
        return self.__vertexes__.delete(vertex)

    def delete_edge(self, edge: _GraphAttrEdge):
        return self.__edges__.delete(edge)

    def create_index(self, **kwargs):
        ...

    def delete_index(self, **kwargs):
        ...

    def query_index(self, **kwargs):
        ...
