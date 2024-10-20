from typing import TypeVar, Generic

from ._base_model import BaseModel
from .._base_batch import BaseBatch as SourceBatch

T = TypeVar("T", bound=BaseModel)


class BaseBatch(SourceBatch, Generic[T]):
    ...
