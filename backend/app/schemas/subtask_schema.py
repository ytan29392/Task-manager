from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SubtaskCreate(BaseModel):
    title: str
    description: Optional[str]
    task_id: int
    start_time: datetime
    end_time: datetime
    duration: float

class SubtaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    duration: Optional[float]
    status: Optional[str]
    note: Optional[str]

class SubtaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: datetime
    duration: float
    status: str
    note: Optional[str]
    task_id: int

    class Config:
        orm_mode = True
