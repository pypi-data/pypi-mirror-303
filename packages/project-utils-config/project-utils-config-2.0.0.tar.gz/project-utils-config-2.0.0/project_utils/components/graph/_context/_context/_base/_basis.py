from . import _T2
from . import _ABC
from . import _BaseGraphContext


class BaseGraphContext(_BaseGraphContext, _ABC):
    __handler__: _T2
