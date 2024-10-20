from . import _T3
from . import _ABC
from . import _BaseGraphConfContext
from . import _GraphConfContextUtils


class BaseGraphConfHandler(_BaseGraphConfContext, _ABC):
    __operation__: _T3
    __utils__: _GraphConfContextUtils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphConfContextUtils()
