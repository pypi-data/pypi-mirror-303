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

from ._basis import BaseGraphAttrOperation


class GraphAttrAsyncOperationHandler(BaseGraphAttrOperation):
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

    async def schema(self, store: str, auth: _T1):
        request_url: str = self.__utils__.schema(self.__config__, store)
        ssl: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=ssl) as session:
            status, response = await self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 39)

    async def create_property(self, store: str, body: dict, auth: _T1):
        request_url, request_headers, request_body = self.__utils__.create_property(self.__config__, store, body)
        ssl: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=ssl, headers=request_headers) as session:
            status, response = await self.send(session.post, request_url, data=_json.dumps(request_body))
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 48)

    async def create_vertex(self, store: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.create_vertex(self.__config__, store, **kwargs)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=connector) as session:
            status, response = await self.send(session.post, request_url, data=_json.dumps(request_body))
        if status == 201:
            return response
        raise _GraphException(response['message'], __file__, 57)

    async def create_edge(self, store: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.create_edge(self.__config__, store, **kwargs)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=connector) as session:
            status, response = await self.send(session.post, request_url, data=_json.dumps(request_body))
        if status == 201:
            return response
        raise _GraphException(response['message'], __file__, 66)

    async def append_property(self, property_name: str, action: str, store: str, auth: _T1, **kwargs):
        request_url, request_body, request_headers = self.__utils__.append_property(self.__config__, property_name,
                                                                                    action, store, **kwargs)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=connector) as session:
            status, response = await self.send(session.put, request_url, data=_json.dumps(request_body))
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 76)

    async def append_vertex(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        request_url, request_headers, request_body = self.__utils__.append_vertex(self.__config__, name, action, store,
                                                                                  **kwargs)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=connector) as session:
            status, response = await self.send(session.put, request_url, data=_json.dumps(request_body))
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 86)

    async def append_edge(self, name: str, action: str, store: str, auth: _T1, **kwargs):
        request_url, request_headers, request_body = self.__utils__.append_edges(self.__config__, name, action, store,
                                                                                 **kwargs)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, headers=request_headers, connector=connector) as session:
            status, response = await self.send(session.put, request_url, data=_json.dumps(request_body))
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 96)

    async def query_properties(self, store: str, auth: _T1):
        request_url: str = self.__utils__.query_properties(self.__config__, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
            if status == 200:
                return response
        raise _GraphException(response['message'], __file__, 67)

    async def query_property(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.query_property(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
            if status == 200:
                return response
        raise _GraphException(response['message'], __file__, 75)

    async def query_vertexes(self, store: str, auth: _T1):
        request_url = self.__utils__.query_vertexes(self.__config__, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 113)

    async def query_vertex(self, name: str, store: str, auth: _T1):
        request_url = self.__utils__.query_vertex(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 122)

    async def query_edges(self, store: str, auth: _T1):
        request_url: str = self.__utils__.query_edges(self.__config__, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 141)

    async def query_edge(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.query_edge(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.get, request_url)
        if status == 200:
            return response
        raise _GraphException(response['message'], __file__, 150)

    async def delete_property(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_property(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.delete, request_url)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 85)

    async def delete_vertex(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_vertex(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.delete, request_url)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 131)

    async def delete_edge(self, name: str, store: str, auth: _T1):
        request_url: str = self.__utils__.delete_edge(self.__config__, name, store)
        connector: _TCPConnector = _TCPConnector(ssl=False)
        async with _ClientSession(auth=auth, connector=connector) as session:
            status, response = await self.send(session.delete, request_url)
        if status == 202:
            return response
        raise _GraphException(response['message'], __file__, 177)
