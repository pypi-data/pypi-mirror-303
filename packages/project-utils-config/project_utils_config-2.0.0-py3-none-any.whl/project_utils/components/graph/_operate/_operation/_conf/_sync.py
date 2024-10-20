from . import _T1
from . import _GraphConfSyncOperationHandler

from ._basis import BaseGraphConfOperation


class GraphConfSyncOperation(BaseGraphConfOperation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphConfSyncOperationHandler(*args, **kwargs)

    def show(self, name: str, auth: _T1):
        return self.__handler__.show(name, auth)

    def clear(self, name: str, auth: _T1, confirm: str):
        return self.__handler__.clear(name, auth, confirm)

    def clone(self, clone_graph_name: str, body: str, auth: _T1):
        return self.__handler__.clone(clone_graph_name, body, auth)

    def create(self, name: str, body: str, auth: _T1):
        return self.__handler__.create(name, body, auth)

    def delete(self, name: str, confirm: str, auth: _T1):
        return self.__handler__.delete(name, confirm, auth)

    def config(self, name: str, auth: _T1):
        return self.__handler__.config(name, auth)

    def get_mode(self, name: str, auth: _T1):
        return self.__handler__.get_mode(name, auth)

    def get_read_mode(self, name: str, auth: _T1):
        return self.__handler__.get_read_mode(name, auth)

    def snapshot_create(self, snapshot_name: str, hugegraph_name: str, auth: _T1):
        return self.__handler__.snapshot_create(snapshot_name, hugegraph_name, auth)

    def snapshot_resume(self, snapshot_name: str, graph_name: str, auth: _T1):
        return self.__handler__.snapshot_resume(snapshot_name, graph_name, auth)

    def compact(self, name: str, auth: _T1):
        return self.__handler__.compact(name, auth)
