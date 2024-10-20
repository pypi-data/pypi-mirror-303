from ._base import BaseGraphConnect

from .._session import GraphSession, T1


class GraphConnect(BaseGraphConnect):
    def session(self, auth: T1 = None):
        return GraphSession(self.__config__, auth)
