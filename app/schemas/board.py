from pydantic import BaseModel
from typing import Optional, List


class BoardBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_public: Optional[bool] = False


class BoardCreate(BoardBase):
    pass


class BoardUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None


class BoardResponse(BoardBase):
    id: int
    owner_id: int
    tasks_count: Optional[int] = 0

    class Config:
        orm_mode = True


class BoardWithTasks(BoardResponse):
    tasks: List[dict] = []
