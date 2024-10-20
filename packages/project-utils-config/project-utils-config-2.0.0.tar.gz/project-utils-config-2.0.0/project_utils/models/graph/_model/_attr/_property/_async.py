from . import _Union
from . import _Optional
from . import _GraphAttrProperty
from . import _BaseGraphAttrPropertyCollection
from . import _GraphAttrPropertyCollectionAsyncContext


class GraphAttrPropertyCollectionAsyncModel(_BaseGraphAttrPropertyCollection):
    SUPER = _BaseGraphAttrPropertyCollection
    CHILD_CLASS = _GraphAttrProperty
    __context__: _GraphAttrPropertyCollectionAsyncContext

    def __init__(self):
        super().__init__()
        self.__context__ = _GraphAttrPropertyCollectionAsyncContext()

    async def create(self, item: CHILD_CLASS):
        self.__data__.add(item)
        return item

    async def append(self, action: str, prop: CHILD_CLASS, user_data: SUPER.BT.UD):
        prop.user_data = user_data
        return prop

    async def query(self, result: _Union[list, dict], name: _Optional[str] = None):
        if name is None:
            for item in result:
                model: _GraphAttrProperty = _GraphAttrProperty(**item)
                model.user_data = item['user_data']
                await self.create(model)
            return self.__data__
        else:
            model: _GraphAttrProperty = _GraphAttrProperty(**result)
            return model

    async def delete(self, item: CHILD_CLASS):
        return self.__data__.remove_from_element(item)
