import asyncio
import functools
import typing
from typing import Any, Awaitable, Callable, Concatenate, ParamSpec, TypeVar, Self

from pydantic_mongo_document.document.types import (
    AsyncInsertOneResult,
    FindOneResult,
    InsertOneResult,
    SyncInsertOneResult,
)

if typing.TYPE_CHECKING:
    from pydantic_mongo_document.document.base import DocumentBase  # noqa: F401


P = ParamSpec("P")
D = TypeVar("D", bound="DocumentBase")


def wrap_one(
    f: Callable[
        Concatenate[type[D], P],
        dict[str, Any] | None | Awaitable[dict[str, Any] | None],
    ],
) -> Callable[Concatenate[type[D], P], FindOneResult]:
    """Wraps one method to return model instance."""

    async def async_wrapper(
        cls: type[D], coro: Awaitable[dict[str, Any] | None], required: bool
    ) -> D | None:
        """Async wrapper for one method."""

        result = await coro
        if result is not None:
            return cls.model_validate(result)
        if required:
            raise cls.NotFoundError()

        return None

    def sync_wrapper(
        cls: type[D], result: dict[str, Any] | None, required: bool
    ) -> D | None:
        """Sync wrapper for one method."""

        if result is not None:
            return cls.model_validate(result)
        if required:
            raise cls.NotFoundError()

        return None

    @functools.wraps(f)
    def wrapper(
        cls: type[D], /, *args: P.args, **kwargs: P.kwargs
    ) -> D | None | Awaitable[D | None]:
        """Wrapper for one method."""

        result = f(cls, *args, **kwargs)
        required: bool = bool(kwargs.get("required", True))

        return (
            async_wrapper(cls, result, required)
            if isinstance(result, Awaitable)
            else sync_wrapper(cls, result, required)
        )

    return wrapper


def wrap_insert(
    f: Callable[P, InsertOneResult],
) -> Callable[P, D | Awaitable[D]]:
    """Wraps insert method to return model instance."""

    async def async_wrapper(self: D, result: AsyncInsertOneResult) -> D:
        """Async wrapper for insert method."""

        result = await result

        if getattr(self, self.__primary_key__, None) is None:
            setattr(self, self.__primary_key__, result.inserted_id)

        return self

    def sync_wrapper(self: D, result: SyncInsertOneResult) -> D:  # type: ignore[valid-type]
        """Sync wrapper for insert method."""

        if getattr(self, self.__primary_key__, None) is None:
            setattr(self, self.__primary_key__, result.inserted_id)  # type: ignore[attr-defined]

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
