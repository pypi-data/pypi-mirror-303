from abc import ABC as _ABC
from abc import ABCMeta as _ABCMeta
from abc import abstractmethod as _abstractmethod
from aiohttp.client import BasicAuth as _BasicAuth

from requests.auth import HTTPBasicAuth as _HTTPBasicAuth

from typing import Any as _Any
from typing import Union as _Union
from typing import Optional as _Optional

from project_utils.conf import Graph as _Graph

from .._base import BaseGraph as _BaseGraph

from .._operate import GraphOperation as _GraphOperation
from .._operate import AsyncGraphOperation as _AsyncGraphOperation
from .._operate import GraphConfSyncOperation as _GraphConfSyncOperation
from .._operate import GraphAttrSyncOperation as _GraphAttrSyncOperation
from .._operate import GraphConfAsyncOperation as _GraphConfAsyncOperation
from .._operate import GraphAttrAsyncOperation as _GraphAttrAsyncOperation

_T1 = _Optional[_Union[_BasicAuth, _HTTPBasicAuth]]
_T2 = _Union[_GraphOperation, _AsyncGraphOperation]
_T3 = _Union[_GraphConfSyncOperation, _GraphConfAsyncOperation]
_T4 = _Union[_GraphAttrSyncOperation, _GraphAttrAsyncOperation]

from ._context import GraphContext
from ._context import AsyncGraphContext
from ._context import GraphConfSyncContext
from ._context import GraphAttrSyncContext
from ._context import GraphConfAsyncContext
from ._context import GraphAttrAsyncContext

__all__ = [
    "GraphContext",
    "AsyncGraphContext",
    "GraphConfSyncContext",
    "GraphAttrSyncContext",
    "GraphConfAsyncContext",
    "GraphAttrAsyncContext"
]
