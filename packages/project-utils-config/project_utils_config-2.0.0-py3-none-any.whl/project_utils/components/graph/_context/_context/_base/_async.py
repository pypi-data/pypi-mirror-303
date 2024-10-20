from . import _ABC
from . import _GraphContextAsyncHandler

from ._basis import BaseGraphContext


class BaseAsyncGraphContext(BaseGraphContext,_ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphContextAsyncHandler(*args, **kwargs)
