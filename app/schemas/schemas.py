from typing import List, Union

from pydantic import BaseModel

class TodosBase(BaseModel):
    name:str
    
class Todo(TodosBase):
    description:str
    
    class Config:
        orm_mode = True