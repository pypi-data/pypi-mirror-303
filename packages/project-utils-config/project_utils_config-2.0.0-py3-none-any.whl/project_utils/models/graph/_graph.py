from . import _Any
from . import _Union

from ._types import Mode
from ._types import ReadMode
from ._basis import BaseGraph
from ._model import GraphConfModel
from ._model import GraphAttrSyncModel
from ._model import GraphAttrAsyncModel


class GraphModel(BaseGraph):
    __is_async: bool
    __conf__: GraphConfModel
    __attr__: _Union[GraphAttrSyncModel, GraphAttrAsyncModel]

    def __init__(
            self,
            name: str = "hugegraph",
            wal_path: str = "./data/logs",
            data_path: str = "./data/data",
            mode: Mode = Mode.NONE,
            read_mode: ReadMode = ReadMode.ALL,
            is_async: bool = False,
    ):
        self.__is_async = is_async
        self.__conf__ = GraphConfModel(name, wal_path, data_path, mode, read_mode)
        self.__conf__.__objects__ = self.__objects__
        self.__attr__ = GraphAttrAsyncModel() if self.__is_async else GraphAttrSyncModel()

    def context(self, context: _Any):
        self.__objects__ = context
        self.__conf__.__objects__ = context.__conf__
        self.__attr__.context(context.__attr__)

    def attribute(self, **kwargs):
        this = self

        class Client:
            def __enter__(self):
                this.__attr__.schema(**kwargs)
                return this.__attr__

            def __exit__(self, exc_type, exc_val, exc_tb):
                return False

            async def __aenter__(self):
                await this.__attr__.schema(**kwargs)
                return this.__attr__

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                return self.__exit__(exc_type, exc_val, exc_tb)

        return Client()
