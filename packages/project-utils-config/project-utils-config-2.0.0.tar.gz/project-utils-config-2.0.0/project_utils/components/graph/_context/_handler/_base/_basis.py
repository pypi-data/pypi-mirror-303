from . import _T2
from . import _ABC
from . import _BaseGraphContext
from . import _GraphContextUtils


class BaseGraphContextHandler(_BaseGraphContext, _ABC):
    __utils__: _GraphContextUtils
    __operation__: _T2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__utils__ = _GraphContextUtils()
