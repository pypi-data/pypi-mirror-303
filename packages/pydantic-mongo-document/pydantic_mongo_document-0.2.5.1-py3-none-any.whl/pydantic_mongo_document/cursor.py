import typing
from typing import (
    Any,
    AsyncGenerator,
    Generator,
    Generic,
    ParamSpec,
    Self,
    TypeVar,
    Callable,
)

import motor.motor_asyncio  # type: ignore[import-untyped]
import pymongo.cursor  # type: ignore[import-untyped]

if typing.TYPE_CHECKING:
    import pydantic_mongo_document.document.sync  # noqa: F401
    import pydantic_mongo_document.document.asyncio  # noqa: F401
    from pydantic_mongo_document.document.base import DocumentBase  # noqa: F401

P = ParamSpec("P")
D = TypeVar("D", bound="DocumentBase[Any, Any, Any, Any, Any, Any, Any]")

AG = AsyncGenerator["pydantic_mongo_document.document.asyncio.Document", None]
G = Generator["pydantic_mongo_document.document.sync.Document", None, None]

C = TypeVar("C", bound="Cursor[Any]")
R = TypeVar("R")


def check_is_sync(f: Callable[[C], R]) -> Callable[[C], R]:
    def wrapper(self: C) -> R:
        from pydantic_mongo_document.document.sync import Document as SyncDocument

        if not isinstance(self.model_cls, SyncDocument) or (
            self.generator is not None and isinstance(self.generator, AsyncGenerator)
        ):
            raise TypeError("Cursor is not sync.")

        return f(self)

    return wrapper


def check_is_async(f: Callable[[C], R]) -> Callable[[C], R]:
    def wrapper(self: C) -> R:
        from pydantic_mongo_document.document.asyncio import Document as AsyncDocument

        if not issubclass(self.model_cls, AsyncDocument) or (
            self.generator is not None and isinstance(self.generator, Generator)
        ):
            raise TypeError("Cursor is not async.")

        return f(self)

    return wrapper


class Cursor(Generic[D]):
    generator: G | AG | None

    def __init__(
        self,
        model_cls: D,
        cursor: pymongo.cursor.Cursor | motor.motor_asyncio.AsyncIOMotorCursor,
    ) -> None:
        self.model_cls = model_cls
        self.cursor = cursor
        self.generator = None

    @check_is_async
    def __aiter__(self) -> Self:
        self.generator = self.cursor.__aiter__()
        return self

    @check_is_sync
    def __iter__(self) -> Self:
        self.generator = self.cursor.__iter__()
        return self

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> "Cursor[D]":
        return Cursor[self.model_cls](self.model_cls, self.cursor(*args, **kwargs))  # type: ignore[name-defined]

    def __getattr__(self, item: str) -> Self | Any:
        value = getattr(self.cursor, item)

        if callable(value):
            return Cursor[self.model_cls](self.model_cls, value)  # type: ignore[name-defined]

        return value

    @check_is_async
    async def __anext__(self) -> D:
        assert isinstance(self.generator, AsyncGenerator)
        return self.model_cls.model_validate(await self.generator.__anext__())

    @check_is_sync
    def __next__(self) -> D:
        assert isinstance(self.generator, Generator)
        return self.model_cls.model_validate(next(self.generator))
