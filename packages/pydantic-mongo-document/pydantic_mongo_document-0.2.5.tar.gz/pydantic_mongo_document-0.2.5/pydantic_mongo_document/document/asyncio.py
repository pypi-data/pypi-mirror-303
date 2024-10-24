import asyncio
from typing import Any, Awaitable, Optional, Self, cast

import pymongo.results  # type: ignore[import-untyped]
from motor.motor_asyncio import (  # type: ignore[import-untyped]
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from pydantic_mongo_document.document.base import DocumentBase
from pydantic_mongo_document.document.types import AsyncInsertOneResult

_ASYNC_CLIENTS: dict[str, AsyncIOMotorClient] = {}


class Document(
    DocumentBase[
        AsyncIOMotorClient,
        AsyncIOMotorDatabase,
        AsyncIOMotorCollection,
        Awaitable[None],
        Awaitable[int],
        Awaitable[pymongo.results.DeleteResult],
        Awaitable[pymongo.results.UpdateResult | None],
        Awaitable[AsyncInsertOneResult],
    ],
):
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
    async def create_indexes(cls) -> None:
        """Creates indexes for collection."""

    async def noop(self) -> None:
        """No operation. Does nothing."""

    @classmethod
    async def one(
        cls,
        /,
        document_id: str | None = None,
        add_query: dict[str, Any] | None = None,
        required: bool = True,
        **kwargs: Any,
    ) -> Optional[Self]:
        result = await cast(
            Awaitable[Optional[dict[str, Any]]],
            cls._inner_one(document_id, add_query, required, **kwargs),
        )

        if result is not None:
            return cls.model_validate(result)
        if required:
            raise cls.NotFoundError()

        return None
