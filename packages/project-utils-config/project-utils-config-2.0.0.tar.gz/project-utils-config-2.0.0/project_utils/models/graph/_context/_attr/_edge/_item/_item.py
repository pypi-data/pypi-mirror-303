from . import _io
from . import _json
from . import _BaseGraphAttrEdge


class GraphAttrEdge(_BaseGraphAttrEdge):
    __super = _BaseGraphAttrEdge
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
            "source_label": self.source_label.name,
            "target_label": self.target_label.name,
            "frequency": self.frequency.value,
            "user_data": self.user_data if type(self.user_data) == dict else self.user_data.to_dict(),
            "properties": [item.name for item, code in self.properties],
            "nullable_keys": [item.name for item, code in self.nullable_keys],
            "index_labels": [item.name for item, code in self.index_labels],
            "sort_keys": [item.name for item, code in self.sort_keys],
        }

    def to_create(self):
        return self.to_params(
            ["name", "source_label", "target_label", "frequency", "properties", "sort_keys", "nullable_keys",
             "enable_label_index", "ttl"]
        )

    def to_user_data(self):
        return self.to_params(["name", "properties", "nullable_keys", "user_data"])
