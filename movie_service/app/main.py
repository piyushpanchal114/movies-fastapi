from fastapi import FastAPI
from .apis import movies


app = FastAPI(openapi_url="/movies/openapi.json", docs_url="/movies/docs")
app.include_router(movies)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
