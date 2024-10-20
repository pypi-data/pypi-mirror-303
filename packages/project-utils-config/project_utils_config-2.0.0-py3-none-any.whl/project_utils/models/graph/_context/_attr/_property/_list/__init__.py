from .. import _Union
from .. import _Optional
from .. import _BaseGraphAttrPropertyCollection

from .._item import GraphAttrProperty as _GraphAttrProperty

from ._sync import GraphAttrPropertyCollectionSyncContext
from ._async import GraphAttrPropertyCollectionAsyncContext

PropertyContext = _Union[GraphAttrPropertyCollectionSyncContext, GraphAttrPropertyCollectionAsyncContext]

__all__ = [
    "PropertyContext",
    "GraphAttrPropertyCollectionSyncContext",
    "GraphAttrPropertyCollectionAsyncContext"
]
