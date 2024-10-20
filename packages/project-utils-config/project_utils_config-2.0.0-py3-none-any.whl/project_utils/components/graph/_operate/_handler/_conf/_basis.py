from . import _ABC
from . import _Any
from . import _abstractmethod
from . import _BaseGraphConfOperation
from . import _GraphConfOperationUtils


class BaseGraphConfOperation(_BaseGraphConfOperation, _ABC):
    __utils__: _GraphConfOperationUtils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphConfOperationUtils()

    @_abstractmethod
    def send(self, call: _Any, *args, **kwargs):
        ...
