from copy import deepcopy
from typing import TypeVar, Generic

from ._batch import BaseBatch
from ._model import BaseModel

T = TypeVar("T", bound=BaseModel, covariant=True)


class BaseIter(Generic[T]):
    __model: T
    __loop: int
    __count: int
    __index: str
    __data: list
    __scroll: int
    __context: any
    __scroll_id: str

    def __batch(self):
        batch: BaseBatch = BaseBatch()
        for hit in self.__data:
            item: T = self.__model.__class__(**hit)
            context: any = deepcopy(self.__context)
            item.__objects__ = context
            context.model = item
            batch.add(item)
        return batch

    def __handle_response(self, response: dict):
        self.__scroll_id = response['_scroll_id']
        hits: list = response['hits']['hits']
        data: list = []
        for hit in hits:
            primary_key: str = self.__model.__default__.primary_key if self.__model.__meta__.primary_key is None else self.__model.__meta__.primary_key
            item: dict = hit['_source']
            item[primary_key] = hit['_id']
            data.append(item)
        self.__data = data
        self.__count = len(self.__data)

    def __init__(self, model: T, index: str, data: list, scroll: int, context: any, scroll_id: str):
        self.__loop = 0
        self.__data = data
        self.__model = model
        self.__index = index
        self.__scroll = scroll
        self.__count = len(data)
        self.__context = context
        self.__scroll_id = scroll_id

    def __iter__(self):
        return self

    def __aiter__(self):
        return self.__iter__()

    def __next__(self):
        if self.__count == 0 and self.__loop:
            raise StopIteration
        self.__loop += 1
        scroll_response: dict = self.__context.operation.scroll(self.__index, self.__context.auth, self.__scroll,
                                                                self.__scroll_id)
        batch: BaseBatch = self.__batch()
        self.__handle_response(scroll_response)
        return batch

    async def __anext__(self):
        if self.__count == 0 and self.__loop:
            raise StopAsyncIteration
        self.__loop += 1
        scroll_response: dict = await self.__context.operation.scroll(self.__index, self.__context.auth, self.__scroll,
                                                                      self.__scroll_id)
        batch: BaseBatch = self.__batch()
        self.__handle_response(scroll_response)
        return batch
