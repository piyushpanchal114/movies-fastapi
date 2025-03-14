import uuid
from datetime import datetime
from sqlalchemy import orm, String, JSON, func


class Base(orm.DeclarativeBase):
    """Base class for declaring model"""
    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True, default=uuid.uuid4)


class Movie(Base):
    """Movie Schema"""
    __tablename__ = "movie"

    name: orm.Mapped[str] = orm.mapped_column(String(255), nullable=False)
    plot: orm.Mapped[str] = orm.mapped_column(String(1000), nullable=True)
    genres: orm.Mapped[dict] = orm.mapped_column(JSON, default=list)
    casts: orm.Mapped[dict] = orm.mapped_column(JSON, default=list)
    created_at: orm.Mapped[datetime] = orm.mapped_column(default=func.now())
