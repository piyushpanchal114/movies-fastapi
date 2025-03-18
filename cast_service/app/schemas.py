import uuid
from pydantic import BaseModel


class Cast(BaseModel):
    """Model for Cast"""
    name: str
    nationality: str


class CastList(Cast):
    """Model for Cast Listing"""
    pk: uuid.UUID
