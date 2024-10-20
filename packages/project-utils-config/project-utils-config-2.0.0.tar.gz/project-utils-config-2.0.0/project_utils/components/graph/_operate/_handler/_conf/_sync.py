from . import _T1
from . import _Any
from . import _json
from . import _Tuple
from . import _Union
from . import _Session
from . import _Optional
from . import _requests
from . import _Response
from . import _traceback
from . import _GraphException

from ._basis import BaseGraphConfOperation


class GraphConfSyncOperationHandler(BaseGraphConfOperation):
    def send(self, call: _Any, *args, **kwargs) -> _Tuple[int, _Union[dict, bytes, str, None]]:
        parser: str = kwargs.pop("parser") if "parser" in kwargs else "json"
        try:
            response: _Response = call(*args, **kwargs)
        except Exception as e:
            raise _GraphException(str(e), __file__, e.__traceback__.tb_lineno, _traceback.format_exc())
        resp: _Optional[str, bytes, dict] = None
        if parser == "json":
            resp: dict = response.json()
        elif parser == "bytes":
            resp: bytes = response.content
        elif parser == "str":
            resp: str = response.text
        return response.status_code, resp

    def show(self, name: str, auth: _T1):
        request_url: str = self.__utils__.show(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            status, graph_response = self.send(session.get, request_url)
        if status == 200:
            return graph_response
        raise _GraphException(graph_response['message'], __file__, 39)

    def clear(self, name: str, auth: _T1, confirm: str):
        request_url: str = self.__utils__.clear(self.__config__, name, confirm)
        with _requests.session() as session:
            session.auth = auth
            status, clear_response = self.send(session.delete, request_url, parser="str")
        if status == 204:
            return clear_response
        raise _GraphException(clear_response['message'], __file__, 48)

    def clone(self, clone_graph_name: str, body: str, auth: _T1):
        request_url = self.__utils__.clone(self.__config__, clone_graph_name)
        with _requests.session() as session:
            session.auth = auth
            session.headers = {"content-type": "text/plain"}
            status, clone_response = self.send(session.post, request_url, data=body)
        if status == 200:
            return clone_response
        raise _GraphException(clone_response['message'], __file__, 58, )

    def create(self, name: str, body: str, auth: _T1):
        request_url: str = self.__utils__.create(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            session.headers = {"content-type": "text/plain"}
            status, create_response = self.send(session.post, request_url, data=body)
        if status == 200:
            return create_response
        raise _GraphException(create_response['message'], __file__, 68)

    def delete(self, name: str, confirm: str, auth: _T1):
        request_url: str = self.__utils__.delete(self.__config__, name, confirm)
        with _requests.session() as session:
            session.auth = auth
            status, delete_response = self.send(session.delete, request_url, parser="str")
        if status == 204:
            return delete_response
        delete_response = _json.loads(delete_response)
        raise _GraphException(delete_response['message'], __file__, 78)

    def config(self, name: str, auth: _T1):
        request_url: str = self.__utils__.config(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            status, config_response = self.send(session.get, request_url, parser="str")
        if status == 200:
            return config_response
        response: dict = _json.loads(config_response)
        raise _GraphException(response['message'], __file__, 88)

    def get_mode(self, name: str, auth: _T1):
        request_url: str = self.__utils__.get_mode(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            mode_status, mode_response = self.send(session.get, request_url)
        if mode_status == 200:
            return mode_response
        raise _GraphException(mode_response['message'], __file__, 97)

    def get_read_mode(self, name: str, auth: _T1):
        request_url: str = self.__utils__.get_read_mode(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            mode_status, mode_response = self.send(session.get, request_url)
        if mode_status == 200:
            return mode_response
        raise _GraphException(mode_response['message'], __file__, 106)

    def snapshot_create(self, snapshot_name: str, hugegraph_name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.snapshot_create(self.__config__, snapshot_name,
                                                                                    hugegraph_name)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            snapshot_create_status, snapshot_create_response = self.send(session.put, request_url, json=request_body)
        if snapshot_create_status == 200:
            return snapshot_create_response
        raise _GraphException(snapshot_create_response['message'], __file__, 117)

    def snapshot_resume(self, snapshot_name: str, graph_name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.snapshot_resume(self.__config__, snapshot_name,
                                                                                    graph_name)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            resume_status, resume_response = self.send(session.put, request_url, json=request_body)
        if resume_status == 200:
            return resume_response
        raise _GraphException(resume_response['message'], __file__, 128)

    def compact(self, name: str, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.compact(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            compact_status, compact_response = self.send(session.put, request_url, json=request_body)
        if compact_status == 200:
            return compact_response
        raise _GraphException(compact_response['message'], __file__, 138)
