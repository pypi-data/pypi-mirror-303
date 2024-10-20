from . import _ABC
from . import _TypeVar
from . import _Optional
from . import _BaseBatch
from . import _IdStrategy
from . import _GraphException
from . import _abstractmethod
from . import _BaseGraphAttrCollection

from ._basis import BaseGraphAttrLabelsBasis


class BaseGraphAttrVertex(BaseGraphAttrLabelsBasis, _ABC):
    class Types(BaseGraphAttrLabelsBasis.Types):
        SUPER = BaseGraphAttrLabelsBasis.Types
        IDS = _IdStrategy
        PKS = _BaseBatch[SUPER.P]

    __id_strategy: Types.IDS
    __primary_keys: Types.PKS

    def __init__(self, name: str, id_strategy: str = Types.IDS.PRIMARY_KEY.value, **kwargs):
        super().__init__(name, **kwargs)

        self.__id_strategy = self.Types.IDS(id_strategy)

        primary_keys: _Optional[BaseGraphAttrVertex.Types.PKS] = self.default("primary_keys", None, **kwargs)
        if self.id_strategy == self.Types.IDS.PRIMARY_KEY:
            summary: str = """When param "id_strategy" value is "PRIMARY KEY",param "primary_keys" must exists!"""
            assert primary_keys is not None, _GraphException(summary, __file__, 30)
        else:
            summary: str = """When param "id_strategy" value isn't "PRIMARY KEY",param "primary_keys" must is null!"""
            assert primary_keys is None, _GraphException(summary, __file__, 33)

        self.__primary_keys = _BaseBatch(primary_keys)

    @property
    def primary_keys(self):
        return self.__primary_keys

    @property
    def id_strategy(self):
        return self.__id_strategy

    @id_strategy.setter
    def id_strategy(self, value: str):
        self.__id_strategy = self.Types.IDS(value)


class BaseGraphAttrVertexCollection(_BaseGraphAttrCollection, _ABC):
    T = _TypeVar("T", bound=BaseGraphAttrVertex, covariant=True)
    CHILD_CLASS = T

    @_abstractmethod
    def create(self, **kwargs):
        """创建一个VertexLabel"""

    @_abstractmethod
    def append(self, **kwargs):
        """为已存在的VertexLabel添加properties或userdata，或者移除userdata（目前不支持移除properties）"""

    @_abstractmethod
    def query(self, **kwargs):
        """获取所有的VertexLabel """

    @_abstractmethod
    def delete(self, **kwargs):
        """根据name删除VertexLabel"""
