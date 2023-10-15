from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Report(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    tech_id: UUID
    client_id: UUID
    activities: list["Activity"]


class Activity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    topics: list["Topic"]


class Topic(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    content: str
