from typing import Any, List, Optional, Self, cast

from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient

from pydantic_mongo_document.document.base import DocumentBase

import pymongo.results

_SYNC_CLIENTS: dict[str, MongoClient] = {}


class Document(DocumentBase):
    """Sync document model."""

    @classmethod
    def client(cls) -> "MongoClient[Self]":
        if cls.__replica__ not in _SYNC_CLIENTS:
            _SYNC_CLIENTS[cls.__replica__] = MongoClient(
                str(cls.get_replica_config().uri),
                **cls.get_replica_config().client_options,
            )

        return _SYNC_CLIENTS[cls.__replica__]

    @classmethod
    def database(cls) -> "Database[Self]":
        return cls.client()[cls.__database__]

    @classmethod
    def collection(cls) -> "Collection[Any]":
        return cls.database()[cls.__collection__]

    @classmethod
    def create_indexes(cls) -> None:
        """Creates indexes for collection."""

    @classmethod
    def one(
        cls,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        required: bool = True,
        **kwargs: Any,
    ) -> Self | None:
        return cast(
            Self | None,
            super().one(document_id=document_id, add_query=add_query, **kwargs),
        )

    @classmethod
    def count(cls, add_query: dict[str, Any] | None = None, **kwargs: Any) -> int:
        return cast(int, super().count(add_query=add_query, **kwargs))

    def insert(self) -> Self:
        return cast(Self, super().insert())

    def noop(self) -> None:
        return

    def commit_changes(
        self, fields: Optional[List[str]] = None
    ) -> Optional[pymongo.results.UpdateResult]:
        return cast(
            Optional[pymongo.results.UpdateResult],
            super().commit_changes(fields=fields),
        )

    def delete(
        self,
    ) -> pymongo.results.DeleteResult:
        return cast(
            pymongo.results.DeleteResult,
            super().delete(),
        )
