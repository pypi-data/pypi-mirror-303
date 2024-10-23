from enum import Enum

from pydantic import BaseModel, ConfigDict


class Role(Enum):
    System = "system"
    User = "user"
    Assistant = "assistant"


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Role
    content: str
