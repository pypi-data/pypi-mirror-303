from .. import _Optional
from .. import _GraphAttrIndex
from .. import _BaseGraphAttrIndexCollection
from .. import _GraphAttrIndexCollectionAsyncContext


class GraphAttrIndexCollectionAsyncModel(_BaseGraphAttrIndexCollection):
    CHILD_CLASS = _GraphAttrIndex
    __context__: _GraphAttrIndexCollectionAsyncContext

    def __init__(self):
        self.__context__ = _GraphAttrIndexCollectionAsyncContext()

    async def create(self, item: CHILD_CLASS):
        ...

    async def query(self, name: _Optional[str] = None):
        ...

    async def delete(self, item: CHILD_CLASS):
        ...
