from fastapi import APIRouter
from .models import Movie


movies = APIRouter()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


@movies.get("/", status_code=200)
async def get_all_movies() -> list[Movie]:
    return fake_movie_db
