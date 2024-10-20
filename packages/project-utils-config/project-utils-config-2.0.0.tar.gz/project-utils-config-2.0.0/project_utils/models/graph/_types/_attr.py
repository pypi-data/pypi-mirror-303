from . import _Enum


class DataType(_Enum):
    INT = "INT"
    BOOL = "BOOL"
    BYTE = "BYTE"
    LONG = "LONG"
    TEXT = "TEXT"
    DATE = "DATE"
    UUID = "UUID"
    BLOB = "BLOB"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"


class Cardinality(_Enum):
    SET = "SET"
    LIST = "LIST"
    SINGLE = "SINGLE"


class AggregateType(_Enum):
    NONE = "NONE"
    AVG = "AVG"
    MAX = "MAX"
    MIN = "MIN"
    SUM = "SUM"


class IdStrategy(_Enum):
    AUTOMATIC = "AUTOMATIC"
    PRIMARY_KEY = "PRIMARY_KEY"
    CUSTOMIZE_UUID = "CUSTOMIZE_UUID"
    CUSTOMIZE_STRING = "CUSTOMIZE_STRING"
    CUSTOMIZE_NUMBER = "CUSTOMIZE_NUMBER"


class Frequency(_Enum):
    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"


class BaseType(_Enum):
    EDGE_LABEL = "EDGE_LABEL"
    VERTEX_LABEL = "VERTEX_LABEL"


