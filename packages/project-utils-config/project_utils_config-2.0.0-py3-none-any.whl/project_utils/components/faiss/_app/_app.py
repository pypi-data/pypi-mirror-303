from typing import List, Dict

from ._base import BaseFaissAPP
from .._base import T1, T2

T3 = List[Dict[str, int]]


class FaissAPP(BaseFaissAPP):
    def add(self, embedding: T1, item: T2):
        faiss_id: int = self.faiss_index.add(embedding)
        item.faiss_id = faiss_id
        self.faiss_store.add(item)
        return self.faiss_index.index.ntotal

    def add_items(self, embeddings: List[T1], items: List[T2]):
        faiss_ids: List[int] = self.faiss_index.add_items(embeddings)
        self.faiss_store.add_items(items, faiss_ids)
        return self.faiss_index.index.ntotal

    def remove_from_index(self, index: int):
        faiss_id: int = self.faiss_store.remove_from_index(index)
        print(faiss_id)
        return self.faiss_index.remove_from_index(faiss_id)

    def remove_from_element(self, element: T2):
        faiss_id: int = self.faiss_store.remove_from_element(element)
        return self.faiss_index.remove_from_element(faiss_id)

    def remove_from_faiss_id(self, faiss_id: int):
        _faiss_id = self.faiss_store.remove_from_faiss_id(faiss_id)
        return self.faiss_index.remove_from_faiss_id(faiss_id)

    def search(self, embedding: T1, top_k: int = 10):
        print(self.faiss_store.faiss_id_list)
        search_result: T3 = self.faiss_index.search(embedding, top_k)
        print(search_result)
        return self.faiss_store.search(search_result)
