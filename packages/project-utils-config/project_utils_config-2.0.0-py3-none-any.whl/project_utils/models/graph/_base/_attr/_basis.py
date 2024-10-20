from . import _T3
from . import _Any
from . import _List
from . import _Union
from . import _ABCMeta
from . import _TypeVar
from . import _Optional
from . import _BaseBatch
from . import _BaseUserData
from . import _abstractmethod


class BaseGraphAttrBasis(metaclass=_ABCMeta):
    class Types:
        ID = _Optional[int]
        STR = str
        STU = _Optional[str]
        UD = _Union[_TypeVar("UD", bound=_BaseUserData, covariant=True), dict]

    __id: Types.ID
    __name: Types.STR
    __status: Types.STU
    __user_data: Types.UD = {}

    def __init__(self, name: str, **kwargs):
        self.__name = name
        self.__id = self.default("id", None, **kwargs)
        self.__status = self.default("status", None, **kwargs)

    def default(self, name: str, value: _Any, **kwargs):
        return kwargs[name] if name in kwargs else value

    def to_params(self, fields: _List[str]):
        source: dict = self.to_dict()
        return {field: source[field] for field in fields}

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: Types.ID):
        self.__id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: Types.STU):
        self.__status = value

    @property
    def user_data(self):
        return self.__user_data

    @user_data.setter
    def user_data(self, value: Types.UD):
        self.__user_data = value

    @_abstractmethod
    def to_dict(self):
        ...

    @_abstractmethod
    def to_create(self):
        ...

    @_abstractmethod
    def to_user_data(self):
        ...


class BaseGraphAttrCollection(metaclass=_ABCMeta):
    T = _TypeVar("T")
    CHILD_CLASS: _Any
    __objects__: _T3
    __data__: _BaseBatch[T]

    def __init__(self):
        self.__data__ = _BaseBatch()

    @_abstractmethod
    def create(self, **kwargs):
        ...

    @_abstractmethod
    def append(self, **kwargs):
        ...

    @_abstractmethod
    def delete(self, **kwargs):
        ...

    @_abstractmethod
    def query(self, **kwargs):
        ...
