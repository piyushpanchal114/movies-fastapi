from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models
from .db import get_db_session
from .schemas import CastList, Cast


casts = APIRouter(prefix="/casts")


@casts.get("/", status_code=status.HTTP_200_OK)
async def get_all_cast(
        session: AsyncSession = Depends(get_db_session)) -> list[CastList]:
    casts = await session.scalars(select(models.Cast))
    return casts


@casts.post("/", status_code=status.HTTP_201_CREATED)
async def create_cast(
    payload: Cast,
        session: AsyncSession = Depends(get_db_session)) -> Cast:
    cast = models.Cast(**payload.model_dump())
    session.add(cast)
    await session.commit()
    await session.refresh(cast)
    return cast


@casts.get("/{id}", status_code=status.HTTP_200_OK)
async def get_cast(session: AsyncSession = Depends(get_db_session)) -> Cast:
    cast = await session.get(models.Cast, id)
    if cast is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="cast not found")
    return cast
