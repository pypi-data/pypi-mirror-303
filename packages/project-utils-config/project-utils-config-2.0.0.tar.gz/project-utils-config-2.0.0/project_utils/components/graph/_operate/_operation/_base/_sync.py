from . import _ABC
from . import _GraphOperationSyncHandler

from ._basis import BaseGraphOperation


class BaseSyncGraphOperation(BaseGraphOperation, _ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphOperationSyncHandler(*args, **kwargs)
