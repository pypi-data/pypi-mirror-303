from typing import Tuple, Optional

from project_utils.conf import ElasticSearch


class OperationUtils:
    T1 = Tuple[str, dict, dict]
    T2 = Tuple[str, dict]

    def create(self, es_model: ElasticSearch, index: str, settings: dict, mappings: dict) -> T1:
        request_url: str = es_model.to_url(index)
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"settings": settings, "mappings": {"properties": mappings}}
        return request_url, request_headers, request_body

    def drop(self, es_model: ElasticSearch, index: str) -> T2:
        request_url: str = es_model.to_url(index)
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_headers

    def indexes(self, es_model: ElasticSearch) -> str:
        request_url: str = es_model.to_url(path="/_cat/indices", query_params={"v": "false"})
        return request_url

    def show(self, es_model: ElasticSearch, index: str) -> str:
        request_url: str = es_model.to_url(index)
        return request_url

    def insert(self, es_model: ElasticSearch, index: str, doc_id: str) -> T2:
        request_url: str = es_model.to_url(index, path=f"/_doc/{doc_id}")
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_headers

    def delete(self, es_model: ElasticSearch, index: str, doc_id: str) -> str:
        request_url: str = es_model.to_url(index, path=f"/_doc/{doc_id}")
        return request_url

    def get(self, es_model: ElasticSearch, index: str, doc_id: str) -> str:
        request_url: str = es_model.to_url(index, path=f"/_doc/{doc_id}")
        return request_url

    def update(self, es_model: ElasticSearch, index: str, doc_id: str, **data) -> T1:
        request_url: str = es_model.to_url(index, path=f"/_update/{doc_id}")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"doc": data.copy()}
        return request_url, request_headers, request_body

    def batch_insert(self, es_model: ElasticSearch, index: str) -> T2:
        request_url: str = es_model.to_url(index, path="/_bulk")
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_headers

    def batch_update(self, es_model: ElasticSearch, index: str) -> T2:
        request_url: str = es_model.to_url(index, path="/_bulk")
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_headers

    def batch_delete(self, es_model: ElasticSearch, index: str, mode: str, **query) -> T1:
        request_url: str = es_model.to_url(index, path="/_delete_by_query")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"query": {mode: query}}
        return request_url, request_headers, request_body

    def select_all(self, es_model: ElasticSearch, index: str, _from: int, _size: int) -> T1:
        request_url: str = es_model.to_url(index, path="/_search")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"query": {"match_all": {}}, "from": _from, "size": _size}
        return request_url, request_headers, request_body

    def filter(self, es_model: ElasticSearch, index: str, mode: str, _from: int, _size: int, query: dict) -> T1:
        request_url: str = es_model.to_url(index, path="/_search")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"query": {mode: query}}
        return request_url, request_headers, request_body

    def filter_by(self, es_model: ElasticSearch, index: str, query: dict) -> T1:
        request_url: str = es_model.to_url(index, path="/_search")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"query": query}
        return request_url, request_headers, request_body

    def first_scroll(self, es_model: ElasticSearch, index: str, scroll: int, mode, _from: int, _size: int,
                     **query) -> T1:
        request_url: str = es_model.to_url(index, path="/_search", query_params={"scroll": f"{scroll}m"})
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"query": {mode: query}, "from": _from, "size": _size}
        return request_url, request_headers, request_body

    def scroll(self, es_model: ElasticSearch, scroll: int, scroll_id: str) -> T1:
        request_url: str = es_model.to_url(path="/_search/scroll")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"scroll": f"{scroll}m", "scroll_id": scroll_id}
        return request_url, request_headers, request_body
