from . import _ABC
from . import _TypeVar
from . import _Optional
from . import _Frequency
from . import _BaseBatch
from . import _abstractmethod
from . import _BaseGraphAttrCollection

from ._vertex import BaseGraphAttrVertex
from ._basis import BaseGraphAttrLabelsBasis


class BaseGraphAttrEdge(BaseGraphAttrLabelsBasis, _ABC):
    class Types(BaseGraphAttrLabelsBasis.Types):
        SUPER = BaseGraphAttrLabelsBasis.Types
        SL = _TypeVar("SL", bound=BaseGraphAttrVertex, covariant=True)
        TL = _TypeVar("TL", bound=BaseGraphAttrVertex, covariant=True)
        F = _Frequency
        SKS = _BaseBatch[SUPER.P]

    __source_label: Types.SL
    __target_label: Types.TL
    __frequency: Types.F
    __sort_keys: Types.SKS

    def __init__(self, name: str, source_label: Types.SL, target_label: Types.TL, **kwargs):
        super().__init__(name, **kwargs)

        self.__source_label = source_label
        self.__target_label = target_label

        self.__frequency = self.Types.F(self.default("frequency", self.Types.F.SINGLE.value, **kwargs))
        self.__sort_keys = _BaseBatch(self.default("sort_keys", [], **kwargs))

    @property
    def sort_keys(self):
        return self.__sort_keys

    @property
    def source_label(self):
        return self.__source_label

    @source_label.setter
    def source_label(self, value: Types.SL):
        self.__source_label = value

    @property
    def target_label(self):
        return self.__target_label

    @target_label.setter
    def target_label(self, value: Types.TL):
        self.__target_label = value

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value: str):
        self.__frequency = self.Types.F(value)


class BaseGraphAttrEdgeCollection(_BaseGraphAttrCollection, _ABC):
    T = _TypeVar("T", bound=BaseGraphAttrEdge, covariant=True)
    CHILD_CLASS = T

    @_abstractmethod
    def create(self, **kwargs):
        """创建一个EdgeLabel"""

    @_abstractmethod
    def append(self, **kwargs):
        """"""
        """为已存在的EdgeLabel添加properties或userdata，或者移除userdata（目前不支持移除properties）"""

    @_abstractmethod
    def query(self, **kwargs):
        """查询 EdgeLabel"""

    @_abstractmethod
    def delete(self, item: CHILD_CLASS):
        """根据name删除EdgeLabel"""
