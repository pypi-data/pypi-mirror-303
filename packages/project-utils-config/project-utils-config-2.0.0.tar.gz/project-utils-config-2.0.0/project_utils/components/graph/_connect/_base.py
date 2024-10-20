from typing import Optional
from abc import ABC, abstractmethod

from .._base import BaseGraph, Graph


class BaseGraphConnect(BaseGraph):
    def __init__(
            self,
            host: str = "127.0.0.1",
            port: str = "8080",
            graph: str = "hugegraph",
            user: Optional[str] = None,
            password: Optional[str] = None,
            ssl: Optional[str] = None
    ):
        self.__config__ = Graph(host, port, graph, user, password, ssl)

    @abstractmethod
    def session(self):
        ...
