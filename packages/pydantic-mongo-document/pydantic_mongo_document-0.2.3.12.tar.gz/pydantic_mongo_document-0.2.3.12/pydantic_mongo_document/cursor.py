import typing
from typing import (
    Any,
    Generic,
    ParamSpec,
    Self,
    TypeVar,
    Generator,
    AsyncGenerator,
    cast,
)

import motor.motor_asyncio
import pymongo.cursor

if typing.TYPE_CHECKING:
    from pydantic_mongo_document.document.base import DocumentBase


DT = TypeVar("DT", bound=type["DocumentBase"])
P = ParamSpec("P")

AG = AsyncGenerator["DocumentBase", None]
G = Generator["DocumentBase", None, None]


class Cursor(Generic[DT]):
    model_cls: DT

    def __init__(
        self, cursor: pymongo.cursor.Cursor | motor.motor_asyncio.AsyncIOMotorCursor
    ) -> None:
        self.cursor = cursor
        self.generator: G | AG | None = None

    def __class_getitem__(cls, item: DT) -> Self:
        result = super().__class_getitem__(item)  # type: ignore[misc]
        result.model_cls = item
        return cast(Self, result)

    def __aiter__(self) -> Self:
        self.generator = self.cursor.__aiter__()
        return self

    def __iter__(self) -> Self:
        self.generator = self.cursor.__iter__()
        return self

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> "Cursor[DT]":
        return Cursor[self.model_cls](self.cursor(*args, **kwargs))  # type: ignore[name-defined]

    def __getattr__(self, item: str) -> Self | Any:
        value = getattr(self.cursor, item)

        if callable(value):
            return Cursor[self.model_cls](value)  # type: ignore[name-defined]

        return value

    async def __anext__(self) -> "DocumentBase":
        if not isinstance(self.generator, AsyncGenerator):
            raise TypeError("Cursor is not async")

        return self.model_cls.model_validate(await self.generator.__anext__())

    def __next__(self) -> "DocumentBase":
        if not isinstance(self.generator, Generator):
            raise TypeError("Cursor is not sync")

        return self.model_cls.model_validate(next(self.generator))
