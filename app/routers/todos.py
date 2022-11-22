import json
from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from ..models import models
from ..schemas import schemas
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
async def todos():
    # response = json.dumps({'name':"get up",'description':"rakoto"})
    return JSONResponse(content="rakoto")

@router.get("/todo/{name}", tags=["todo"])
async def todo(name:str):
    return {"name":name}