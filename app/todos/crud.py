from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todos).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todos).filter(models.Todos.id == todo_id).first()

def get_todo_by_name(db: Session, name: str):
    return db.query(models.Todos).filter(models.Todos.name == name).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todos(name=todo.name, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = db.query(models.Todos).filter(models.Todos.name == todo.name).first()
    db.delete(db_todo)
    db.commit()
