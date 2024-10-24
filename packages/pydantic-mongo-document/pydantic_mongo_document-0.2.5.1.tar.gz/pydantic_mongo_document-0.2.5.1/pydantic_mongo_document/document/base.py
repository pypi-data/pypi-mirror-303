from abc import ABC, abstractmethod
from typing import (
    Any,
    Awaitable,
    ClassVar,
    Generic,
    List,
    Optional,
    Self,
    Type,
    TypeVar,
    Union,
    cast,
)

import bson  # type: ignore[import-untyped]
import pymongo.errors  # type: ignore[import-untyped]
import pymongo.results  # type: ignore[import-untyped]
from motor.motor_asyncio import (  # type: ignore[import-untyped]
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)
from pydantic import BaseModel, Field, validate_call
from pymongo import MongoClient
from pymongo.collection import Collection  # type: ignore[import-untyped]
from pymongo.database import Database  # type: ignore[import-untyped]

from pydantic_mongo_document import ObjectId
from pydantic_mongo_document.config import ReplicaConfig
from pydantic_mongo_document.cursor import Cursor
from pydantic_mongo_document.encoder import JsonEncoder
from pydantic_mongo_document.exceptions import DocumentNotFound

CONFIG: dict[str, ReplicaConfig] = {}
"""Map of replicas to mongo URIs."""

# Type variables
D = TypeVar("D", bound="DocumentBase[Any, Any, Any, Any, Any, Any, Any]")

CLT = TypeVar("CLT", bound=Union[MongoClient, AsyncIOMotorClient])
DBT = TypeVar("DBT", bound=Union[Database, AsyncIOMotorDatabase])
COT = TypeVar("COT", bound=Union[Collection, AsyncIOMotorCollection])

CT = TypeVar("CT", bound=Union[int, Awaitable[int]])
DT = TypeVar(
    "DT", bound=pymongo.results.DeleteResult | Awaitable[pymongo.results.DeleteResult]
)
CCT = TypeVar(
    "CCT",
    bound=Optional[pymongo.results.UpdateResult]
    | Awaitable[Optional[pymongo.results.UpdateResult]],
)


class DocumentBase(BaseModel, ABC, Generic[CLT, DBT, COT, CT, DT, CCT]):
    __primary_key__: ClassVar[str] = "id"

    __replica__: ClassVar[str]
    """Mongodb replica name."""

    __database__: ClassVar[str]
    """Mongodb database name."""

    __collection__: ClassVar[str]
    """Mongodb collection name."""

    __clients__: ClassVar[dict[str, Any]] = {}
    """Map of clients for each database."""

    __document__: dict[str, Any]
    """Document data. For internal use only."""

    NotFoundError: ClassVar[Type[Exception]] = DocumentNotFound
    DuplicateKeyError: ClassVar[Type[Exception]] = pymongo.errors.DuplicateKeyError

    encoder: ClassVar[JsonEncoder] = JsonEncoder()

    id: ObjectId = Field(default_factory=lambda: str(bson.ObjectId()), alias="_id")

    def model_post_init(self, __context: Any) -> None:
        self.__document__ = self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    @abstractmethod
    def client(cls) -> CLT:
        """Returns client for database."""

    @classmethod
    def database(cls) -> DBT:
        return cast(DBT, cls.client()[cls.__database__])

    @classmethod
    def collection(cls) -> COT:
        return cast(COT, cls.database()[cls.__collection__])

    @property
    def primary_key(self) -> Any:
        return getattr(self, self.__primary_key__)

    @classmethod
    def get_replica_config(cls) -> ReplicaConfig:
        return CONFIG[cls.__replica__]

    @property
    def primary_key_field_name(self) -> str:
        return self.model_fields[self.__primary_key__].alias or self.__primary_key__

    @classmethod
    @validate_call
    def set_replica_config(cls, config: dict[str, ReplicaConfig]) -> None:
        CONFIG.clear()
        CONFIG.update(config)

    @classmethod
    @abstractmethod
    def create_indexes(cls) -> Awaitable[None] | None:
        """Creates indexes for collection."""

    @classmethod
    def _inner_one(
        cls,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Optional[dict[str, Any]] | Awaitable[dict[str, Any]]:
        """Finds one document by ID."""

        query = {}
        if document_id is not None:
            query["_id"] = document_id
        if add_query is not None:
            query.update(add_query)

        query = cls.encoder.encode_dict(query, reveal_secrets=True)

        return cast(
            Optional[dict[str, Any]] | Awaitable[dict[str, Any]],
            cls.collection().find_one(query, **kwargs),
        )

    @classmethod
    @abstractmethod
    def one(
        cls,
        /,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        required: bool = True,
        **kwargs: Any,
    ) -> Optional[Self | Awaitable[Optional[Self]]]:
        """Finds one document by ID."""

        raise NotImplementedError()

    @classmethod
    def all(
        cls,
        document_ids: List[str | bson.ObjectId] | None = None,
        add_query: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Cursor[Self]:  # noqa
        """Finds all documents based in IDs."""

        query = {}
        if document_ids is not None:
            query["_id"] = {"$in": document_ids}
        if add_query is not None:
            query.update(add_query)

        query = cls.encoder.encode_dict(query, reveal_secrets=True)

        cursor_cls = Cursor[cls]  # type: ignore[valid-type]

        return cursor_cls(cls, cls.collection().find(query, **kwargs))

    @classmethod
    def count(cls, add_query: dict[str, Any] | None = None, **kwargs: Any) -> CT:
        """Counts documents in collection."""

        query = {}
        if add_query is not None:
            query.update(add_query)

        query = cls.encoder.encode_dict(query, reveal_secrets=True)

        return cast(
            CT,
            cls.collection().count_documents(query, **kwargs),
        )

    def delete(
        self,
    ) -> DT:
        """Deletes document from collection."""

        query = self.encoder.encode_dict(
            {self.primary_key_field_name: self.primary_key},
        )

        return cast(DT, self.collection().delete_one(query))

    def commit_changes(self, fields: Optional[List[str]] = None) -> CCT:
        """Saves changes to document."""

        search_query: dict[str, Any] = {self.primary_key_field_name: self.primary_key}
        update_query: dict[str, Any] = {}

        if not fields:
            fields = [
                field
                for field in self.model_fields.keys()
                if field != self.__primary_key__
            ]

        data = self.encoder.encode_dict(
            self.model_dump(by_alias=True, exclude_none=True),
            reveal_secrets=True,
        )

        for field in fields:
            if field in data and data[field] != self.__document__.get(field):
                update_query.setdefault("$set", {}).update({field: data[field]})
            elif field not in data and field in self.__document__:
                update_query.setdefault("$unset", {}).update({field: ""})

        if update_query:
            return cast(
                CCT, self.collection().update_one(search_query or None, update_query)
            )

        return cast(CCT, self.noop())

    @abstractmethod
    def insert(self) -> Self | Awaitable[Self]:
        """Inserts document into collection."""

        raise NotImplementedError()

    def noop(self) -> Awaitable[None] | None:
        """No operation. Does nothing."""
