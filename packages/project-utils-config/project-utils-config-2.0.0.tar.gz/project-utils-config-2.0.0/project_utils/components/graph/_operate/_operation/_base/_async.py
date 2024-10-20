from . import _ABC
from . import _GraphOperationAsyncHandler

from ._basis import BaseGraphOperation


class BaseAsyncGraphOperation(BaseGraphOperation,_ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphOperationAsyncHandler(*args, **kwargs)
