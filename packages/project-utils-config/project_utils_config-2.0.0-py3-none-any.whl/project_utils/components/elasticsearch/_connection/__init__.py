from ._connection import ElasticSearchConnect

Connection = Connect = ElasticSearchConnect

__all__ = [
    "Connect",
    "Connection",
    "ElasticSearchConnect"
]
