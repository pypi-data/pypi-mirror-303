from typing import Optional

from .._session import ElasticSearchSession
from .._base import BaseElasticSearch, ElasticSearch


class ElasticSearchConnect(BaseElasticSearch):
    def __init__(self, host: str = "127.0.0.1", port: str = "9200", user: Optional[str] = None,
                 password: Optional[str] = None, ssl: bool = False):
        self.es_model = ElasticSearch(host=host, port=str(port), user=user, password=password, ssl=ssl)

    def session(self, is_async: bool = False):
        return ElasticSearchSession(self.es_model, is_async)
