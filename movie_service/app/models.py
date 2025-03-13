from pydantic import BaseModel


class Movie(BaseModel):
    """Model for Movie"""
    name: str
    plot: str
    genres: list[str]
    casts: list[str]
