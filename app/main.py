from fastapi import Depends,FastAPI

from .routers import todos

app = FastAPI()

app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message":"hello world"}