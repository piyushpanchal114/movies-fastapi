from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]


class Movie(BaseModel):
    name: str
    plot: str
    genres: list[str]
    casts: list[str]


@app.get("/")
async def ping():
    return {"message": "pong"}


@app.get("/movies")
async def movies() -> list[Movie]:
    return fake_movie_db
