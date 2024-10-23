import asyncio
from typing import Any, Awaitable, Self, cast

import pymongo.results

from pydantic_mongo_document.document.base import DocumentBase


from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)


_ASYNC_CLIENTS: dict[str, AsyncIOMotorClient] = {}


class Document(DocumentBase):
    """Async document model."""

    @classmethod
    def client(cls) -> AsyncIOMotorClient:
        if cls.__replica__ not in _ASYNC_CLIENTS:
            _ASYNC_CLIENTS[cls.__replica__] = AsyncIOMotorClient(
                host=str(cls.get_replica_config().uri),
                **cls.get_replica_config().client_options,
            )

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()

        # Set the current event loop to the client's I/O loop
        _ASYNC_CLIENTS[cls.__replica__]._io_loop = loop  # noqa

        return _ASYNC_CLIENTS[cls.__replica__]

    @classmethod
    def database(cls) -> AsyncIOMotorDatabase:
        return cls.client()[cls.__database__]

    @classmethod
    def collection(cls) -> AsyncIOMotorCollection:
        return cls.database()[cls.__collection__]

    @classmethod
    async def create_indexes(cls) -> None:
        """Creates indexes for collection."""

    @classmethod
    def one(
        cls,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        required: bool = True,
        **kwargs: Any,
    ) -> Awaitable[Self | None]:
        return cast(
            Awaitable[Self | None],
            super().one(document_id=document_id, add_query=add_query, **kwargs),
        )

    @classmethod
    def count(
        cls, add_query: dict[str, Any] | None = None, **kwargs: Any
    ) -> Awaitable[int]:
        return cast(Awaitable[int], super().count(add_query=add_query, **kwargs))

    def delete(
        self,
    ) -> Awaitable[pymongo.results.DeleteResult]:
        return cast(
            Awaitable[pymongo.results.DeleteResult],
            super().delete(),
        )

    def commit_changes(
        self, fields: list[str] | None = None
    ) -> Awaitable[pymongo.results.UpdateResult | None]:
        return cast(
            Awaitable[pymongo.results.UpdateResult | None],
            super().commit_changes(fields=fields),
        )

    def insert(self) -> Awaitable[Self]:
        return cast(Awaitable[Self], super().insert())

    async def noop(self) -> None:
        """No operation. Does nothing."""
