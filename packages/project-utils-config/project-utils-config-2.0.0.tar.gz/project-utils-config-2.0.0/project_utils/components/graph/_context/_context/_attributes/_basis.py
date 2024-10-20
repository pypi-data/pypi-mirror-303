from . import _T4
from . import _ABC
from . import _BaseGraphAttrContext


class BaseGraphAttrContext(_BaseGraphAttrContext, _ABC):
    __handler__: _T4
