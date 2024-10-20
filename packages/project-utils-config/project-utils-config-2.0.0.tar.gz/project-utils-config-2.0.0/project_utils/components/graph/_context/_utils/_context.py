from ._base import BaseGraphContextUtils


class GraphContextUtils(BaseGraphContextUtils):
    def before_graphs(self, **kwargs):
        ...

    def after_graphs(self, response: dict):
        return response['graphs']
