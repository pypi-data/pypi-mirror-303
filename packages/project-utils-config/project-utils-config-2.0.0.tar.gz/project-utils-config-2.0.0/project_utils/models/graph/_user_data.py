from . import _ABC
from . import _time
from . import _BaseMode


class BaseUserData(_BaseMode, _ABC):
    def __init__(self, **kwargs):
        create_time: str = kwargs['~create_time'].split(".")[0] if "~create_time" in kwargs else _time.datetime_to_str()
        super().__init__(create_time=_time.str_to_timestamp(create_time), **kwargs)


class DefaultUserData(BaseUserData):
    ...
