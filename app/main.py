from fastapi import Depends,FastAPI

from .routers import todos, main

app = FastAPI()

app.include_router(todos.router)
app.include_router(main.router)
