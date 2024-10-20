from project_utils.models.graph import BaseUserData


class Author(BaseUserData):
    name: str
    age: int
    abstract:str

    def __init__(self, book_name: str):
        self.book_name = book_name
        super().__init__()
