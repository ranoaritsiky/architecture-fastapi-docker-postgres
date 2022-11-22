from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas


def get_todo(db:Session, todo_id:int):
    return db.query(models.Todos).filter(models.Todos.id == todo_id).first()