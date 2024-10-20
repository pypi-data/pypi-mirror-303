from project_utils.exception import FaissException

from ._base import BaseServiceConfig


class FaissConfig(BaseServiceConfig):
    __dim: int
    __param: str

    def __init__(self, dim: str = "1024", param: str = "Flat"):
        super().__init__("0.0.0.0", "65535")
        assert dim.isdigit(), FaissException(f"The params value is {dim},value type require is integer,not other!",
                                             __file__, 14, dim)
        self.__dim = int(dim)
        self.__param = param

    def to_dict(self):
        return {
            "param": str(self.__param),
            "dim": str(self.__dim),
        }

    @property
    def dim(self):
        return self.__dim

    @property
    def param(self):
        return self.__param
