from . import _T1
from . import _Any
from . import _json
from . import _Tuple
from . import _Union
from . import _Optional
from . import _traceback
from . import _TCPConnector
from . import _ClientSession
from . import _GraphException

from ._basis import BaseGraphConfOperation


class GraphConfAsyncOperationHandler(BaseGraphConfOperation):
    async def send(self, call: _Any, *args, **kwargs) -> _Tuple[int, _Union[str, bytes, dict, None]]:
        parser: str = kwargs.pop("parser") if "parser" in kwargs else "json"
        try:
            async with call(*args, **kwargs) as response:
                resp: _Optional[_Union[str, bytes, dict]] = None
                if parser == "json":
                    resp = await response.json()
                elif parser == "str":
                    resp = await response.text()
                elif parser == "bytes":
                    resp = await response.content.read()
                return response.status, resp

        except Exception as e:
            raise _GraphException(str(e), __file__, e.__traceback__.tb_lineno, _traceback.format_exc())

    async def show(self, name: str, auth: _T1):
        request_url: str = self.__utils__.show(self.__config__, name)
        async with _ClientSession(auth=auth, connector=_TCPConnector(ssl=False)) as session:
            status, graphs_response = await self.send(session.get, request_url)
            if status == 200:
                return graphs_response
            raise _GraphException(graphs_response['message'], __file__, 12,
                                  _json.dumps(graphs_response, ensure_ascii=False))

    async def clear(self, name: str, auth: _T1, confirm: str):
        request_url: str = self.__utils__.clear(self.__config__, name, confirm)
        async with _ClientSession(auth=auth, connector=_TCPConnector(ssl=False)) as session:
            status, clear_response = await self.send(session.delete, request_url, parser="text")
            if status == 204:
                return clear_response
            raise _GraphException(
                summary=clear_response['message'],
                trace_file=__file__,
                trace_line=43
            )

    async def clone(self, clone_graph_name: str, body: str, auth: _T1):
        request_url: str = self.__utils__.clone(self.__config__, clone_graph_name)
        async with _ClientSession(auth=auth, connector=_TCPConnector(ssl=False)) as session:
            headers: dict = {"content-type": "text/plain"}
            status, clone_response = await self.send(session.post, request_url, data=body, headers=headers)
            if status == 200:
                return clone_response
            raise _GraphException(
                summary=clone_response['message'],
                trace_file=__file__,
                trace_line=60,
                detail=_json.dumps(clone_response, ensure_ascii=False)
            )

    async def create(self, name: str, body: str, auth: _T1):
        request_url: str = self.__utils__.create(self.__config__, name)
        request_headers: dict = {"content-type": "text/plain"}
        request_connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_connector, headers=request_headers) as session:
            status, create_response = await self.send(session.post, request_url, data=body)
            if status == 200:
                return create_response
            raise _GraphException(
                summary=create_response['message'],
                trace_file=__file__,
                trace_line=75,
                detail=_json.dumps(create_response, ensure_ascii=False)
            )

    async def delete(self, name: str, confirm: str, auth: _T1):
        request_url: str = self.__utils__.delete(self.__config__, name, confirm)
        request_connector: _TCPConnector = _TCPConnector(ssl=False)
        request_headers: dict = {"content-type": "text/plain"}
        async with _ClientSession(auth=auth, connector=request_connector, headers=request_headers) as session:
            status, delete_response = await self.send(session.delete, request_url)
            if status == 204:
                return delete_response
            delete_response = _json.loads(delete_response)
            raise _GraphException(
                summary=delete_response['message'],
                trace_file=__file__,
                trace_line=90,
                detail=_json.dumps(delete_response, ensure_ascii=False)
            )

    async def config(self, name: str, auth: _T1):
        request_url: str = self.__utils__.config(self.__config__, name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_tcp) as session:
            status, config_response = await self.send(session.get, request_url, parser="str")
            if status == 200:
                return config_response
            response: dict = _json.loads(config_response)
            raise _GraphException(
                summary=response['message'],
                trace_file=__file__,
                trace_line=105,
                detail=_json.dumps(config_response, ensure_ascii=False)
            )

    async def get_mode(self, name: str, auth: _T1):
        request_url: str = self.__utils__.get_mode(self.__config__, name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_tcp) as session:
            mode_get_status, mode_get_response = await self.send(session.get, request_url)
            if mode_get_status == 200:
                return mode_get_response
            raise _GraphException(
                summary=mode_get_response['message'],
                trace_file=__file__,
                trace_line=121,
                detail=_json.dumps(mode_get_response, ensure_ascii=False)
            )

    async def get_read_mode(self, name: str, auth: _T1):
        request_url: str = self.__utils__.get_read_mode(self.__config__, name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_tcp) as session:
            mode_get_status, mode_get_response = await self.send(session.get, request_url)
            if mode_get_status == 200:
                return mode_get_response
            raise _GraphException(
                summary=mode_get_response['message'],
                trace_file=__file__,
                trace_line=136,
                detail=_json.dumps(mode_get_response, ensure_ascii=False)
            )

    async def snapshot_create(self, snapshot_name: str, hugegraph_name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.snapshot_create(self.__config__, snapshot_name,
                                                                                    hugegraph_name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_tcp, headers=request_headers) as session:
            create_status, create_response = await self.send(session.put, request_url, data=_json.dumps(request_body))
            if create_status == 200:
                return create_response
            raise _GraphException(
                summary=create_response['message'],
                trace_file=__file__,
                trace_line=136,
                detail=_json.dumps(create_response, ensure_ascii=False)
            )

    async def snapshot_resume(self, snapshot_name: str, graph_name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.snapshot_resume(self.__config__, snapshot_name,
                                                                                    graph_name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=request_tcp) as session:
            resume_status, resume_response = await self.send(session.put, request_url, data=_json.dumps(request_body))
            if resume_status == 200:
                return resume_response
            raise _GraphException(
                summary=resume_response['message'],
                trace_file=__file__,
                trace_line=163,
                detail=_json.dumps(resume_response, ensure_ascii=False)
            )

    async def compact(self, name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.compact(self.__config__, name)
        request_tcp: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=request_tcp, headers=request_headers) as session:
            compact_status, compact_response = await self.send(session.put, request_url, data=_json.dumps(request_body))
            if compact_status == 200:
                return compact_response
            raise _GraphException(
                summary=compact_response['message'],
                trace_file=__file__,
                trace_line=177,
                detail=_json.dumps(compact_response, ensure_ascii=False)
            )
