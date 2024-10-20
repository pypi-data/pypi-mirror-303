from . import _BaseGraphAttrIndex


class GraphAttrIndex(_BaseGraphAttrIndex):
    __super = _BaseGraphAttrIndex
    __types = __super.Types

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "user_data": self.user_data.to_dict(),
            "base_type": self.base_type.value,
            "base_value": self.base_value,
            "index_type": self.index_type,
            "fields": [item for item in self.fields]
        }

    def to_create(self):
        return self.to_params(["name", "base_type", "base_value", "index_type", "fields"])

    def to_user_data(self):
        return {}
