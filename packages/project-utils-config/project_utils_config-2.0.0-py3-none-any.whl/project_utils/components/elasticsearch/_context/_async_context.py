from typing import Optional

from ._base import BaseElasticSearchContext
from .._operation import AsyncElasticSearchOperation


class AsyncElasticSearchContext(BaseElasticSearchContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operation = AsyncElasticSearchOperation(self.es_model)

    async def create(self):
        index, settings, mappings = self.utils.before_create(self.model)
        create_response: dict = await self.operation.create(index, settings, mappings, self.auth)
        return self.utils.after_create(create_response)

    async def drop(self):
        index: str = self.utils.before_drop(self.model)
        delete_response: dict = await self.operation.drop(index, self.auth)
        return self.utils.after_drop(delete_response)

    async def indexes(self):
        index_response: str = await self.operation.indexes(self.auth)
        return index_response

    async def show(self):
        index: str = self.utils.before_show(self.model)
        index_response: dict = await self.operation.show(index, self.auth)
        return self.utils.after_show(index_response)

    async def save(self):
        index, primary_key, data = self.utils.before_insert(self.model)
        doc_id: str = getattr(self.model, primary_key)
        insert_response: dict = await self.operation.insert(index, doc_id, self.auth, **data)
        return self.utils.after_insert(insert_response, self.model)

    async def delete(self):
        index, primary_key = self.utils.before_delete(self.model)
        doc_id: str = getattr(self.model, primary_key)
        delete_response: dict = await self.operation.delete(index, doc_id, self.auth)
        return self.utils.after_delete(delete_response, self.model)

    async def get(self, doc_id: str):
        index, primary_key = self.utils.before_get(self.model)
        response: dict = await self.operation.get(index, doc_id, self.auth)
        model: Optional[any] = self.utils.after_get(response, self.model)
        setattr(model, primary_key, doc_id)
        if model:
            model.__objects__ = self
            self.model = model
        return model

    async def update(self):
        index, doc_id, data = self.utils.before_update(self.model)
        update_response: dict = await self.operation.update(index, doc_id, self.auth, **data)
        return self.utils.after_update(update_response, self.model)

    async def batch_insert(self, b: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseBatch
        batch: ElasticSearchBaseBatch = b
        index: str = self.utils.before_batch_insert(self.model)
        batch_insert_response: dict = await self.operation.batch_insert(index, self.auth, batch.to_params())
        return self.utils.after_batch_insert(batch_insert_response)

    async def batch_update(self, b: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseBatch
        batch: ElasticSearchBaseBatch = b
        index: str = self.utils.before_batch_update(self.model)
        batch_update_response: dict = await self.operation.batch_update(index, self.auth, batch.to_params("update"))
        return self.utils.after_batch_update(batch_update_response)

    async def batch_delete(self, mode: str = "match", **query):
        index: str = self.utils.before_batch_delete(self.model)
        batch_delete_response: dict = await self.operation.batch_delete(index, self.auth, mode, **query)
        return self.utils.after_batch_delete(batch_delete_response)

    async def all(self, _from: int = 0, _size: int = 10):
        index: str = self.utils.before_select_all(self.model)
        select_all_response: dict = await self.operation.all(index, self.auth, _from, _size)
        return self.utils.after_select_all(select_all_response, self.model, self)

    async def filter(self, mode: str = "match", _from: int = 0, _size: int = 10, **query):
        index: str = self.utils.before_select_filter(self.model)
        select_filter_response: dict = await self.operation.filter(index, self.auth, query, mode, _from, _size)
        return self.utils.after_select_filter(select_filter_response, self.model, self)

    async def filter_by(self, query: dict):
        index: str = self.utils.before_select_filter_by(self.model)
        select_filter_by_response: dict = await self.operation.filter_by(index, self.auth, query)
        return self.utils.after_select_filter_by(select_filter_by_response, self.model, self)

    async def scroll(self, scroll: int, mode: str = "match_all", _from: int = 0, _size: int = 1000, **query):
        index: str = self.utils.before_select_scroll(self.model)
        select_scroll_response: dict = await self.operation.scroll(index, self.auth, scroll, mode=mode, _from=_from,
                                                                   _size=_size, **query)
        print(select_scroll_response)
        return self.utils.after_select_scroll(scroll, index, self.model, self, select_scroll_response)
