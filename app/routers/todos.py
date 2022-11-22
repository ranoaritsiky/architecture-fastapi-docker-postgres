import json
from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from fastapi.encoders import jsonable_encoder

from ..models import models
from ..schemas import schemas
from ..todos import crud
from ..database.db_config import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/todos/", tags=["todos"],  response_model=schemas.Todo)
async def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return JSONResponse(content=jsonable_encoder(todos))

@router.get("/todo/{todo_id}", tags=["todo"])
async def search_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_todo

@router.post("/create_todos/", tags=["create_todo"], response_model=schemas.TodoCreate)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_name(db, name=todo.name)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already registered")
    crud.create_todo(db=db, todo=todo)
    return JSONResponse(content={"response":"todo saved"})

