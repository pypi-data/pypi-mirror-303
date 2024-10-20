from . import _BaseSyncGraphContext
from . import _GraphConfSyncContext
from . import _GraphAttrSyncContext


class GraphContext(_BaseSyncGraphContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__conf__ = _GraphConfSyncContext(*args, **kwargs)
        self.__attr__ = _GraphAttrSyncContext(*args, **kwargs)

    def graphs(self):
        return self.__handler__.graphs()
