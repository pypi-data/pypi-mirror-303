from . import _Enum


class Mode(_Enum):
    NONE = "NONE"
    RESTORING = "RESTORING"
    MERGING = "MERGING"
    LOADING = "LOADING"


class ReadMode(_Enum):
    ALL = "ALL"
    OLTP_ONLY = "OLTP_ONLY"
    OLAP_ONLY = "OLAP_ONLY"
