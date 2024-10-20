from . import _Graph

from ._base import BaseGraphOperationUtils


class GraphOperationUtils(BaseGraphOperationUtils):
    def graphs(self, graph: _Graph):
        return graph.to_url()
