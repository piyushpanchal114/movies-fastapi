from fastapi import FastAPI
from .apis import movies

app = FastAPI()
app.include_router(movies)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
