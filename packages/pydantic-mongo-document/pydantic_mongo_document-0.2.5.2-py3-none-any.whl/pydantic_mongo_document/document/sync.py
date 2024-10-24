from typing import Any, Optional, Self, cast

import pymongo.results  # type: ignore[import-untyped]
from pymongo.collection import Collection  # type: ignore[import-untyped]
from pymongo.database import Database  # type: ignore[import-untyped]
from pymongo.mongo_client import MongoClient  # type: ignore[import-untyped]

from pydantic_mongo_document.document.base import DocumentBase


_SYNC_CLIENTS: dict[str, MongoClient] = {}


class Document(
    DocumentBase[
        MongoClient,
        Database,
        Collection,
        int,
        pymongo.results.DeleteResult,
        Optional[pymongo.results.UpdateResult],
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
            cls._inner_one(document_id, add_query, **kwargs),
        )

        if result is not None:
            return cls.model_validate(result)
        if required:
            raise cls.NotFoundError()

        return None

    def insert(self) -> Self:
        """Insert document into collection."""

        result = self.collection().insert_one(
            self.encoder.encode_dict(
                self.model_dump(by_alias=True, exclude_none=True),
                reveal_secrets=True,
            )
        )

        if getattr(self, self.__primary_key__, None) is None:
            setattr(self, self.__primary_key__, result.inserted_id)

        return self
