import uuid
from datetime import datetime
from sqlalchemy import orm, String, func


class Base(orm.DeclarativeBase):
    """Base class for declaring models"""
    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True, unique=True)


class Cast(Base):
    """Model for Cast"""
    __tablename__ = "cast"

    name: orm.Mapped[str] = orm.mapped_column(
        String(255), nullable=False)
    nationality: orm.Mapped[str] = orm.mapped_column(String(100))
    created_at: orm.Mapped[datetime] = orm.mapped_column(default=func.now)
