from . import _T4
from . import _ABC
from . import _BaseGraphAttrContext
from . import _GraphAttrContextUtils


class BaseGraphAttrContext(_BaseGraphAttrContext, _ABC):
    __operation__: _T4
    __utils__: _GraphAttrContextUtils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphAttrContextUtils()
