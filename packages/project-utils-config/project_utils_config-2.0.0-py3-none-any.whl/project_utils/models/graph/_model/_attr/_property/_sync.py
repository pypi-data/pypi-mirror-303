from . import _Union
from . import _Optional
from . import _GraphAttrProperty
from . import _BaseGraphAttrPropertyCollection
from . import _GraphAttrPropertyCollectionSyncContext


class GraphAttrPropertyCollectionSyncModel(_BaseGraphAttrPropertyCollection):
    SUPER = _BaseGraphAttrPropertyCollection
    CHILD_CLASS = _GraphAttrProperty
    __context__: _GraphAttrPropertyCollectionSyncContext

    def __init__(self):
        super().__init__()
        self.__context__ = _GraphAttrPropertyCollectionSyncContext()

    def create(self, item: CHILD_CLASS):
        self.__data__.add(item)
        return item

    def append(self, action: str, prop: CHILD_CLASS, user_data: SUPER.BT.UD):
        prop.user_data = user_data
        return prop

    def query(self, result: _Union[list, dict], name: _Optional[str] = None):
        if name is None:
            for item in result:
                model: _GraphAttrProperty = _GraphAttrProperty(**item)
                model.user_data = item['user_data']
                self.create(model)
            return self.__data__
        else:
            prop: _GraphAttrProperty = _GraphAttrProperty(**result)
            prop.user_data = result['user_data']
            return prop

    def delete(self, item: CHILD_CLASS):
        return self.__data__.remove_from_element(item)
