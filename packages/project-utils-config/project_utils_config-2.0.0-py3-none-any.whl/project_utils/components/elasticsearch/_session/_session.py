from aiohttp import BasicAuth
from typing import Union, Tuple

from .._base import BaseElasticSearch, ElasticSearch
from .._context import ElasticSearchContext, AsyncElasticSearchContext


class ElasticSearchSession(BaseElasticSearch):
    __is_async: bool
    T1 = Union[BasicAuth, Tuple[str, str], None]
    T2 = Union[ElasticSearchContext, AsyncElasticSearchContext]

    def __init__(self, es_model: ElasticSearch, is_async: bool):
        self.es_model = es_model
        self.__is_async = is_async

    def from_model(self, model: any, auth: T1 = None):
        instance: any = model()
        if self.__is_async:
            instance.__objects__ = AsyncElasticSearchContext(self.es_model, instance, auth=auth)
        else:
            instance.__objects__ = ElasticSearchContext(self.es_model, instance, auth=auth)
        return instance

    def show(self, auth: T1 = None):
        context: ElasticSearchContext = ElasticSearchContext(self.es_model, None, auth=auth)
        return context.indexes()

    async def async_show(self, auth: T1 = None):
        context: AsyncElasticSearchContext = AsyncElasticSearchContext(self.es_model, None, auth=auth)
        return await context.indexes()
