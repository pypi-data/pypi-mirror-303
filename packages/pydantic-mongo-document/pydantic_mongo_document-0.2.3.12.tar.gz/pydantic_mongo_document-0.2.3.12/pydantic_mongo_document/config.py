from typing import Annotated, Any

from pydantic import BaseModel, Field


class ReplicaConfig(BaseModel):
    """Mongodb replica config model."""

    uri: Annotated[
        str,
        Field(..., description="Mongodb connection URI."),
    ]
    client_options: dict[str, Any] = Field(
        default_factory=dict,
        description="Mongodb client options.",
    )
