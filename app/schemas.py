from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from uuid import uuid4, UUID


class UserBaseSchema(BaseModel):

    id: UUID | None = None
    first_name: str = Field(
        ..., description="The first name of the user", example="John"
    )
    last_name: str = Field(..., description="The last name of the user", example="Doe")
    address: str | None = None
    activated: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]


class Status(Enum):
    Success = "Success"
    Failed = "Failed"


class CreateUserResponse(BaseModel):
    Status: Status
    User: UserBaseSchema
