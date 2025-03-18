from fastapi import FastAPI
from .apis import casts


app = FastAPI()
app.include_router(casts)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
