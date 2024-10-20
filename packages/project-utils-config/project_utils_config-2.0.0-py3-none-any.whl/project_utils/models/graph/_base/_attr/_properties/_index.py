from . import _ABC
from . import _Union
from . import _TypeVar
from . import _Optional
from . import _BaseType
from . import _BaseBatch
from . import _abstractmethod

from . import _BaseGraphAttrBasis
from . import _BaseGraphAttrCollection


class BaseGraphAttrIndex(_BaseGraphAttrBasis, _ABC):
    class Types(_BaseGraphAttrBasis.Types):
        BT = _BaseType
        BV = _Union[str, int, bool]
        IT = _Optional[str]
        FS = _BaseBatch[str]

    __base_type: Types.BT
    __base_value: Types.BV
    __index_type: Types.IT
    __fields: Types.FS

    @property
    def fields(self):
        return self.__fields

    @property
    def base_type(self):
        return self.__base_type

    @base_type.setter
    def base_type(self, value: str):
        self.__base_type = self.Types.BT(value)

    @property
    def base_value(self):
        return self.__base_value

    @base_value.setter
    def base_value(self, value: Types.BV):
        self.__base_value = value

    @property
    def index_type(self):
        return self.__index_type

    @index_type.setter
    def index_type(self, value: Types.IT):
        self.__index_type = value


class BaseGraphAttrIndexCollection(_BaseGraphAttrCollection, _ABC):
    T = _TypeVar("T", bound=BaseGraphAttrIndex, covariant=True)
    CHILD_CLASS = T

    @_abstractmethod
    def create(self, item: CHILD_CLASS):
        """创建一个IndexLabel"""

    def append(self, **kwargs):
        """此方法无用"""

    @_abstractmethod
    def delete(self, item: CHILD_CLASS):
        """根据name删除 IndexLabel"""

    @_abstractmethod
    def query(self, name: _Optional[str] = None):
        """查询 IndexLabel"""
