from . import _ABC
from . import _GraphOperation

from ._basis import BaseGraphContextHandler


class BaseGraphContextSyncHandler(BaseGraphContextHandler, _ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__operation__ = _GraphOperation(self.__config__)
