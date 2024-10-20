from . import _io
from . import _json
from . import _BaseGraphAttrProperty


class GraphAttrProperty(_BaseGraphAttrProperty):
    def to_code(self):
        data: dict = self.to_dict()
        data.pop("user_data")
        return _io.md5_encode(_json.dumps(data))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "data_type": self.data_type.value,
            "cardinality": self.cardinality.value,
            "aggregate_type": self.aggregate_type.value,
            "write_type": self.write_type,
            "properties": [item for item, code in self.properties],
            "status": self.status,
            "user_data": self.user_data if type(self.user_data) == dict else self.user_data.to_dict()
        }

    def to_create(self):
        return self.to_params(["name", "data_type", "cardinality"])

    def to_user_data(self):
        return self.to_params(["name", "user_data"])
