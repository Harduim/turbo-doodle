from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Client(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
