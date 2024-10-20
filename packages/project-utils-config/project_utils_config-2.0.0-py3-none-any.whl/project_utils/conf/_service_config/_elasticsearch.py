import traceback

from aiohttp import BasicAuth
from requests.auth import HTTPBasicAuth
from typing import List, Dict, Optional, Union

from ._base import BaseServiceConfig
from project_utils.exception import ServiceConfigException


class ElasticSearchService(BaseServiceConfig):
    user: Optional[str]
    password: Optional[str]
    indexes: List[str]
    relation: Dict[str, str]

    def __init__(
            self,
            user: Optional[str] = None,
            password: Optional[str] = None,
            indexes: Optional[str] = None,
            relation: Optional[str] = None,
            sep: str = ",",
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.user = user
        self.password = password
        self.relation = {}
        if indexes is None and relation is None:
            self.indexes = []
        else:
            indexes_: list = indexes.split(sep)
            relation_: list = relation.split(sep)
            assert len(indexes_) == len(relation_), ServiceConfigException(
                "The number of params indexes and relation must same.",
                __file__, 30
            )
            for item in relation_:
                item_split: list = item.split(":")
                try:
                    assert len(item_split) == 2
                    assert item_split[1].isdigit()
                except Exception as e:
                    raise ServiceConfigException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
                key: str = item_split[0]
                index: int = int(item_split[1])
                value: str = indexes_[index]
                self.relation[key] = value
            self.indexes = indexes_

    def get_index(self, key: Union[str, int], type: str = "index"):
        if type == "index":
            return self.indexes[key]
        else:
            return self.relation.get(key)

    def to_dict(self):
        result: dict = {
            "host": str(self.host),
            "port": str(self.port),
        }
        if self.user: result['user'] = str(self.user)
        if self.password: result['password'] = str(self.password)
        if self.ssl: result['ssl'] = "1"

    def auth(self):
        if self.user and self.password:
            return HTTPBasicAuth(self.user, self.password)
        else:
            return None

    def aio_auth(self):
        if self.user and self.password:
            return BasicAuth(self.user, self.password)
        else:
            return None
