from . import _Any
from . import _ABC
from . import _traceback
from . import _TCPConnector
from . import _GraphException

from ._basis import BaseGraphOperationHandler


class BaseGraphOperationAsyncHandler(BaseGraphOperationHandler, _ABC):
    connector: _TCPConnector = _TCPConnector(ssl=False)

    async def send(self, call: _Any, *args, **kwargs):
        try:
            async with call(*args, **kwargs) as response:
                return response.status, await response.json()
        except Exception as e:
            raise _GraphException(str(e), __file__, e.__traceback__.tb_lineno, _traceback.format_exc())
