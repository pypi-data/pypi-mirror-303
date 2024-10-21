from reqdb.api import API
from reqdb.schemas import BaseSchema, TagSchema, TopicSchema, \
    RequirementSchema, ExtraTypeSchema, ExtraEntrySchema, CatalogueSchema, CommentSchema
from reqdb.models import Base, Tag, Topic, \
    Requirement, ExtraType, ExtraEntry, Catalogue, Comment


class ReqDB:

    api = None

    def __init__(self, fqdn, bearer, insecure: bool = False) -> None:
        ReqDB.api = API(fqdn, bearer, insecure)

    class Entity:
        endpoint: str = None
        schema: BaseSchema = None
        model: Base = None

        @classmethod
        def get(cls, id: int) -> dict|bool:
            return ReqDB.api.get(f"{cls.endpoint}/{id}")

        @classmethod
        def all(cls) -> dict|bool:
            return ReqDB.api.get(f"{cls.endpoint}")

        @classmethod
        def update(cls, id: int, data: Base) -> dict|bool:
            if not isinstance(data, cls.model):
                raise TypeError(f"Data not the correct model ({cls.model.__name__})")
            return ReqDB.api.update(f"{cls.endpoint}/{id}", cls.schema.dump(data))

        @classmethod
        def delete(cls, id: int) -> dict|bool:
            return ReqDB.api.delete(f"{cls.endpoint}/{id}")

        @classmethod
        def add(cls, data: Base) -> dict|bool:
            if not isinstance(data, cls.model):
                raise TypeError(f"Data not the correct model ({cls.model.__name__})")
            r = ReqDB.api.add(f"{cls.endpoint}", cls.schema.dump(data))
            return r

    class Tags(Entity):
        endpoint = "tags"
        schema = TagSchema()
        model = Tag

    class Topics(Entity):
        endpoint = "topics"
        schema = TopicSchema()
        model = Topic

    class Requirements(Entity):
        endpoint = "requirements"
        schema = RequirementSchema()
        model = Requirement

    class ExtraTypes(Entity):
        endpoint = "extraTypes"
        schema = ExtraTypeSchema()
        model = ExtraType

    class ExtraEntries(Entity):
        endpoint = "extraEntries"
        schema = ExtraEntrySchema()
        model = ExtraEntry

    class Catalogues(Entity):
        endpoint = "catalogues"
        schema = CatalogueSchema()
        model = Catalogue

    class Comment(Entity):
        endpoint = "comments"
        schema = CommentSchema()
        model = Comment

    class Coffee(Entity):
        endpoint = "coffee"
        schema = None
        model = None

    class Audit(Entity):
        endpoint = "audit"
        schema = None
        model = None

        @classmethod
        def _targetCheck(cls, obj: str):
            target = ["extraEntries", "extraTypes", "requirements", "tags", "topics", "catalogues", "comments"]
            if obj not in ["extraEntries", "extraTypes", "requirements", "tags", "topics", "catalogues", "comments"]:
                raise KeyError(f"Audit object can only one of: {', '.join(target)}")

        @classmethod
        def get(cls, obj: str, id: int) -> dict|bool:
            cls._targetCheck(obj)
            return ReqDB.api.get(f"{cls.endpoint}/{obj}/{id}")

        @classmethod
        def all(cls, obj: str) -> dict|bool:
            cls._targetCheck(obj)
            return ReqDB.api.get(f"{cls.endpoint}/{obj}")

        @classmethod
        def update(cls, id, data: Base):
            raise NotImplementedError

        @classmethod
        def delete(cls, id):
            raise NotImplementedError

        @classmethod
        def add(cls, data: Base):
            raise NotImplementedError