from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Movie
from .db import get_db_session
from . import models


movies = APIRouter()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


@movies.get("/", status_code=status.HTTP_200_OK)
async def get_all_movies(
        session: AsyncSession = Depends(get_db_session)) -> list[Movie]:
    movies = await session.scalars(select(models.Movie))
    return movies


@movies.post("/", status_code=status.HTTP_201_CREATED)
async def create_movie(
     payload: Movie, session: AsyncSession = Depends(get_db_session)) -> Movie:
    movie = models.Movie(**payload.model_dump())
    session.add(movie)
    await session.commit()
    await session.refresh(movie)
    return movie


@movies.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.model_dump()
    movies_length = len(fake_movie_db)
    if 0 <= id < movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404,
                        detail="Movie with given id not found")


@movies.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id < movies_length:
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404,
                        detail="Movie with given id not found")
