from ._meta import BaseMeta
from ._model import BaseModel
from ._batch import BaseBatch
from ._iter import BaseIter

ElasticSearchBaseMeta = BaseMeta
ElasticSearchBaseModel = BaseModel
ElasticSearchBaseBatch = BaseBatch
ElasticSearchIter = BaseIter


__all__ = [
    "ElasticSearchBaseMeta",
    "ElasticSearchBaseModel",
    "ElasticSearchBaseBatch",
    "ElasticSearchIter"
]
