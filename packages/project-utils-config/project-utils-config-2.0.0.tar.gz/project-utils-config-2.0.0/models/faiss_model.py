from project_utils.models.faiss import FaissBaseModel


class HomeItemModel(FaissBaseModel):
    name: str
    age: int
    gender: bool
