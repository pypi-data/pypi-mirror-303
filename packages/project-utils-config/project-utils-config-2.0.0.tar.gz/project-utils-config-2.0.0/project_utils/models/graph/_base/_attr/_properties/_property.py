from . import _ABC
from . import _TypeVar
from . import _DataType
from . import _Optional
from . import _BaseBatch
from . import _Cardinality
from . import _AggregateType
from . import _abstractmethod
from . import _BaseGraphAttrBasis
from . import _BaseGraphAttrCollection


class BaseGraphAttrProperty(_BaseGraphAttrBasis, _ABC):
    class Types(_BaseGraphAttrBasis.Types):
        DT = _DataType
        C = _Cardinality
        AT = _AggregateType
        WT = _Optional[str]
        PS = _BaseBatch

    __data_type: Types.DT
    __cardinality: Types.C
    __aggregate_type: Types.AT
    __write_type: Types.WT
    __properties: Types.PS

    def __init__(
            self, name: str, data_type: str = Types.DT.TEXT.value,
            cardinality: str = Types.C.SINGLE.value,
            **kwargs
    ):
        super().__init__(name, **kwargs)

        self.__data_type = self.Types.DT(data_type)
        self.__cardinality = self.Types.C(cardinality)

        aggregate_type: str = self.Types.AT.NONE.value

        self.__aggregate_type = self.Types.AT(self.default("aggregate_type", aggregate_type, **kwargs))
        self.__write_type = self.default("write_type", None, **kwargs)
        self.__properties = _BaseBatch(self.default("properties", [], **kwargs))

    @property
    def properties(self):
        return self.__properties

    @property
    def write_type(self):
        return self.__write_type

    @write_type.setter
    def write_type(self, value: Types.WT):
        self.__write_type = value

    @property
    def aggregate_type(self):
        return self.__aggregate_type

    @aggregate_type.setter
    def aggregate_type(self, value: str):
        self.__aggregate_type = self.Types.AT(value)

    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, value: str):
        self.__cardinality = self.Types.C(value)

    @property
    def data_type(self):
        return self.__data_type

    @data_type.setter
    def data_type(self, value: str):
        self.__data_type = self.Types.DT(value)


class BaseGraphAttrPropertyCollection(_BaseGraphAttrCollection, _ABC):
    T = _TypeVar("T", bound=BaseGraphAttrProperty, covariant=True)
    BT = BaseGraphAttrProperty.Types
    CHILD_CLASS = T

    @_abstractmethod
    def create(self, **kwargs):
        """创建一个 PropertyKey"""

    @_abstractmethod
    def append(self, **kwargs):
        """为已存在的 PropertyKey 添加或移除 userdata"""

    @_abstractmethod
    def query(self, **kwargs):
        """获取 PropertyKey"""

    @_abstractmethod
    def delete(self, **kwargs):
        """删除 PropertyKey """
