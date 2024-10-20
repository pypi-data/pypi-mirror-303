from abc import ABC, abstractmethod
from aiohttp.client import BasicAuth
from requests.auth import HTTPBasicAuth
from typing import Any, Optional, Union

from .._base import BaseGraph, Graph

T1 = Optional[Union[BasicAuth, HTTPBasicAuth]]


class BaseGraphSession(BaseGraph, ABC):
    __auth__: T1

    def __init__(self, graph: Graph, auth: T1 = None):
        self.__config__ = graph
        self.__auth__ = auth

    @abstractmethod
    def from_graph(self, m: Any, is_async: bool = False):
        ...

    @abstractmethod
    def graphs(self, **kwargs):
        ...

    @abstractmethod
    def async_graphs(self):
        ...