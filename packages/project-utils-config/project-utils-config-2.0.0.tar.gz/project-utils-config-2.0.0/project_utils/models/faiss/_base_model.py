from .._base_model import BaseModel as SourceModel


class BaseModel(SourceModel):
    faiss_id: int = 0
    score: float = 0
