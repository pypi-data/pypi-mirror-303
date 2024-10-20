from .template import ConfigTemplate, BaseSystem
from ._service_config import ElasticSearch, Service, Faiss, FTP, Graph

BaseConfig = Template = ConfigTemplate
SystemConfig = System = BaseSystem

__all__ = [
    "BaseSystem",
    "BaseConfig",
    "Template",
    "System",
    "ConfigTemplate",
    "SystemConfig"
]
