from datetime import timezone
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Movie(Base):
    """Movie Schema"""
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    plot = Column(String(1000), nullable=True)
    genres = Column(JSON, default=list)
    casts = Column(JSON, default=list)
    created_at = Column(DateTime, default=timezone.utc)
