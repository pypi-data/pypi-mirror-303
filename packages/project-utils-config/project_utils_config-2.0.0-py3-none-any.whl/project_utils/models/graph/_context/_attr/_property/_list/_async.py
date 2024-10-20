from . import _Optional
from . import _GraphAttrProperty
from . import _BaseGraphAttrPropertyCollection


class GraphAttrPropertyCollectionAsyncContext(_BaseGraphAttrPropertyCollection):
    CHILD_CLASS = _GraphAttrProperty

    async def create(self, prop: CHILD_CLASS):
        item: dict = await self.__objects__.create_property(**prop.to_create())
        prop.id = item['id']
        prop.aggregate_type = item['aggregate_type']
        prop.write_type = item['write_type']
        prop.status = item['status']
        return prop

    async def append(self, action: str, prop: CHILD_CLASS, user_data: CHILD_CLASS.Types.UD):
        await self.__objects__.append_property(prop.name, action, **prop.to_user_data())
        return prop

    async def query(self, name: _Optional[str] = None):
        if name is None:
            return await self.__objects__.query_properties()
        else:
            return await self.__objects__.query_property(name)

    async def delete(self, item: CHILD_CLASS):
        return await self.__objects__.delete_property(item.name)