from typing import Any, Optional, Self, TypeVar, cast

import pymongo.results  # type: ignore[import-untyped]
from pymongo.collection import Collection  # type: ignore[import-untyped]
from pymongo.database import Database  # type: ignore[import-untyped]
from pymongo.mongo_client import MongoClient  # type: ignore[import-untyped]

from pydantic_mongo_document.document.base import DocumentBase
from pydantic_mongo_document.document.types import SyncInsertOneResult


_SYNC_CLIENTS: dict[str, MongoClient] = {}


class Document(
    DocumentBase[
        MongoClient,
        Database,
        Collection,
        None,
        int,
        pymongo.results.DeleteResult,
        Optional[pymongo.results.UpdateResult],
        SyncInsertOneResult,
    ],
):
    """Sync document model."""

    @classmethod
    def client(cls) -> MongoClient:
        if cls.__replica__ not in _SYNC_CLIENTS:
            _SYNC_CLIENTS[cls.__replica__] = MongoClient(
                str(cls.get_replica_config().uri),
                **cls.get_replica_config().client_options,
            )

        return _SYNC_CLIENTS[cls.__replica__]

    @classmethod
    def create_indexes(cls) -> None:
        """Creates indexes for collection."""

    @classmethod
    def one(
        cls,
        /,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        required: bool = True,
        **kwargs: Any,
    ) -> Self | None:
        result = cast(
            Optional[dict[str, Any]],
            cls._inner_one(document_id, add_query, required, **kwargs),
        )

        if result is not None:
            return cls.model_validate(result)
        if required:
            raise cls.NotFoundError()

        return None
