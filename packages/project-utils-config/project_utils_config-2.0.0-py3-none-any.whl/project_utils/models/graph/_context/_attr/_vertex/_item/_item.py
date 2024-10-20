from . import _io
from . import _json
from . import _BaseGraphAttrVertex


class GraphAttrVertex(_BaseGraphAttrVertex):
    __super = _BaseGraphAttrVertex
    __types = __super.Types

    def to_code(self):
        data: dict = self.to_dict()
        data.pop("user_data")
        return _io.md5_encode(_json.dumps(data))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "ttl": self.ttl,
            "enable_label_index": self.enable_label_index,
            "id_strategy": self.id_strategy.value,
            "user_data": self.user_data if type(self.user_data) == dict else self.user_data.to_dict(),
            "properties": [item.name for item, code in self.properties],
            "primary_keys": [item.name for item, code in self.primary_keys],
            "nullable_keys": [item.name for item, code in self.nullable_keys],
            "index_labels": [item.name for item, code in self.index_labels]
        }

    def to_create(self):
        return self.to_params(
            ["name", "id_strategy", "properties", "primary_keys", "nullable_keys", "enable_label_index", "ttl"]
        )

    def to_user_data(self):
        return self.to_params(["name", "properties", "nullable_keys", "user_data"])
