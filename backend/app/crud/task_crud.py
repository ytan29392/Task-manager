from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.schemas.task_schema import TaskCreate

def create_task(db: Session, data: TaskCreate):
    task = Task(
        title=data.title,
        description=data.description,
        start_time=data.start_time,
        end_time=data.end_time,
        total_duration=data.total_duration,
        status=TaskStatus.TODO
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all_tasks(db: Session):
    return db.query(Task).all()
