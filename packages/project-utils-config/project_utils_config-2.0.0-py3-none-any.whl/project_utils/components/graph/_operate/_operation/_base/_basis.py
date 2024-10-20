from . import _T2
from . import _ABC
from . import _BaseGraphOperation


class BaseGraphOperation(_BaseGraphOperation, _ABC):
    __handler__: _T2
