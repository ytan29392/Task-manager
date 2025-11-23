from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlarmCreate(BaseModel):
    subtask_id: int
    trigger_time: datetime

class AlarmUpdate(BaseModel):
    status: Optional[str]
    reschedule_prompted: Optional[bool]

class AlarmResponse(BaseModel):
    id: int
    subtask_id: int
    trigger_time: datetime
    status: str
    reschedule_prompted: bool

    class Config:
        orm_mode = True
