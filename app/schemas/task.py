from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "todo"
    priority: Optional[str] = "medium"
    board_id: int


class TaskCreate(TaskBase):
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskMove(BaseModel):
    status: str
    position: int


class TaskAssign(BaseModel):
    assigned_to: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    position: int
    assigned_to: Optional[int] = None

    class Config:
        orm_mode = True
