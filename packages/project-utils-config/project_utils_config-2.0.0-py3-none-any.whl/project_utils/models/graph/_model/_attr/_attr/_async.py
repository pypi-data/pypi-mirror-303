from . import _T3
from . import _List
from . import _Union
from . import _asyncio
from . import _Optional
from . import _BaseType
from . import _DataType
from . import _IdStrategy
from . import _Cardinality
from . import _BaseGraphAttr
from . import _GraphAttrEdge
from . import _GraphAttrIndex
from . import _GraphException
from . import _DefaultUserData
from . import _GraphAttrVertex
from . import _GraphAttrProperty
from . import _GraphAttrAsyncContext
from . import _GraphAttrEdgeCollectionAsyncModel
from . import _GraphAttrIndexCollectionAsyncModel
from . import _GraphAttrVertexCollectionAsyncModel
from . import _GraphAttrPropertyCollectionAsyncModel


class GraphAttrAsyncModel(_BaseGraphAttr):
    __context__: _GraphAttrAsyncContext

    __mapping__: dict = {
        "propertykeys": _GraphAttrProperty,
        "vertexlabels": _GraphAttrVertex,
        "edgelabels": _GraphAttrEdge

    }

    def __init__(self):
        self.__context__ = _GraphAttrAsyncContext()
        self.__edges__ = _GraphAttrEdgeCollectionAsyncModel()
        self.__indexes__ = _GraphAttrIndexCollectionAsyncModel()
        self.__vertexes__ = _GraphAttrVertexCollectionAsyncModel()
        self.__properties__ = _GraphAttrPropertyCollectionAsyncModel()

    def context(self, context: _T3):
        self.__context__.context(context)
        super().context(context)

    async def query_item(self, item: dict):
        for key in ("properties", "primary_keys", "nullable_keys", "index_labels", "sort_keys", "fields"):
            if key in item:
                for i in range(len(item[key])):
                    name: str = item[key][i]
                    item[key][i] = await self.query_property(name)
        return item

    async def schema(self, **kwargs):
        schema: dict = await self.__context__.schema(**kwargs)
        for key, items in schema.items():
            for item in items:
                if key != "propertykeys":
                    for k in ("properties", "primary_keys", "nullable_keys", "sort_keys", "fields", "index_labels"):
                        if k in item:
                            for i in range(len(item[k])):
                                if k != "index_labels":
                                    item[k][i] = await self.query_property(name=item[k][i])
                    for k in ("source_label", "target_label"):
                        if k in item:
                            item[k] = await self.query_vertex(item[k])
                model = self.__mapping__[key](**item)
                model.user_data = item['user_data']
                if key == "propertykeys":
                    await self.__properties__.create(model)
                elif key == "vertexlabels":
                    await self.__vertexes__.create(model, item)
                elif key == "edgelabels":
                    await self.__edges__.create(model, item)

    async def create_property(
            self,
            name: str,
            user_data: _Optional[_GraphAttrProperty.Types.UD] = None,
            data_type: str = _DataType.TEXT.value,
            cardinality: str = _Cardinality.SINGLE.value, **kwargs
    ):
        prop: _GraphAttrProperty = _GraphAttrProperty(name, data_type, cardinality, **kwargs)
        await self.__properties__.create(await self.__context__.create_property(prop))
        await self.append_property("append", prop, user_data)
        return prop

    async def create_vertex(
            self,
            name: str,
            user_data: _Optional[_GraphAttrVertex.Types.UD] = None,
            id_strategy: str = _IdStrategy.PRIMARY_KEY,
            **kwargs
    ):
        vertex: _GraphAttrVertex = _GraphAttrVertex(name, id_strategy, **kwargs)
        created: dict = await self.__context__.create_vertex(vertex)
        await self.__vertexes__.create(vertex, created)
        await self.append_vertex("append", vertex, user_data)
        return vertex

    async def create_edge(
            self,
            name: str,
            source_label: _GraphAttrVertex,
            target_label: _GraphAttrVertex,
            user_data: _Optional[_GraphAttrEdge.Types.UD] = None,
            **kwargs
    ):
        edge: _GraphAttrEdge = _GraphAttrEdge(name, source_label, target_label, **kwargs)
        created: dict = await self.__context__.create_edge(edge)
        await self.__edges__.create(edge, created)
        await _asyncio.sleep(0.5)
        await self.append_edge("append", edge, user_data=user_data)
        return edge

    async def create_index(self, **kwargs):
        ...

    async def append_property(
            self,
            action: str,
            prop: _GraphAttrProperty,
            user_data: _Optional[_GraphAttrProperty.Types.UD]
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 123)
        if user_data is None:
            user_data = _DefaultUserData()
        await self.__properties__.append(action, prop, user_data)
        await self.__context__.append_property(action, prop, user_data)
        return prop

    async def append_vertex(
            self,
            action: str,
            vertex: _GraphAttrVertex,
            properties: _Optional[_List[_GraphAttrProperty]] = None,
            nullable_keys: _Optional[_List[_GraphAttrProperty]] = None,
            user_data: _Optional[_GraphAttrVertex.Types.UD] = None,
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 139)
        if user_data is None:
            user_data = _DefaultUserData()
        await self.__vertexes__.append(action, vertex, properties, nullable_keys, user_data)
        await self.__context__.append_vertex(action, vertex)
        return vertex

    async def append_edge(
            self,
            action: str,
            edge: _GraphAttrEdge,
            properties: _Optional[_List[_GraphAttrEdge]] = None,
            nullable_keys: _Optional[_List[_GraphAttrEdge]] = None,
            user_data: _Optional[_GraphAttrEdge.Types.UD] = None
    ):
        summary: str = """The value of param "action" only have "append" and "eliminate",not other!"""
        assert action in ("append", "eliminate"), _GraphException(summary, __file__, 155)
        if user_data is None:
            user_data = _DefaultUserData()
        _edge: _GraphAttrEdge = await self.__edges__.append(action, edge, user_data, properties, nullable_keys)
        await self.__context__.append_edge(action, _edge)
        return edge

    async def query_property(self, name: _Optional[str] = None):
        result: _Union[list, dict] = await self.__context__.query_property(name)
        return await self.__properties__.query(result, name)

    async def query_vertex(self, name: _Optional[str] = None):
        result: _Union[list, dict] = await self.__context__.query_vertex(name)
        if type(result) == list:
            for item in result:
                await self.query_item(item)
        else:
            await self.query_item(result)
        return await self.__vertexes__.query(result, name)

    async def query_edge(self, name: _Optional[str] = None):
        result: _Union[list, dict] = await self.__context__.query_edge(name)
        if name is None:
            for item in result:
                for key in ("source_label", "target_label"):
                    _name: str = item[key]
                    item[key] = await self.query_vertex(name=_name)
                for key in ("properties", "nullable_keys", "sort_keys"):
                    for i in range(len(item[key])):
                        _name: str = item[key][i]
                        item[key][i] = await self.query_property(name=_name)
        else:
            for key in ("source_label", "target_label"):
                print(result)
                _name: str = result[key]
                result[key] = await self.query_vertex(name=_name)
            for key in ("properties", "nullable_keys", "sort_keys"):
                for i in range(len(result[key])):
                    _name: str = result[key][i]
                    result[key][i] = await self.query_property(name=_name)
        return await self.__edges__.query(result, name)

    async def query_index(self, **kwargs):
        ...

    async def delete_property(self, name: str):
        item: _GraphAttrProperty = await self.query_property(name)
        await self.__context__.delete_property(item)
        await self.__properties__.delete(item)
        return self.__properties__.__data__.count

    async def delete_vertex(self, name: str):
        model: _GraphAttrVertex = await self.query_vertex(name)
        await self.__context__.delete_vertex(model)
        await self.__vertexes__.delete(model)
        return model

    async def delete_edge(self, name: str):
        model: _GraphAttrEdge = await self.query_edge(name)
        await self.__context__.delete_edge(model)
        await self.__edges__.delete(model)
        return model

    async def delete_index(self, **kwargs):
        ...
