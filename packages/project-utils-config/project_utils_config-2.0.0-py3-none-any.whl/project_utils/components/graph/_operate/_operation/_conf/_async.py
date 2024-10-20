from . import _T1
from . import _GraphConfAsyncOperationHandler

from ._basis import BaseGraphConfOperation


class GraphConfAsyncOperation(BaseGraphConfOperation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphConfAsyncOperationHandler(*args, **kwargs)

    async def show(self, name: str, auth: _T1):
        return await self.__handler__.show(name, auth)

    async def clear(self, name: str, auth: _T1, confirm: str):
        return await self.__handler__.clear(name, auth, confirm)

    async def clone(self, clone_graph_name: str, body: str, auth: _T1):
        return await self.__handler__.clone(clone_graph_name, body, auth)

    async def create(self, name: str, body: str, auth: _T1):
        return await self.__handler__.create(name, body, auth)

    async def delete(self, name: str, confirm: str, auth: _T1):
        return await self.__handler__.delete(name, confirm, auth)

    async def config(self, name: str, auth: _T1):
        return await self.__handler__.config(name, auth)

    async def get_mode(self, name: str, auth: _T1):
        return await self.__handler__.get_mode(name, auth)

    async def get_read_mode(self, name: str, auth: _T1):
        return await self.__handler__.get_read_mode(name, auth)

    async def snapshot_create(self, snapshot_name: str, hugegraph_name, auth: _T1):
        return await self.__handler__.snapshot_create(snapshot_name, hugegraph_name, auth)

    async def snapshot_resume(self, snapshot_name: str, graph_name: str, auth: _T1):
        return await self.__handler__.snapshot_resume(snapshot_name, graph_name, auth)

    async def compact(self, name: str, auth: _T1):
        return await self.__handler__.compact(name, auth)
