from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Client(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
