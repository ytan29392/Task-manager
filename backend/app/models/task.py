from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class TaskStatus(str, enum.Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    OVERDUE = "Overdue"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    total_duration = Column(Float, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.TODO)
    progress = Column(Float, default=0.0)

    subtasks = relationship("Subtask", back_populates="task", cascade="all, delete")
