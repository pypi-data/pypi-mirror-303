from . import _ABCMeta
from . import _GraphContext


class BaseGraph(metaclass=_ABCMeta):
    __objects__: _GraphContext = None
