import typing
from typing import Awaitable, TypeVar, Optional
import pymongo.results

if typing.TYPE_CHECKING:
    from pydantic_mongo_document.document.base import DocumentBase  # noqa: F401


D = TypeVar("D", bound="DocumentBase")

SyncInsertOneResult = pymongo.results.InsertOneResult
AsyncInsertOneResult = Awaitable[SyncInsertOneResult]  # type: ignore[valid-type]
InsertOneResult = SyncInsertOneResult | AsyncInsertOneResult
SyncFindOneResult = Optional["DocumentBase"]
AsyncFindOneResult = Awaitable[SyncFindOneResult]
FindOneResult = SyncFindOneResult | AsyncFindOneResult
