import copy
import time

from typing import Tuple, Optional

from project_utils.exception import ElasticSearchException


class ContextUtils:
    T = Tuple[str, dict, dict]
    T1 = Tuple[str, str, dict]
    T2 = Tuple[int, Optional[dict]]
    T3 = Tuple[str, str]

    def before_create(self, m: any) -> T:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        index: str = model.__meta__.name
        settings: dict = model.__default__.settings if model.__meta__.settings is None else model.__meta__.settings
        mappings: dict = model.__default__.mappings if model.__meta__.mappings is None else model.__meta__.mappings
        return index, settings, mappings

    def after_create(self, response: dict) -> Optional[str]:
        if "index" in response:
            return response["index"]
        else:
            return

    def before_drop(self, m: any) -> str:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        return model.__meta__.name

    def after_drop(self, response: dict) -> T2:
        if "error" in response:
            return -1, response
        else:
            return 1, None

    def before_show(self, m: any) -> str:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        return model.__meta__.name

    def after_show(self, response: dict) -> Optional[dict]:
        if "error" in response:
            return
        else:
            return response

    def before_insert(self, m: any) -> T1:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        model.create_time = int(time.time() * 1000)
        model.update_time = int(time.time() * 1000)
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        primary_key: str = model.__default__.primary_key if model.__meta__.primary_key is None else model.__meta__.primary_key
        return name, primary_key, model.to_dict()

    def after_insert(self, response: dict, m: any) -> Optional[any]:
        if "error" in response:
            return
        else:
            return m

    def before_delete(self, m: any) -> T3:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        primary_key: str = model.__default__.primary_key if model.__meta__.primary_key is None else model.__meta__.primary_key
        return name, primary_key

    def after_delete(self, response: dict, m: any) -> Optional[str]:
        if "error" in response:
            return
        else:
            primary_key: str = m.__default__.primary_key if m.__meta__.primary_key is None else m.__meta__.primary_key
            return getattr(m, primary_key)

    def before_get(self, m: any) -> T3:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        primary_key: str = model.__default__.primary_key if model.__meta__.primary_key is None else model.__meta__.primary_key
        return name, primary_key

    def after_get(self, response: dict, m: any) -> Optional[any]:
        found: bool = response['found']
        if not found:
            return
        instance: any = m.__class__(**response['_source'])
        return instance

    def before_update(self, m: any) -> T1:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        primary_key: str = model.__default__.primary_key if model.__meta__.primary_key is None else model.__meta__.primary_key
        doc_id: str = model.__getattribute__(primary_key)
        source_data: dict = model.__source__
        current_data: dict = model.to_dict()
        update_data: dict = {"update_time": int(time.time() * 1000)}
        for key, val in source_data.items():
            if val != current_data[key]:
                update_data[key] = current_data[key]
        return name, doc_id, update_data

    def after_update(self, response: dict, m: any):
        if "error" in response:
            return
        else:
            return m

    def before_batch_insert(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_batch_insert(self, response: dict):
        if "items" in response:
            return len(response["items"])
        else:
            return -1

    def before_batch_update(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_batch_update(self, response: dict):
        if "items" in response:
            return len(response["items"])
        else:
            return -1

    def before_batch_delete(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_batch_delete(self, response: dict):
        if "deleted" in response:
            return response['deleted']
        else:
            return -1

    def before_select_all(self, m: any) -> str:
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_select_all(self, response: dict, m: any, context: any):
        if "hits" in response:
            from project_utils.models.elasticsearch import ElasticSearchBaseModel, ElasticSearchBaseBatch
            model: ElasticSearchBaseModel = m
            batch: ElasticSearchBaseBatch[ElasticSearchBaseModel] = ElasticSearchBaseBatch()
            model_class: any = model.__class__
            hits: list = response['hits']['hits']
            for hit in hits:
                item: ElasticSearchBaseModel = model_class(**hit['_source'])
                context_copy = copy.deepcopy(context)
                item.__objects__ = context_copy
                context_copy.model = item
                primary_key: str = item.__default__.primary_key if item.__meta__.primary_key is None else item.__meta__.primary_key
                item.__setattr__(primary_key, hit['_id'])
                batch.add(item)
            return batch
        else:
            return

    def before_select_filter(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_select_filter(self, response: dict, m: any, context: any):
        if "hits" in response:
            from project_utils.models.elasticsearch import ElasticSearchBaseModel, ElasticSearchBaseBatch
            model: ElasticSearchBaseModel = m
            batch: ElasticSearchBaseBatch[ElasticSearchBaseModel] = ElasticSearchBaseBatch()
            model_class: any = model.__class__
            hits: list = response['hits']['hits']
            for hit in hits:
                item: ElasticSearchBaseModel = model_class(**hit['_source'])
                context_copy = copy.deepcopy(context)
                item.__objects__ = context_copy
                context_copy.model = item
                primary_key: str = item.__default__.primary_key if item.__meta__.primary_key is None else item.__meta__.primary_key
                item.__setattr__(primary_key, hit['_id'])
                batch.add(item)
            return batch
        else:
            return

    def before_select_filter_by(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_select_filter_by(self, response: dict, m: any, context: any):
        if "hits" in response:
            from project_utils.models.elasticsearch import ElasticSearchBaseModel, ElasticSearchBaseBatch
            model: ElasticSearchBaseModel = m
            batch: ElasticSearchBaseBatch[ElasticSearchBaseModel] = ElasticSearchBaseBatch()
            model_class: any = model.__class__
            hits: list = response['hits']['hits']
            for hit in hits:
                item: ElasticSearchBaseModel = model_class(**hit['_source'])
                context_copy = copy.deepcopy(context)
                item.__objects__ = context_copy
                context_copy.model = item
                primary_key: str = item.__default__.primary_key if item.__meta__.primary_key is None else item.__meta__.primary_key
                item.__setattr__(primary_key, hit['_id'])
                batch.add(item)
            return batch
        else:
            return

    def before_select_scroll(self, m: any):
        from project_utils.models.elasticsearch import ElasticSearchBaseModel
        model: ElasticSearchBaseModel = m
        assert model.__meta__.name, ElasticSearchException("The name of index value cannot is null!", __file__, 10)
        name: str = model.__meta__.name
        return name

    def after_select_scroll(self, scroll: int, index: str, m: any, context: any, response: dict):
        if "hits" in response:
            from project_utils.models.elasticsearch import ElasticSearchIter
            scroll_id: str = response['_scroll_id']
            hits: list = response['hits']['hits']
            data: list = []
            for hit in hits:
                primary_key: str = m.__default__.primary_key if m.__meta__.primary_key is None else m.__meta__.primary_key
                item: dict = hit['_source']
                item[primary_key] = hit['_id']
                data.append(item)
            print(111111)
            return ElasticSearchIter(m, index, data, scroll, context, scroll_id)
        else:
            return
