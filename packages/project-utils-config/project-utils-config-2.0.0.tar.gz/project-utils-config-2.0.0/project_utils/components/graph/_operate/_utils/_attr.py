from . import _Graph

from ._base import BaseGraphOperationUtils


class GraphAttrOperationUtils(BaseGraphOperationUtils):
    def schema(self, graph: _Graph, name: str):
        request_url: str = graph.to_url(name, path="/schema")
        return request_url

    def create_property(self, graph: _Graph, name: str, body: dict):
        request_url: str = graph.to_url(name, path="/schema/propertykeys")
        request_body: dict = body
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_headers, request_body

    def create_vertex(self, graph: _Graph, store: str, **kwargs):
        request_url: str = graph.to_url(store, path="/schema/vertexlabels")
        request_body: dict = kwargs
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_body, request_headers

    def create_edge(self, graph: _Graph, store: str, **kwargs):
        request_url: str = graph.to_url(store, path="/schema/edgelabels")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = kwargs
        return request_url, request_body, request_headers

    def append_property(self, graph: _Graph, property_name: str, action: str, graph_name: str, **kwargs):
        request_url: str = graph.to_url(graph_name, path=f"/schema/propertykeys/{property_name}",
                                        query_params={"action": action})
        request_body: dict = kwargs
        request_headers: dict = {"content-type": "application/json"}
        return request_url, request_body, request_headers

    def append_vertex(self, graph: _Graph, name: str, action: str, store: str, **kwargs):
        request_url: str = graph.to_url(store, path=f"/schema/vertexlabels/{name}", query_params={"action": action})
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"name": name}
        request_body.update(kwargs)
        return request_url, request_headers, request_body

    def append_edges(self, graph: _Graph, name: str, action: str, store: str, **kwargs):
        request_url: str = graph.to_url(store, path=f"/schema/edgelabels/{name}", query_params={"action": action})
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"name": name}
        request_body.update(kwargs)
        return request_url, request_headers, request_body

    def query_properties(self, graph: _Graph, store: str):
        return graph.to_url(store, path="/schema/propertykeys")

    def query_property(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/propertykeys/{name}")

    def query_vertexes(self, graph: _Graph, store: str):
        return graph.to_url(store, path="/schema/vertexlabels")

    def query_vertex(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/vertexlabels/{name}")

    def query_edges(self, graph: _Graph, store: str):
        return graph.to_url(store, path="/schema/edgelabels")

    def query_edge(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/edgelabels/{name}")

    def delete_property(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/propertykeys/{name}")

    def delete_vertex(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/vertexlabels/{name}")

    def delete_edge(self, graph: _Graph, name: str, store: str):
        return graph.to_url(store, path=f"/schema/edgelabels/{name}")
