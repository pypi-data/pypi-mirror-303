from typing import List

from project_utils.models import BaseBatch
from project_utils.exception import FaissException
from project_utils.models.faiss import FaissBaseBatch

from .._base import T2
from ._base import BaseFaissStore, T3


class FaissStore(BaseFaissStore, FaissBaseBatch):
    def __init__(self, *args, **kwargs):
        BaseFaissStore.__init__(self)
        FaissBaseBatch.__init__(self, *args, **kwargs)

    def add(self, item: T2):
        self.faiss_id_list.append(item.faiss_id)
        return FaissBaseBatch.add(self, item)

    def add_items(self, items: List[T2], faiss_ids: List[int]):
        for i in range(len(items)):
            item: T2 = items[i]
            item.faiss_id = faiss_ids[i]
            self.faiss_id_list.append(faiss_ids[i])
        return FaissBaseBatch.add_items(self, items)

    def remove_from_index(self, index: int):
        element: T2 = FaissBaseBatch.remove_from_index(self, index)
        faiss_id: int = self.faiss_id_list.pop(index)
        try:
            assert element.faiss_id == faiss_id, FaissException(
                "The value of param faiss_id and param faiss_id of element can is not same!",
                __file__, 25, f"{element.faiss_id} and {faiss_id}"
            )
        except FaissException as e:
            self.add(element)
            raise e
        return faiss_id

    def remove_from_element(self, element: T2):
        element: T2 = FaissBaseBatch.remove_from_element(self, element)
        faiss_id: int = element.faiss_id
        index: int = self.faiss_id_list.index(faiss_id)
        self.faiss_id_list.pop(index)
        return faiss_id

    def remove_from_faiss_id(self, faiss_id: int):
        index: int = self.faiss_id_list.index(faiss_id)
        return self.remove_from_index(index)

    def search(self, search_data: T3):
        batch: BaseBatch[T2] = BaseBatch()
        for item in search_data:
            faiss_id: int = item['faiss_id']
            score: float = (1 - item['score']) * 1000
            index: int = self.faiss_id_list.index(faiss_id)
            element:T2 = self.data[index]
            element.score = score
            batch.add(element)
        return batch
