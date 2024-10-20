from . import _Graph

from ._base import BaseGraphOperationUtils


class GraphConfOperationUtils(BaseGraphOperationUtils):
    def show(self, graph: _Graph, name: str):
        return graph.to_url(name)

    def clear(self, graph: _Graph, name: str, confirm: str):
        return graph.to_url(name, "/clear", {"confirm_message": confirm})

    def clone(self, graph: _Graph, clone_graph_name: str):
        return graph.to_url(path="/hugegraph_clone", query_params={"clone_graph_name": clone_graph_name})

    def create(self, graph: _Graph, name: str):
        return graph.to_url(name)

    def delete(self, graph: _Graph, name: str, confirm: str):
        return graph.to_url(name, query_params={"confirm_message": confirm})

    def config(self, graph: _Graph, name: str):
        return graph.to_url(name, path="/conf")

    def get_mode(self, graph: _Graph, name: str):
        return graph.to_url(name, path="/mode")

    def get_read_mode(self, graph: _Graph, name: str):
        return graph.to_url(name, path="/graph_read_mode")

    def snapshot_create(self, graph: _Graph, snapshot_name: str, hugegraph_name: str):
        request_url: str = graph.to_url(hugegraph_name, path="/snapshot_create")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"name": snapshot_name}
        return request_url, request_headers, request_body

    def snapshot_resume(self, graph: _Graph, snapshot_name: str, graph_name: str):
        request_url: str = graph.to_url(graph_name, path="/snapshot_resume")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"name": snapshot_name}
        return request_url, request_headers, request_body

    def compact(self, graph: _Graph, name: str):
        request_url: str = graph.to_url(name, path="/compact")
        request_headers: dict = {"content-type": "application/json"}
        request_body: dict = {"name": name}
        return request_url, request_headers, request_body
