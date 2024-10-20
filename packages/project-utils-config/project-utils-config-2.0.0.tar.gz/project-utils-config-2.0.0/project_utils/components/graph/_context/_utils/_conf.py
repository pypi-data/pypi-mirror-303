from . import _Any

from ._base import BaseGraphContextUtils


class GraphConfContextUtils(BaseGraphContextUtils):
    def before_show(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_show(self, response: dict):
        return response

    def before_clear(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_clear(self, response: dict):
        return response

    def before_clone(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.to_body()

    def after_clone(self, response: dict):
        return response

    def before_create(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store, model.__conf__.to_body()

    def after_create(self, response: dict):
        return response

    def before_delete(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_delete(self, response: dict):
        return response

    def before_config(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_config(self, response: str):
        return response

    def before_get_mode(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_get_mode(self, response: dict):
        return response['mode']

    def before_get_read_mode(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_get_read_mode(self, response: dict):
        return response['graph_read_mode']

    def before_snapshot_create(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_snapshot_create(self, snapshot_response: dict):
        return snapshot_response

    def before_snapshot_resume(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_snapshot_resume(self, resume_response: dict):
        return resume_response

    def before_compact(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_compact(self,compact_response:dict):
        return compact_response
