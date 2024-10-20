from . import _ABC
from . import _Any
from . import _Tuple
from . import _Response
from . import _traceback
from . import _GraphException

from ._basis import BaseGraphOperationHandler


class BaseGraphOperationSyncHandler(BaseGraphOperationHandler, _ABC):
    def send(self, call: _Any, *args, **kwargs) -> _Tuple[int, dict]:
        try:
            response: _Response = call(*args, **kwargs)
        except Exception as e:
            raise _GraphException(str(e), __file__, e.__traceback__.tb_lineno, _traceback.format_exc())
        return response.status_code, response.json()
