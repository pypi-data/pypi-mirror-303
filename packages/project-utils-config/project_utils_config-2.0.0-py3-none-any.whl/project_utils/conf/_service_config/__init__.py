from ._ftp import FTPConfig
from ._faiss import FaissConfig
from ._graph import GraphService
from ._service import ServiceConfig
from ._elasticsearch import ElasticSearchService

ftp = FTP = FTPConfig
faiss = Faiss = FaissConfig
graph = Graph = GraphService
service = Service = ServiceConfig
elasticsearch = ElasticSearch = ElasticSearchService

__all__ = [
    "elasticsearch",
    "ElasticSearch",
    "ElasticSearchService",
    "faiss",
    "Faiss",
    "FaissConfig",
    "ftp",
    "FTP",
    "FTPConfig",
    "graph",
    "Graph",
    "GraphService",
    "service",
    "Service",
    "ServiceConfig",
]
