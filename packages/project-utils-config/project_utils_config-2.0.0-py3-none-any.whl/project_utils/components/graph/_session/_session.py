from typing import Any, Union

from .._context import GraphContext, AsyncGraphContext
from ._base import BaseGraphSession

T1 = Union[GraphContext, AsyncGraphContext]


class GraphSession(BaseGraphSession):
    def from_graph(self, m: Any, is_async: bool = False):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        context: T1 = AsyncGraphContext(self.__config__, model, self.__auth__) \
            if is_async else GraphContext(self.__config__, model, self.__auth__)
        model.context(context)
        # model.context(context)
        return model

    def graphs(self):
        context: T1 = GraphContext(self.__config__, None, self.__auth__)
        return context.graphs()

    async def async_graphs(self):
        context: T1 = AsyncGraphContext(self.__config__, None, self.__auth__)
        return await context.graphs()
