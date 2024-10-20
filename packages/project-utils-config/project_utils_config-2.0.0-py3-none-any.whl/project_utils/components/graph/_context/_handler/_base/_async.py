from . import _ABC
from . import _AsyncGraphOperation

from ._basis import BaseGraphContextHandler


class BaseGraphContextAsyncHandler(BaseGraphContextHandler, _ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__operation__ = _AsyncGraphOperation(self.__config__)
