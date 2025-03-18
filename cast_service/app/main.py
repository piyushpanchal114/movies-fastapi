from fastapi import FastAPI
from .apis import casts


app = FastAPI(openapi_url="/casts/openapi.json", docs_url="/casts/docs")
app.include_router(casts)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
