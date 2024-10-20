from . import _Optional
from . import _GraphAttrProperty
from . import _BaseGraphAttrPropertyCollection


class GraphAttrPropertyCollectionSyncContext(_BaseGraphAttrPropertyCollection):
    CHILD_CLASS = _GraphAttrProperty

    def create(self, item: CHILD_CLASS):
        prop_item: dict = self.__objects__.create_property(**item.to_create())
        item.id = prop_item['id']
        item.aggregate_type = prop_item['aggregate_type']
        item.write_type = prop_item['write_type']
        item.status = prop_item['status']
        return item

    def append(self, action: str, prop: CHILD_CLASS, user_data: CHILD_CLASS.Types.UD):
        property_name: str = prop.name
        self.__objects__.append_property(property_name, action, **prop.to_user_data())
        return prop

    def delete(self, item: CHILD_CLASS):
        return self.__objects__.delete_property(item.name)

    def query(self, name: _Optional[str] = None):
        if name is None:
            return self.__objects__.query_properties()
        else:
            return self.__objects__.query_property(name)
