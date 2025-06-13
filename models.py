from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):## basemodel is for data validation
    title: str
    completed: Optional[bool] = False  #default false if can be filled or not