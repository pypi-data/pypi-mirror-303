import requests.packages.urllib3

from abc import ABCMeta
from urllib3.exceptions import InsecureRequestWarning

from project_utils.conf import ElasticSearch


class BaseElasticSearch(metaclass=ABCMeta):
    es_model: ElasticSearch
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
