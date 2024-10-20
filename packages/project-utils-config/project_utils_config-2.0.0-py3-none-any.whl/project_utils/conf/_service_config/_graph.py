from typing import Optional
from aiohttp import BasicAuth
from requests.auth import HTTPBasicAuth

from ._base import BaseServiceConfig


class GraphService(BaseServiceConfig):
    __graph: str
    __user: Optional[str]
    __password: Optional[str]

    def __init__(
            self,
            host: str = "127.0.0.1",
            port: str = "8080",
            graph: str = "hugegraph",
            user: Optional[str] = None,
            password: Optional[str] = None,
            ssl: Optional[str] = None
    ):
        super().__init__(host, port, ssl)
        self.__graph = graph
        self.__user = user
        self.__password = password

    def auth(self, is_async: bool = False):
        if self.__user and self.__password:
            return BasicAuth(self.__user, self.__password) if is_async else HTTPBasicAuth(self.__user, self.__password)

    @property
    def graph(self):
        return self.__graph

    def to_dict(self):
        result: dict = super().to_dict()
        result['graph'] = self.__graph
        if self.auth:
            result.update({"user": str(self.__user), "password": str(self.__password)})
        if self.ssl:
            result['ssl'] = "1"
        return result

    def to_url(self, graph: Optional[str] = None, path: Optional[str] = None, query_params: Optional[dict] = None):
        base_url: str = super().to_url()
        base_url += "/graphs"
        if graph:
            base_url += f"/{graph.strip('/')}"
        if path:
            base_url += f"/{path.strip('/')}"
        if query_params:
            base_url += "?"
            for key, val in query_params.items():
                base_url += f"{key}={val}&"
            base_url.strip("&")
        return base_url
