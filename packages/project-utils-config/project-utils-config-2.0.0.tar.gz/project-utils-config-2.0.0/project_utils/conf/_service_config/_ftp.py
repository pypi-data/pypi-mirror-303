from typing import Optional

from ._base import BaseServiceConfig


class FTPConfig(BaseServiceConfig):
    __user: Optional[str]
    __password: Optional[str]

    def __init__(self, host: str = "localhost", port: str = "22", user: Optional[str] = None,
                 password: Optional[str] = None):
        super().__init__(host, port)
        self.__user = user
        self.__password = password

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    def to_dict(self):
        result = {"host": str(self.host), "port": str(self.port)}
        if self.user: result['user'] = str(self.__user)
        if self.password: result['password'] = str(self.__password)
        return result
