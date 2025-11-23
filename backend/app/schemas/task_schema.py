from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SubtaskSimple(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    total_duration: Optional[float]

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    progress: float
    status: str
    subtasks: List[SubtaskSimple]

    class Config:
        orm_mode = True
