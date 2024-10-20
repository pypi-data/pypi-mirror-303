from . import _GraphConfSyncContextHandler

from ._basis import BaseGraphConfContext


class GraphConfSyncContext(BaseGraphConfContext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler__ = _GraphConfSyncContextHandler(*args, **kwargs)

    def show(self, *args, **kwargs):
        return self.__handler__.show()

    def clear(self, confirm: str = "I'm sure to delete all data"):
        return self.__handler__.clear(confirm)

    def clone(self, clone_graph_name: str = "hugegraph"):
        return self.__handler__.clone(clone_graph_name)

    def create(self, *args, **kwargs):
        return self.__handler__.create(*args, **kwargs)

    def delete(self, confirm: str = "I'm sure to drop the graph"):
        return self.__handler__.delete(confirm)

    def config(self, *args, **kwargs):
        return self.__handler__.config(*args, **kwargs)

    def get_mode(self, *args, **kwargs):
        return self.__handler__.get_mode(*args, **kwargs)

    def get_read_mode(self, *args, **kwargs):
        return self.__handler__.get_read_mode(*args, **kwargs)

    def snapshot_create(self, name: str):
        return self.__handler__.snapshot_create(name)

    def snapshot_resume(self, name: str):
        return self.__handler__.snapshot_resume(name)

    def compact(self, *args, **kwargs):
        return self.__handler__.compact(*args, **kwargs)
