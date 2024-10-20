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

from ._basis import BaseGraphAttrOperation


class GraphAttrSyncOperationHandler(BaseGraphAttrOperation):
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

    def schema(self, name: str, auth: _T1):
        request_url: str = self.__utils__.schema(self.__config__, name)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 39)

    def create_property(self, name: str, body: dict, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.create_property(self.__config__, name, body)
        with _requests.session() as session:
            session.headers = request_headers
            session.auth = auth
            status, response = self.send(session.post, request_url, json=request_body)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 49)

    def create_vertex(self, store: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.create_vertex(self.__config__, store, **kwargs)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            status, response = self.send(session.post, request_url, json=request_body)
        if status == 201:
            return response
        raise _GraphException(response['message'], __file__, 59)

    def create_edge(self, store: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.create_edge(self.__config__, store, **kwargs)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            status, response = self.send(session.post, request_url, json=request_body)
        if status == 201:
            return response
        raise _GraphException(response['message'], __file__, 69)

    def append_property(self, property_name: str, action: str, graph_name: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.append_property(self.__config__, property_name,
                                                                                    action, graph_name, **kwargs)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            status, response = self.send(session.put, request_url, json=request_body)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 80)

    def append_vertex(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        request_url, request_headers, request_body = self.__utils__.append_vertex(self.__config__, name, action, store,
                                                                                  **kwargs)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            status, response = self.send(session.put, request_url, json=request_body)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 91)

    def append_edge(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        request_url, request_headers, request_body = self.__utils__.append_edges(self.__config__, name, action, store,
                                                                                 **kwargs)
        with _requests.session() as session:
            session.auth = auth
            session.headers = request_headers
            status, response = self.send(session.put, request_url, json=request_body)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 102)

    def query_properties(self, store: str, auth: _T1):
        request_url: str = self.__utils__.query_properties(self.__config__, store)
        session: _Session = _requests.session()
        session.auth = auth
        status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 69)

    def query_property(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.query_property(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 78)

    def query_vertexes(self, store: str, auth: _T1):
        request_url: str = self.__utils__.query_vertexes(self.__config__, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 129)

    def query_vertex(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.query_vertex(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 138)

    def query_edges(self, store: str, auth: _T1):
        request_url: str = self.__utils__.query_edges(self.__config__, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 147)

    def query_edge(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.query_edge(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 156)

    def delete_property(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_property(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.delete, request_url)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 87)

    def delete_vertex(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_vertex(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.delete, request_url)
            if status == 202:
                return response
            raise _GraphException(response['message'], __file__, 135)

    def delete_edge(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_edge(self.__config__, name, store)
        with _requests.session() as session:
            session.auth = auth
            status, response = self.send(session.delete, request_url)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 183)
