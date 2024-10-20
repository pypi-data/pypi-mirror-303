from . import _T3
from . import _List
from . import _Union
from . import _BaseType
from . import _DataType
from . import _Optional
from . import _IdStrategy
from . import _system_time
from . import _Cardinality
from . import _GraphAttrEdge
from . import _BaseGraphAttr
from . import _GraphException
from . import _GraphAttrIndex
from . import _DefaultUserData
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _GraphAttrSyncContext
from . import _GraphAttrEdgeCollectionSyncModel
from . import _GraphAttrIndexCollectionSyncModel
from . import _GraphAttrVertexCollectionSyncModel
from . import _GraphAttrPropertyCollectionSyncModel


class GraphAttrSyncModel(_BaseGraphAttr):
    __context__: _GraphAttrSyncContext

    __mapping__: dict = {
        "propertykeys": _GraphAttrProperty,
        "vertexlabels": _GraphAttrVertex,
        "edgelabels": _GraphAttrEdge,
    }

    def __init__(self):
        self.__context__ = _GraphAttrSyncContext()
        self.__edges__ = _GraphAttrEdgeCollectionSyncModel()
        self.__indexes__ = _GraphAttrIndexCollectionSyncModel()
        self.__vertexes__ = _GraphAttrVertexCollectionSyncModel()
        self.__properties__ = _GraphAttrPropertyCollectionSyncModel()

    def context(self, context: _T3):
        self.__context__.context(context)
        super().context(context)

    def schema(self, **kwargs):
        schema: dict = self.__context__.schema()
        for key, items in schema.items():
            for item in items:
                if key != "propertykeys":
                    for k in ("properties", "primary_keys", "nullable_keys", "sort_keys", "fields"):
                        if k in item:
                            for i in range(len(item[k])):
                                item[k][i] = self.query_property(name=item[k][i])
                    for k in ("source_label", "target_label"):
                        if k in item:
                            print(item[k])
                            item[k] = self.query_vertex(item[k])
                model = self.__mapping__[key](**item)
                model.user_data = item['user_data']
                if key == "propertykeys":
                    self.__properties__.create(model)
                elif key == "vertexlabels":
                    self.__vertexes__.create(model, item)
                elif key == "edgelabels":
                    self.__edges__.create(model, item)

    def create_property(
            self,
            name: str,
            user_data: _Optional[_GraphAttrProperty.Types.UD] = None,
            data_type: str = _DataType.TEXT.value,
            cardinality: str = _Cardinality.SINGLE.value, **kwargs):
        prop: _GraphAttrProperty = _GraphAttrProperty(name, data_type, cardinality, **kwargs)
        self.__properties__.create(self.__context__.create_property(prop))
        _system_time.sleep(0.5)
        self.append_property("append", prop, user_data)
        return prop

    def create_vertex(
            self,
            name: str,
            user_data: _Optional[_GraphAttrVertex.Types.UD] = None,
            id_strategy: str = _IdStrategy.PRIMARY_KEY,
            **kwargs
    ):
        vertex: _GraphAttrVertex = _GraphAttrVertex(name, id_strategy, **kwargs)
        created: dict = self.__context__.create_vertex(vertex)
        self.__vertexes__.create(vertex, created)
        self.append_vertex("append", vertex, user_data)
        return vertex

    def create_edge(
            self,
            name: str,
            source_label: _GraphAttrVertex,
            target_label: _GraphAttrVertex,
            user_data: _Optional[_GraphAttrEdge.Types.UD] = None,
            **kwargs
    ):
        edge: _GraphAttrEdge = _GraphAttrEdge(name, source_label, target_label, **kwargs)
        created: dict = self.__context__.create_edge(edge)
        self.__edges__.create(edge, created)
        print(created)
        # _system_time.sleep(1)
        self.append_edge("append", edge, user_data=user_data)
        return edge

    def create_index(self, **kwargs):
        ...

    def append_property(
            self,
            action: str,
            prop: _GraphAttrProperty,
            user_data: _Optional[_GraphAttrProperty.Types.UD]
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 115)
        if user_data is None:
            user_data = _DefaultUserData()
        self.__properties__.append(action, prop, user_data)

        self.__context__.append_property(action, prop, user_data)
        return prop

    def append_vertex(
            self,
            action: str,
            vertex: _GraphAttrVertex,
            properties: _Optional[_List[_GraphAttrProperty]] = None,
            nullable_keys: _Optional[_List[_GraphAttrProperty]] = None,
            user_data: _Optional[_GraphAttrVertex.Types.UD] = None
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 132)
        if user_data is None:
            user_data = _DefaultUserData()
        self.__vertexes__.append(action, vertex, properties, nullable_keys, user_data)
        self.__context__.append_vertex(action, vertex)
        return vertex

    def append_edge(
            self,
            action: str,
            edge: _GraphAttrEdge,
            properties: _Optional[_List[_GraphAttrEdge]] = None,
            nullable_keys: _Optional[_List[_GraphAttrEdge]] = None,
            user_data: _Optional[_GraphAttrEdge.Types.UD] = None
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 148)
        if user_data is None:
            user_data = _DefaultUserData()
        _edge: _GraphAttrEdge = self.__edges__.append(action, edge, user_data, properties, nullable_keys)

        self.__context__.append_edge(action, _edge)
        return edge

    def query_property(self, name: _Optional[str] = None):
        result: _Union[list, dict] = self.__context__.query_property(name)
        return self.__properties__.query(result, name)

    def query_vertex(self, name: _Optional[str] = None):
        result: _Union[list, dict] = self.__context__.query_vertex(name)
        if name is None:
            for item in result:
                for key in ("primary_keys", "nullable_keys", "properties"):
                    for i in range(len(item[key])):
                        item[key][i] = self.query_property(name=item[key][i])
        else:
            for key in ("primary_keys", "nullable_keys", "index_labels", "properties"):
                for i in range(len(result[key])):
                    if key != "index_labels":
                        result[key][i] = self.query_property(name=result[key][i])
        return self.__vertexes__.query(result, name)

    def query_edge(self, name: _Optional[str] = None):
        result: _Union[list, dict] = self.__context__.query_edge(name)
        if name is None:
            for item in result:
                for key in ("source_label", "target_label"):
                    _name: str = item[key]
                    item[key] = self.query_vertex(name=_name)
                for key in ("properties", "nullable_keys", "sort_keys"):
                    for i in range(len(item[key])):
                        _name: str = item[key][i]
                        item[key][i] = self.query_property(name=_name)
        else:
            for key in ("source_label", "target_label"):
                _name: str = result[key]
                result[key] = self.query_vertex(name=_name)
            for key in ("properties", "nullable_keys", "sort_keys"):
                for i in range(len(result[key])):
                    _name: str = result[key][i]
                    result[key][i] = self.query_property(name=_name)
        return self.__edges__.query(result, name)

    def query_index(self, **kwargs):
        ...

    def delete_property(self, name: str):
        item: _GraphAttrProperty = self.query_property(name)
        self.__context__.delete_property(item)
        self.__properties__.delete(item)
        return self.__properties__.__data__.count

    def delete_vertex(self, name: str):
        model: _GraphAttrVertex = self.query_vertex(name)
        self.__context__.delete_vertex(model)
        self.__vertexes__.delete(model)
        return model

    def delete_edge(self, name: str):
        model: _GraphAttrEdge = self.query_edge(name)
        self.__context__.delete_edge(model)
        self.__edges__.delete(model)
        return model

    def delete_index(self, **kwargs):
        ...
