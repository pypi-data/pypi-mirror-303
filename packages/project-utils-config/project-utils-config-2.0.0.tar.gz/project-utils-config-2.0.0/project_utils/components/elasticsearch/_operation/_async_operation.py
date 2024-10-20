import json
import traceback

from typing import Optional
from aiohttp import BasicAuth
from aiohttp.client import ClientSession
from aiohttp.connector import TCPConnector

from project_utils.exception import ElasticSearchException

from ._base import BaseElasticSearchOperation


class AsyncElasticSearchOperation(BaseElasticSearchOperation):
    T1 = Optional[BasicAuth]

    async def create(self, index: str, settings: Optional[dict] = None, mappings: Optional[dict] = None,
                     auth: T1 = None):
        request_url, request_headers, request_body = self.utils.create(self.es_model, index, settings, mappings)
        async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.put(request_url, data=json.dumps(request_body)) as response:
                    create_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return create_response

    async def drop(self, index: str, auth: T1 = None):
        request_url, request_headers = self.utils.drop(self.es_model, index)
        async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.delete(request_url) as response:
                    delete_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return delete_response

    async def indexes(self, auth: T1 = None):
        request_url: str = self.utils.indexes(self.es_model)
        async with ClientSession(auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.get(request_url) as response:
                    index_response: str = await response.text()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return index_response

    async def show(self, index: str, auth: T1):
        request_url: str = self.utils.show(self.es_model, index)
        async with ClientSession(auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.get(request_url) as response:
                    index_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return index_response

    async def insert(self, index: str, doc_id: str, auth: T1, **kwargs):
        request_url, request_headers = self.utils.insert(self.es_model, index, doc_id)
        request_body: dict = kwargs.copy()
        async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    insert_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return insert_response

    async def delete(self, index: str, doc_id: str, auth: T1):
        request_url: str = self.utils.delete(self.es_model, index, doc_id)
        async with ClientSession(auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.delete(request_url) as response:
                    delete_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return delete_response

    async def get(self, index: str, doc_id: str, auth: T1):
        request_url: str = self.utils.get(self.es_model, index, doc_id)
        async with ClientSession(auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.get(request_url) as response:
                    data_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return data_response

    async def update(self, index: str, doc_id: str, auth: T1, **data):
        request_url, request_headers, request_body = self.utils.update(self.es_model, index, doc_id, **data)
        async with ClientSession(auth=auth, headers=request_headers, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    update_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return update_response

    async def batch_insert(self, index: str, auth: T1, params: str):
        request_url, request_headers = self.utils.batch_insert(self.es_model, index)
        async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.post(request_url, data=params) as response:
                    batch_insert_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return batch_insert_response

    async def batch_update(self, index: str, auth: T1, params: str):
        request_url, request_headers = self.utils.batch_insert(self.es_model, index)
        async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.post(request_url, data=params) as response:
                    batch_update_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return batch_update_response

    async def batch_delete(self, index: str, auth: T1, mode: str = "match", **query):
        request_url, request_headers, request_body = self.utils.batch_delete(self.es_model, index, mode, **query)
        try:
            async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    return await response.json()
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())

    async def all(self, index: str, auth: T1, _from: int = 0, _size: int = 10):
        request_url, request_headers, request_body = self.utils.select_all(self.es_model, index, _from, _size)
        async with ClientSession(auth=auth, headers=request_headers, connector=TCPConnector(ssl=False)) as session:
            try:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    select_all_response: dict = await response.json()
            except Exception as e:
                raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
            return select_all_response

    async def filter(self, index: str, auth: T1, query: dict, mode: str = "match", _from: int = 0, _size: int = 0):
        request_url, request_headers, request_body = self.utils.filter(self.es_model, index, mode, _from, _size, query)
        try:
            async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    return await response.json()
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())

    async def filter_by(self, index: str, auth: T1, query: dict):
        request_url, request_headers, request_body = self.utils.filter_by(self.es_model, index, query)
        try:
            async with ClientSession(headers=request_headers, auth=auth, connector=TCPConnector(ssl=False)) as session:
                async with session.post(request_url, data=json.dumps(request_body)) as response:
                    return await response.json()
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())

    async def scroll(self, index: str, auth: T1, scroll: int, scroll_id: Optional[str] = None, mode: str = "match_all",
                     _from: int = 0, _size: int = 1000, **query):
        if scroll_id is None:
            request_url, request_headers, request_body = self.utils.first_scroll(self.es_model, index, scroll, mode,
                                                                                 _from, _size, **query)
        else:
            request_url, request_headers, request_body = self.utils.scroll(self.es_model, scroll, scroll_id)
        try:
            async with ClientSession(headers=request_headers,auth=auth,connector=TCPConnector(ssl=False)) as session:
                async with session.post(request_url,data=json.dumps(request_body)) as response:
                    return await response.json()
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())