from . import _BaseGraphContextSyncHandler


class GraphContextSyncHandler(_BaseGraphContextSyncHandler):
    def graphs(self):
        self.__utils__.before_graphs()
        graphs_response: dict = self.__operation__.graphs(self.__auth__)
        return self.__utils__.after_graphs(graphs_response)
