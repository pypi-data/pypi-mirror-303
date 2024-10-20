from . import _T1
from . import _BaseSyncGraphOperation


class GraphOperation(_BaseSyncGraphOperation):
    def graphs(self, auth: _T1 = None):
        return self.__handler__.graphs(auth)
