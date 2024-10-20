from abc import ABCMeta
from typing import Optional


class BaseMeta(metaclass=ABCMeta):
    name: Optional[str] = None
    settings: Optional[dict] = None
    mappings: Optional[dict] = None
    primary_key: Optional[str] = None
