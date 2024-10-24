import typing
from typing import Awaitable, Optional, Any, TypeAlias

import pymongo.results  # type: ignore[import-untyped]

if typing.TYPE_CHECKING:
    from pydantic_mongo_document.document.base import DocumentBase  # noqa: F401

SyncInsertOneResult: TypeAlias = pymongo.results.InsertOneResult
AsyncInsertOneResult = Awaitable[SyncInsertOneResult]
InsertOneResult = SyncInsertOneResult | AsyncInsertOneResult
SyncFindOneResult = Optional["DocumentBase[Any, Any, Any, Any, Any, Any, Any, Any]"]
AsyncFindOneResult = Awaitable[SyncFindOneResult]
FindOneResult = SyncFindOneResult | AsyncFindOneResult
