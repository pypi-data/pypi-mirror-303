from . import _Optional
from . import _GraphAttrIndex
from . import _BaseGraphAttrIndexCollection


class GraphAttrIndexCollectionSyncContext(_BaseGraphAttrIndexCollection):
    CHILD_CLASS = _GraphAttrIndex

    def create(self, item: CHILD_CLASS):
        ...

    def append(self, **kwargs):
        ...

    def query(self, name: _Optional[str] = None):
        ...

    def delete(self, item: CHILD_CLASS):
        ...