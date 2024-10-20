from . import _BaseGraphContextAsyncHandler


class GraphContextAsyncHandler(_BaseGraphContextAsyncHandler):
    async def graphs(self):
        self.__utils__.before_graphs()
        graphs_response: dict = await self.__operation__.graphs(self.__auth__)
        return self.__utils__.after_graphs(graphs_response)

