from .. import _Optional
from .. import _GraphAttrIndex
from .. import _BaseGraphAttrIndexCollection
from .. import _GraphAttrIndexCollectionSyncContext


class GraphAttrIndexCollectionSyncModel(_BaseGraphAttrIndexCollection):
    CHILD_CLASS = _GraphAttrIndex
    __context__: _GraphAttrIndexCollectionSyncContext

    def __init__(self):
        self.__context__ = _GraphAttrIndexCollectionSyncContext()

    def create(self, item: CHILD_CLASS):
        ...

    def query(self, name: _Optional[str] = None):
        ...

    def delete(self, item: CHILD_CLASS):
        ...
