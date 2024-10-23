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


D = TypeVar("D", bound="DocumentBase")
P = ParamSpec("P")

AG = AsyncGenerator["DocumentBase", None]
G = Generator["DocumentBase", None, None]


class Cursor(Generic[D]):
    model_cls: D

    def __init__(
        self, cursor: pymongo.cursor.Cursor | motor.motor_asyncio.AsyncIOMotorCursor
    ) -> None:
        self.cursor = cursor
        self.generator: G | AG | None = None

    def __class_getitem__(cls, item: D) -> Self:
        result = super().__class_getitem__(item)  # type: ignore[misc]
        result.model_cls = item
        return cast(Self, result)

    def __aiter__(self) -> Self:
        self.generator = self.cursor.__aiter__()
        return self

    def __iter__(self) -> Self:
        self.generator = self.cursor.__iter__()
        return self

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> "Cursor[D]":
        return Cursor[self.model_cls](self.cursor(*args, **kwargs))  # type: ignore[name-defined]

    def __getattr__(self, item: str) -> Self | Any:
        value = getattr(self.cursor, item)

        if callable(value):
            return Cursor[self.model_cls](value)  # type: ignore[name-defined]

        return value

    async def __anext__(self) -> D:
        return self.model_cls.model_validate(await self.generator.__anext__())

    def __next__(self) -> D:
        return self.model_cls.model_validate(next(self.generator))
