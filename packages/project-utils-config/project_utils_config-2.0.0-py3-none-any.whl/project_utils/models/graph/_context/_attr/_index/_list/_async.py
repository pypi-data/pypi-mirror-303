from . import _Optional
from . import _GraphAttrIndex
from . import _BaseGraphAttrIndexCollection


class GraphAttrIndexCollectionAsyncContext(_BaseGraphAttrIndexCollection):
    CHILD_CLASS = _GraphAttrIndex

    async def create(self, item: CHILD_CLASS):
        ...

    async def append(self, **kwargs):
        ...

    async def query(self, name: _Optional[str] = None):
        ...

    async def delete(self, item: CHILD_CLASS):
        ...
