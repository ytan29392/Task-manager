from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class AlarmStatus(str, enum.Enum):
    PENDING = "Pending"
    TRIGGERED = "Triggered"
    MISSED = "Missed"

class Alarm(Base):
    __tablename__ = "alarms"

    id = Column(Integer, primary_key=True, index=True)
    subtask_id = Column(Integer, ForeignKey("subtasks.id"))
    trigger_time = Column(DateTime, nullable=False)
    status = Column(Enum(AlarmStatus), default=AlarmStatus.PENDING)
    reschedule_prompted = Column(Boolean, default=False)

    subtask = relationship("Subtask")
