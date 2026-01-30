from pydantic import BaseModel
from typing import Optional

# Model used when client CREATES a task
class TaskCreate(BaseModel):
    title: str


# Model used when client PARTIALLY updates a task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


# Model returned by server (actual resource)
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
