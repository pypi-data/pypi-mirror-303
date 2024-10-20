import json
import time

from typing import TypeVar, Generic, List

from ._model import BaseModel
from .._base_batch import BaseBatch as SourceBatch

T = TypeVar("T", bound=BaseModel, contravariant=True)


class BaseBatch(SourceBatch, Generic[T]):

    def __handle_insert(self, index: str, doc_id: str, item: T):
        head: dict = {"index": {"_index": index, "_type": "_doc", "_id": doc_id}}
        return "\n".join((json.dumps(head), item.to_json()))

    def __handle_update(self, index: str, doc_id: str, item: T):
        head: dict = {"update": {"_index": index, "_id": doc_id}}
        update_data: dict = {}
        source_data: dict = item.__source__
        cur_data: dict = item.to_dict()
        for key in source_data:
            if source_data[key] != cur_data[key]:
                update_data[key] = cur_data[key]
        update_data['update_time'] = int(time.time() * 1000)
        return "\n".join((json.dumps(head), json.dumps({"doc": update_data})))

    def to_data(self, operate_type: str = "insert"):
        es_params: List[str] = []
        for item in self.data:
            index: str = item.__meta__.name
            primary_key: str = item.__default__.primary_key if item.__meta__.primary_key is None else item.__meta__.primary_key
            doc_id: str = item.__getattribute__(primary_key)
            if operate_type == "insert":
                es_params.append(self.__handle_insert(index, doc_id, item))
            else:
                es_params.append(self.__handle_update(index, doc_id, item))
        return es_params

    def to_params(self, operate_type: str = "insert"):
        return "\n".join(self.to_data(operate_type)) + "\n"
