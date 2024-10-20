import numpy as np

from typing import List, Tuple

from ._base import BaseFaissIndex
from .._base import T1

T3 = np.ndarray
T4 = Tuple[np.ndarray, np.ndarray]


class FaissIndex(BaseFaissIndex):
    def add(self, embedding: T1):
        vector: T3 = np.array([embedding], dtype=np.float32)
        faiss_id: int = self.get_faiss_id()
        self.index.add_with_ids(vector, [faiss_id])
        return faiss_id

    def add_items(self, embeddings: List[T1]):
        vector: T3 = np.array(embeddings, dtype=np.float32)
        faiss_ids: List[int] = [self.get_faiss_id() for i in range(len(embeddings))]
        self.index.add_with_ids(vector, faiss_ids)
        return faiss_ids

    def remove_from_index(self, faiss_id: int):
        self.index.remove_ids(np.arange(faiss_id))
        return self.index.ntotal

    def remove_from_element(self, faiss_id: int):
        return self.remove_from_index(faiss_id)

    def remove_from_faiss_id(self, faiss_id: int):
        return self.remove_from_index(faiss_id)

    def search(self, embedding: T1, top_k: int = 10):
        vector: T3 = np.array([embedding], dtype=np.float32)
        search_result: T4 = self.index.search(vector, top_k)
        scores: List[float] = [float(item) for item in search_result[0].tolist()[0]]
        faiss_ids: List[int] = [int(item) for item in search_result[1].tolist()[0]]
        return [{"faiss_id": faiss_ids[i], "score": scores[i]} for i in range(len(scores))]
