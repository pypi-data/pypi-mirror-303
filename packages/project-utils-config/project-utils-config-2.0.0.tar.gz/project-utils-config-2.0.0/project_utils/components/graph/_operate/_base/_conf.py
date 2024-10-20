from . import _T1
from . import _ABC
from . import _Graph
from . import _BaseGraph
from . import _abstractmethod


class BaseGraphConfOperation(_BaseGraph, _ABC):
    def __init__(self, graph: _Graph):
        self.__config__ = graph

    @_abstractmethod
    def show(self, *args, **kwargs):
        """查看某个图的信息"""

    @_abstractmethod
    def clear(self, *args, **kwargs):
        """清空某个图的全部数据，包括 schema、vertex、edge 和 index 等，该操作需要管理员权限"""

    @_abstractmethod
    def clone(self, *args, **kwargs):
        """克隆一个图 (管理员权限)"""

    @_abstractmethod
    def create(self, *args, **kwargs):
        """创建一个图，该操作需要管理员权限"""

    @_abstractmethod
    def delete(self, *args, **kwargs):
        """删除某个图及其全部数据 """

    @_abstractmethod
    def config(self, *args, **kwargs):
        """查看某个图的配置，该操作需要管理员权限"""

    @_abstractmethod
    def get_mode(self, *args, **kwargs):
        """查看某个图的模式"""

    @_abstractmethod
    def get_read_mode(self, *args, **kwargs):
        """查看某个图的读模式。"""

    @_abstractmethod
    def snapshot_create(self, *args, **kwargs):
        """创建快照"""

    @_abstractmethod
    def snapshot_resume(self, *args, **kwargs):
        """快照恢复"""

    @_abstractmethod
    def compact(self, *args, **kwargs):
        """手动压缩图，该操作需要管理员权限"""
