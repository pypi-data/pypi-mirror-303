from typing import Annotated, Literal, TypeVar

import bson  # type: ignore[import-untyped]
import bson.json_util  # type: ignore[import-untyped]
from pydantic import BeforeValidator, StringConstraints

T = TypeVar("T")

_ObjectIdString = Annotated[
    str, StringConstraints(min_length=24, max_length=24, pattern=r"^[a-f\d]{24}$")
]

_DictObjectId = dict[Literal["$oid"], _ObjectIdString]


def check_object_id(value: _ObjectIdString | _DictObjectId) -> str:
    if isinstance(value, dict):
        value = value["$oid"]

    if not bson.ObjectId.is_valid(value):
        raise ValueError("Invalid ObjectId")

    return str(value)


ObjectId = Annotated[
    _ObjectIdString,
    BeforeValidator(check_object_id),
]

__all__ = ["ObjectId"]
