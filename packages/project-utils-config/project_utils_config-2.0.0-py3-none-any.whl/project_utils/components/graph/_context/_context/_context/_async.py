from . import _BaseAsyncGraphContext
from . import _GraphConfAsyncContext
from . import _GraphAttrAsyncContext


class AsyncGraphContext(_BaseAsyncGraphContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__conf__ = _GraphConfAsyncContext(*args, **kwargs)
        self.__attr__ = _GraphAttrAsyncContext(*args, **kwargs)

    async def graphs(self):
        return await self.__handler__.graphs()
