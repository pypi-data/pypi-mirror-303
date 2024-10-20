from . import _T1

from . import _BaseAsyncGraphOperation


class AsyncGraphOperation(_BaseAsyncGraphOperation):
    async def graphs(self, auth: _T1 = None):
        return await self.__handler__.graphs(auth)
