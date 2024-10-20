from . import _GraphConfSyncOperation

from ._basis import BaseGraphConfHandler


class GraphConfSyncContextHandler(BaseGraphConfHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__operation__ = _GraphConfSyncOperation(graph=self.__config__)

    def show(self, *args, **kwargs):
        name: str = self.__utils__.before_show(self.__model__)
        show_response: dict = self.__operation__.show(name, self.__auth__)
        return self.__utils__.after_show(show_response)

    def clear(self, confirm: str):
        name: str = self.__utils__.before_clear(self.__model__)
        clear_response: dict = self.__operation__.clear(name, self.__auth__, confirm)
        return self.__utils__.after_clear(clear_response)

    def clone(self, clone_graph_name: str):
        body: str = self.__utils__.before_clone(self.__model__)
        clone_response: dict = self.__operation__.clone(clone_graph_name, body, self.__auth__)
        return self.__utils__.after_clone(clone_response)

    def create(self, *args, **kwargs):
        name, body = self.__utils__.before_create(self.__model__)
        create_response: dict = self.__operation__.create(name, body, self.__auth__)
        return self.__utils__.after_create(create_response)

    def delete(self, confirm: str):
        name: str = self.__utils__.before_delete(self.__model__)
        delete_response: dict = self.__operation__.delete(name, confirm, self.__auth__)
        return self.__utils__.after_delete(delete_response)

    def config(self, *args, **kwargs):
        name: str = self.__utils__.before_config(self.__model__)
        config_response: str = self.__operation__.config(name, self.__auth__)
        return self.__utils__.after_config(config_response)

    def get_mode(self, *args, **kwargs):
        name: str = self.__utils__.before_get_mode(self.__model__)
        mode_get_response: dict = self.__operation__.get_mode(name, self.__auth__)
        return self.__utils__.after_get_mode(mode_get_response)

    def get_read_mode(self, *args, **kwargs):
        name: str = self.__utils__.before_get_read_mode(self.__model__)
        read_mode_response: dict = self.__operation__.get_read_mode(name, self.__auth__)
        return self.__utils__.after_get_read_mode(read_mode_response)

    def snapshot_create(self, name: str):
        snapshot_name: str = name
        hugegraph_name: str = self.__utils__.before_snapshot_create(self.__model__)
        snapshot_response: dict = self.__operation__.snapshot_create(snapshot_name, hugegraph_name, self.__auth__)
        return self.__utils__.after_snapshot_create(snapshot_response)

    def snapshot_resume(self, name: str):
        snapshot_name: str = name
        graph_name: str = self.__utils__.before_snapshot_resume(self.__model__)
        resume_response: dict = self.__operation__.snapshot_resume(snapshot_name, graph_name, self.__auth__)
        return self.__utils__.after_snapshot_resume(resume_response)

    def compact(self, *args, **kwargs):
        name: str = self.__utils__.before_compact(self.__model__)
        compact_response: dict = self.__operation__.compact(name, self.__auth__)
        return self.__utils__.after_compact(compact_response)
