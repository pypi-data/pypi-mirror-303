from ._base import BaseProjectUtilsException


class ServiceException(BaseProjectUtilsException):
    ...


class ElasticSearchException(ServiceException):
    ...


class FaissException(ServiceException):
    ...


class FTPException(ServiceException):
    ...


class GraphException(ServiceException):
    ...
