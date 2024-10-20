from . import _ABC
from . import _GraphContextSyncHandler

from ._basis import BaseGraphContext


class BaseSyncGraphContext(BaseGraphContext, _ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphContextSyncHandler(*args, **kwargs)
