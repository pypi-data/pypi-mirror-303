from . import _T2
from . import _BaseGraphConf
from . import _GraphConfContext


class GraphConfModel(_BaseGraphConf):
    __context__: _GraphConfContext
    __objects__: _T2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__context__ = _GraphConfContext(*args, **kwargs)

    def to_dict(self):
        return super().to_dict()

    def to_body(self):
        return f"""gremlin.graph={self.gremlin_graph}
                   backend={self.backend}
                   serializer={self.serializer}
                   store={self.store}
                   rocksdb.data_path={self.data_path}
                   rocksdb.wal_path={self.wal_path}"""
