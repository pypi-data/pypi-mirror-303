from . import _ABC
from . import _Any
from . import _abstractmethod
from . import _BaseGraphAttrOperation
from . import _GraphAttrOperationUtils


class BaseGraphAttrOperation(_BaseGraphAttrOperation, _ABC):
    __utils__: _GraphAttrOperationUtils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphAttrOperationUtils()

    @_abstractmethod
    def send(self, call: _Any, *args, **kwargs):
        ...
