from . import _T3
from . import _ABC
from . import _BaseGraphConfContext


class BaseGraphConfContext(_BaseGraphConfContext, _ABC):
    __handler__: _T3
