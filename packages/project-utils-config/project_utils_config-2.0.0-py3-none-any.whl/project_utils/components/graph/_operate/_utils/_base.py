from . import _ABCMeta


class BaseGraphOperationUtils(metaclass=_ABCMeta):
    request_headers: dict = {"content-type": "application/json"}
