import uuid
import time
import json
import zlib
import base64

from abc import ABCMeta

from project_utils.exception import BaseModelException
from project_utils.utils import io


class BaseModel(metaclass=ABCMeta):
    doc_id: str
    create_user: str
    create_time: int
    update_user: str
    update_time: int
    is_delete: bool
    remake: str

    def get_doc_id(self):
        return uuid.uuid4().hex

    def __init__(self, **kwargs):
        init_field: list = ["doc_id", "create_user", "create_time", "update_user", "update_time", "is_delete", "remake"]
        self.doc_id = kwargs.pop("doc_id") if "doc_id" in kwargs else self.get_doc_id()
        self.create_user = kwargs.pop("create_user") if "create_user" in kwargs else "admin"
        self.create_time = int(kwargs.pop("create_time")) if "create_time" in kwargs else int(time.time() * 1000)
        self.update_user = kwargs.pop("update_user") if "update_user" in kwargs else "admin"
        self.update_time = int(kwargs.pop("update_time")) if "update_time" in kwargs else int(time.time() * 1000)
        self.is_delete = bool(kwargs.pop("is_delete")) if "is_delete" in kwargs else False
        self.remake = kwargs.pop("remake") if "remake" in kwargs else ""
        params: dict = {key: val for key, val in self.__annotations__.items() if not key.startswith("__")}
        for name, value_type in params.items():
            if name in init_field:
                continue
            elif name in kwargs:
                if value_type == bool: kwargs[name] = bool(kwargs[name])
                assert type(kwargs[name]) == value_type, BaseModelException(
                    f"Params {name} value type require {str(value_type)},cur value is {kwargs[name]}!", __file__, 31
                )
                self.__setattr__(name, kwargs[name])
            else:
                try:
                    self.__setattr__(name, self.__getattribute__(name))
                except:
                    self.__setattr__(name, value_type(None))

    def to_dict(self):
        result: dict = self.__dict__
        result_copy: dict = result.copy()
        for key in result:
            if key.startswith("__"):
                result_copy.pop(key)
            elif type(result[key]) == bool:
                result_copy[key] = int(result[key])
        return result_copy

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def to_bytes(self, encoding: str = "utf-8"):
        return self.to_json().encode(encoding=encoding)

    def to_base64(self, encoding: str = "utf-8"):
        return base64.b64encode(self.to_bytes(encoding=encoding))

    def compress(self, encoding: str = "utf-8"):
        return zlib.compress(self.to_base64(encoding=encoding))

    def to_code(self, encoding: str = "utf-8"):
        return io.md5_encode(self.to_json(), encoding=encoding)

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def from_json(cls, data: str):
        return cls.from_dict(**json.loads(data))

    @classmethod
    def from_bytes(cls, data: bytes, encoding: str = "utf-8"):
        json_str: str = data.decode(encoding=encoding)
        return cls.from_json(json_str)

    @classmethod
    def from_base64(cls, data: bytes, encoding: str = "utf-8"):
        byte_data: bytes = base64.b64decode(data)
        return cls.from_bytes(byte_data, encoding=encoding)

    @classmethod
    def decompress(cls, data: bytes, encoding: str = "utf-8"):
        base64_code: bytes = zlib.decompress(data)
        return cls.from_base64(base64_code, encoding=encoding)
