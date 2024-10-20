from . import _Any

from ._base import BaseGraphContextUtils


class GraphAttrContextUtils(BaseGraphContextUtils):
    def before_schema(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_schema(self, response: dict):
        return response

    def before_create_property(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_create_property(self, response: dict):
        return response['property_key']

    def before_create_vertex(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_create_vertex(self, response: dict):
        return response

    def before_create_edge(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_create_edge(self, response: dict):
        return response

    def before_append_property(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_append_property(self, response: dict):
        return response['property_key']

    def before_append_vertex(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_append_vertex(self, response: dict):
        return response

    def before_append_edge(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_append_edge(self, response: dict):
        return response

    def before_query_properties(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_properties(self, response: dict):
        return response['propertykeys']

    def before_query_property(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_property(self, response: dict):
        return response

    def before_query_vertexes(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_vertexes(self, response: dict):
        return response['vertexlabels']

    def before_query_vertex(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_vertex(self, response: dict):
        return response

    def before_query_edges(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_edges(self, response: dict):
        return response['edgelabels']

    def before_query_edge(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_query_edge(self, response: dict):
        return response

    def before_delete_property(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_delete_property(self, response: dict):
        return response['task_id']

    def before_delete_vertex(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_delete_vertex(self, response: dict):
        return response['task_id']

    def before_delete_edge(self, m: _Any):
        from project_utils.models.graph import GraphModel
        model: GraphModel = m
        return model.__conf__.store

    def after_delete_edge(self, response: dict):
        return response['task_id']
