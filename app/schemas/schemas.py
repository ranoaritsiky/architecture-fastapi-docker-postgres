from typing import List, Union

from pydantic import BaseModel

class TodosBase(BaseModel):
    name:str
    
class TodoCreate(TodosBase):
    description:str
    
class Todo(TodosBase):
    pass    

    class Config:
        orm_mode = True