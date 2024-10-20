from project_utils.models.elasticsearch import ElasticSearchBaseModel, ElasticSearchBaseMeta


class TestESModel(ElasticSearchBaseModel):
    name: str = None
    age: int = None
    gender: bool = None

    class Meta(ElasticSearchBaseMeta):
        name = "test_es1"
        mappings = {
            "name": {"type": "keyword", "index": True},
            "age": {"type": "long", "index": True},
            "gender": {"type": "byte", "index": True},
            "create_user": {"type": "keyword", "index": True},
            "update_user": {"type": "keyword", "index": True},
            "create_time": {"type": "long", "index": True},
            "update_time": {"type": "long", "index": True},
            "is_delete": {"type": "byte", "index": True},
            "remake": {"type": "text", "index": True},
        }


class AsyncTestESModel(ElasticSearchBaseModel):
    name: str = None
    age: int = None
    gender: bool = None

    class Meta(ElasticSearchBaseMeta):
        name = "test_es2"
        mappings = {
            "name": {"type": "keyword", "index": True},
            "age": {"type": "long", "index": True},
            "gender": {"type": "byte", "index": True},
            "create_user": {"type": "keyword", "index": True},
            "update_user": {"type": "keyword", "index": True},
            "create_time": {"type": "long", "index": True},
            "update_time": {"type": "long", "index": True},
            "is_delete": {"type": "byte", "index": True},
            "remake": {"type": "text", "index": True},
        }
