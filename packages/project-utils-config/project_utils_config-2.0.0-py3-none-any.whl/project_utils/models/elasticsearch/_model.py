from ._meta import BaseMeta
from .._base_model import BaseModel as SourceModel

from project_utils.db.elasticsearch import ElasticSearchContext


class BaseModel(SourceModel):
    class Meta(BaseMeta):
        ...

    class DefaultMeta(BaseMeta):
        primary_key = "doc_id"
        settings = {}
        mappings = {}

    __meta__: Meta
    __source__: dict
    __default__: DefaultMeta
    __objects__: ElasticSearchContext

    def __init__(self, **kwargs):
        self.__source__ = kwargs.copy()
        super().__init__(**kwargs)
        self.__meta__ = self.Meta()
        self.__default__ = self.DefaultMeta()

    def to_dict(self):
        primary_key: str = self.__default__.primary_key if self.__meta__.primary_key is None else self.__meta__.primary_key
        result: dict = super().to_dict().copy()
        result.pop(primary_key)
        return result
