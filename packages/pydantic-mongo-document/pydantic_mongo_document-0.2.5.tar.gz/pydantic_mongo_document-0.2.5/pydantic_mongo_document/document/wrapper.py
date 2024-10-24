import asyncio
import functools
import typing
from typing import (
    Any,
    Awaitable,
    Callable,
    ParamSpec,
    TypeVar,
    overload,
)

from pydantic_mongo_document.document.types import (
    AsyncInsertOneResult,
    InsertOneResult,
    SyncInsertOneResult,
)

if typing.TYPE_CHECKING:
    from pydantic_mongo_document.document.base import DocumentBase  # noqa: F401


T = TypeVar("T")
P = ParamSpec("P")
D = TypeVar("D", bound="DocumentBase[Any, Any, Any, Any, Any, Any, Any, Any]")


@overload
def wrap_insert(
    f: Callable[[D], SyncInsertOneResult],
) -> Callable[[D], D]: ...


@overload
def wrap_insert(
    f: Callable[[D], AsyncInsertOneResult],
) -> Callable[[D], Awaitable[D]]: ...


def wrap_insert(
    f: Callable[[D], InsertOneResult],
) -> Callable[[D], D | Awaitable[D]]:
    """Wraps insert method to return model instance."""

    async def async_wrapper(self: D, coro: AsyncInsertOneResult) -> D:
        """Async wrapper for insert method."""

        result = await coro

        if getattr(self, self.__primary_key__, None) is None:
            setattr(self, self.__primary_key__, result.inserted_id)

        return self

    def sync_wrapper(self: D, result: SyncInsertOneResult) -> D:
        """Sync wrapper for insert method."""

        if getattr(self, self.__primary_key__, None) is None:
            setattr(self, self.__primary_key__, result.inserted_id)

        return self

    @functools.wraps(f)
    def wrapper(self: D) -> D | Awaitable[D]:
        """Wrapper for insert method."""

        result = f(self)

        return (
            async_wrapper(self, result)
            if asyncio.iscoroutine(result)
            else sync_wrapper(self, result)
        )

    return wrapper
