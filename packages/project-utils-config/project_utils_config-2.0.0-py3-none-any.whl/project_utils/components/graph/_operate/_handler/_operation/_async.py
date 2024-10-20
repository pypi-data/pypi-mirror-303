from . import _T1
from . import _json
from . import _ClientSession
from . import _GraphException

from . import _BaseGraphOperationAsyncHandler


class GraphOperationAsyncHandler(_BaseGraphOperationAsyncHandler):
    async def graphs(self, auth: _T1 = None):
        request_url: str = self.__utils__.graphs(self.__config__)
        async with _ClientSession(auth=auth, connector=self.connector) as session:
            status, graphs_response = await self.send(session.get, request_url)
            if status == 200:
                return graphs_response
            raise _GraphException(graphs_response['message'], __file__, 12,
                                  _json.dumps(graphs_response, ensure_ascii=False))
