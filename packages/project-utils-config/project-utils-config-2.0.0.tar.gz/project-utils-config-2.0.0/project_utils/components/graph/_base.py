from abc import ABCMeta

from project_utils.conf import Graph


class BaseGraph(metaclass=ABCMeta):
    __config__: Graph
