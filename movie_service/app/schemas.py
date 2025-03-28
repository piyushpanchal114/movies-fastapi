import uuid
from pydantic import BaseModel


class Movie(BaseModel):
    """Model for Movie"""
    name: str
    plot: str
    genres: list[str]
    casts: list[str]


class MovieList(BaseModel):
    """Model for Movie List"""
    pk: uuid.UUID
    name: str
    plot: str
    genres: list[str]
    casts: list[str]
