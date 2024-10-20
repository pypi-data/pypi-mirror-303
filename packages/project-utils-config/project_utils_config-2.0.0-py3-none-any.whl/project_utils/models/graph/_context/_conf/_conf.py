from . import _BaseGraphConf


class GraphConfContext(_BaseGraphConf):
    def to_dict(self):
        return {
            "store": self.store,
            "mode": self.mode.value,
            "wal_path": self.wal_path,
            "data_path": self.data_path,
            "read_mode": self.read_mode.value,
            "backend": self.backend,
            "serializer": "binary",
            "gremlin.graph": "org.apache.hugegraph.auth.HugeFactoryAuthProxy"
        }
