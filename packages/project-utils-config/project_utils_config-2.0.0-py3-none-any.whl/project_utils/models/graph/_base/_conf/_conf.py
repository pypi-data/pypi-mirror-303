from . import _Mode
from . import _ABCMeta
from . import _ReadMode
from . import _GraphContext
from . import _abstractmethod


class BaseGraphConf(metaclass=_ABCMeta):
    store: str
    mode: _Mode
    wal_path: str
    data_path: str
    backend = "rocksdb"
    read_mode: _ReadMode
    serializer = "binary"
    __objects__: _GraphContext
    gremlin_graph = "org.apache.hugegraph.auth.HugeFactoryAuthProxy"

    def __init__(self, name: str, wal_path: str, data_path: str, mode: _Mode = _Mode.NONE,
                 read_mode: _ReadMode = _ReadMode.ALL):
        self.mode = mode
        self.store = name
        self.wal_path = wal_path
        self.data_path = data_path
        self.read_mode = read_mode

    @_abstractmethod
    def to_dict(self):
        ...
