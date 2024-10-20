from . import _T4
from . import _ABC

from . import _BaseGraphAttrOperation


class BaseGraphAttrOperation(_BaseGraphAttrOperation, _ABC):
    __handler__: _T4
