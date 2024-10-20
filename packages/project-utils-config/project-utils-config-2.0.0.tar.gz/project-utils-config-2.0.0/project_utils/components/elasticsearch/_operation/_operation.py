import json

import requests
import traceback

from typing import Optional, Tuple
from requests import Session, Response
from requests.auth import HTTPBasicAuth

from project_utils.exception import ElasticSearchException

from ._base import BaseElasticSearchOperation


class ElasticSearchOperation(BaseElasticSearchOperation):
    T1 = Optional[HTTPBasicAuth]

    def create(self, index: str, settings: Optional[dict] = None, mappings: Optional[dict] = None, auth: T1 = None):
        request_url, request_headers, request_body = self.utils.create(self.es_model, index, settings, mappings)
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.put(request_url, json=request_body, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def drop(self, index: str, auth: T1 = None):
        request_url, request_headers = self.utils.drop(self.es_model, index)
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.delete(request_url, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def indexes(self, auth: T1 = None):
        request_url: str = self.utils.indexes(self.es_model)
        session: Session = requests.session()
        try:
            response: Response = session.get(request_url, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.text

    def show(self, index: str, auth: T1):
        request_url: str = self.utils.show(self.es_model, index)
        session: Session = requests.session()
        try:
            response: Response = session.get(request_url, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def insert(self, index: str, doc_id: str, auth: T1, **kwargs):
        request_url, request_headers = self.utils.insert(self.es_model, index, doc_id)
        request_body: dict = kwargs.copy()
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.post(request_url, json=request_body, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def delete(self, index: str, doc_id: str, auth: T1):
        request_url = self.utils.delete(self.es_model, index, doc_id)
        session: Session = requests.session()
        try:
            response: Response = session.delete(request_url, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def get(self, index: str, doc_id: str, auth: T1):
        request_url = self.utils.get(self.es_model, index, doc_id)
        session: Session = requests.session()
        try:
            response: Response = session.get(request_url, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def update(self, index: str, doc_id: str, auth: T1, **data):
        request_url, request_headers, request_body = self.utils.update(self.es_model, index, doc_id, **data)
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.post(request_url, json=request_body, verify=False, auth=auth)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def batch_insert(self, index: str, auth: T1, params: str):
        request_url, request_headers = self.utils.batch_insert(self.es_model, index)
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.post(request_url, data=params.encode(), verify=False, auth=auth, )
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def batch_update(self, index: str, auth: T1, params: str):
        request_url, request_headers = self.utils.batch_update(self.es_model, index)
        session: Session = requests.session()
        session.headers = request_headers
        try:
            response: Response = session.post(request_url, data=params.encode(), verify=False, auth=auth, )
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def batch_delete(self, index: str, auth: T1, mode: str = "match", **query):
        request_url, request_headers, request_body = self.utils.batch_delete(self.es_model, index, mode, **query)
        try:
            session: Session = requests.session()
            session.headers = request_headers
            session.auth = auth
            session.verify = False
            response: Response = session.post(request_url, json=request_body)
            return response.json()
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())

    def all(self, index: str, auth: T1, _from: int = 0, _size: int = 10):
        request_url, request_headers, request_body = self.utils.select_all(self.es_model, index, _from, _size)
        session: Session = requests.session()
        session.headers = request_headers
        session.auth = auth
        try:
            response: Response = session.post(request_url, json=request_body, verify=False)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def filter(self, index: str, auth: T1, query: dict, mode: str = "match", _from: int = 0, _size: int = 0):
        request_url, request_headers, request_body = self.utils.filter(self.es_model, index, mode, _from, _size, query)
        try:
            session: Session = requests.session()
            session.headers = request_headers
            session.auth = auth
            response: Response = session.post(request_url, json=request_body, verify=False)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def filter_by(self, index: str, auth: T1, query: dict):
        request_url, request_headers, request_body = self.utils.filter_by(self.es_model, index, query)
        try:
            session: Session = requests.session()
            session.headers = request_headers
            session.auth = auth
            response: Response = session.post(request_url, json=request_body, verify=False)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()

    def scroll(self, index: str, auth: T1, scroll: int, scroll_id: Optional[str] = None, mode: str = "match_all",
               _from: int = 0, _size: int = 1000, **query):
        if scroll_id is None:
            request_url, request_headers, request_body = self.utils.first_scroll(self.es_model, index, scroll, mode,
                                                                                 _from, _size, **query)
        else:
            request_url, request_headers, request_body = self.utils.scroll(self.es_model, scroll, scroll_id)
        session: Session = requests.session()
        session.headers = request_headers
        session.auth = auth
        try:
            response: Response = session.post(request_url, json=request_body, verify=False)
        except Exception as e:
            raise ElasticSearchException(str(e), __file__, e.__traceback__.tb_lineno, traceback.format_exc())
        return response.json()
