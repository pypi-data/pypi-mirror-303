from . import _GraphConfAsyncContextHandler

from ._basis import BaseGraphConfContext


class GraphConfAsyncContext(BaseGraphConfContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphConfAsyncContextHandler(*args, **kwargs)

    async def show(self, *args, **kwargs):
        return await self.__handler__.show()

    async def clear(self, confirm: str = "I'm sure to delete all data"):
        return await self.__handler__.clear(confirm)

    async def clone(self, clone_graph_name: str = "hugegraph"):
        return await self.__handler__.clone(clone_graph_name)

    async def create(self, *args, **kwargs):
        return await self.__handler__.create(*args, **kwargs)

    async def delete(self, confirm: str = "I'm sure to drop the graph"):
        return await self.__handler__.delete(confirm)

    async def config(self, *args, **kwargs):
        return await self.__handler__.config(*args, **kwargs)

    async def get_mode(self, *args, **kwargs):
        return await self.__handler__.get_mode(*args, **kwargs)

    async def get_read_mode(self, *args, **kwargs):
        return await self.__handler__.get_read_mode(*args, **kwargs)

    async def snapshot_create(self, name: str):
        return await self.__handler__.snapshot_create(name)

    async def snapshot_resume(self, name: str):
        return await self.__handler__.snapshot_resume(name)

    async def compact(self, *args, **kwargs):
        return await self.__handler__.compact(*args, **kwargs)
