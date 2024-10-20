from . import _ABC
from . import _TypeVar
from . import _BaseBatch
from . import _BaseGraphAttrBasis
from . import _BaseGraphAttrIndex
from . import _BaseGraphAttrProperty


class BaseGraphAttrLabelsBasis(_BaseGraphAttrBasis, _ABC):
    class Types(_BaseGraphAttrBasis.Types):
        P = _TypeVar("P", bound=_BaseGraphAttrProperty, covariant=True)
        I = _TypeVar("I", bound=_BaseGraphAttrIndex, covariant=True)
        PS = _BaseBatch[P]
        NS = _BaseBatch[P]
        IS = _BaseBatch[I]
        TTL = int
        ELI = bool

    __properties: Types.PS
    __nullable_keys: Types.NS
    __index_labels: Types.IS
    __ttl: Types.TTL
    __enable_label_index: Types.ELI

    def __init__(self, name: str, **kwargs):
        super().__init__(name, **kwargs)

        self.__ttl = self.default("ttl", 0, **kwargs)
        self.__properties = _BaseBatch(self.default("properties", [], **kwargs))
        self.__index_labels = _BaseBatch(self.default("index_labels", [], **kwargs))
        self.__nullable_keys = _BaseBatch(self.default("nullable_keys", [], **kwargs))
        self.__enable_label_index = self.default("enable_label_index", False, **kwargs)

    @property
    def properties(self):
        return self.__properties

    @property
    def nullable_keys(self):
        return self.__nullable_keys

    @property
    def index_labels(self):
        return self.__index_labels

    @property
    def ttl(self):
        return self.__ttl

    @ttl.setter
    def ttl(self, value: int):
        self.__ttl = value

    @property
    def enable_label_index(self):
        return self.__enable_label_index

    @enable_label_index.setter
    def enable_label_index(self, value: bool):
        self.__enable_label_index = value
