from . import _T1
from . import _json
from . import _Session
from . import _requests
from . import _GraphException

from . import _BaseGraphOperationSyncHandler


class GraphOperationSyncHandler(_BaseGraphOperationSyncHandler):
    def graphs(self, auth: _T1 = None):
        request_url: str = self.__utils__.graphs(self.__config__)
        with _requests.session() as session:
            session.auth = auth
            status, graph_response = self.send(session.get, request_url)
        if status == 200:
            return graph_response
        raise _GraphException(graph_response['message'], __file__, 18, _json.dumps(graph_response, ensure_ascii=False))
