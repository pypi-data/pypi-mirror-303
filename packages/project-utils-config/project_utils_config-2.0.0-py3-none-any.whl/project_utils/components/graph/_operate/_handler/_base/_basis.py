from . import _ABC
from . import _Any
from . import _abstractmethod
from . import _BaseGraphOperation
from . import _GraphOperationUtils


class BaseGraphOperationHandler(_BaseGraphOperation, _ABC):
    __utils__: _GraphOperationUtils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphOperationUtils()

    @_abstractmethod
    def send(self, call: _Any, *args, **kwargs):
        ...
