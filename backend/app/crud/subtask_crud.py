from sqlalchemy.orm import Session
from app.models.subtask import Subtask, SubtaskStatus
from app.schemas.subtask_schema import SubtaskCreate, SubtaskUpdate

def create_subtask(db: Session, data: SubtaskCreate):
    subtask = Subtask(
        title=data.title,
        description=data.description,
        task_id=data.task_id,
        start_time=data.start_time,
        end_time=data.end_time,
        duration=data.duration,
        status=SubtaskStatus.TODO,
    )
    db.add(subtask)
    db.commit()
    db.refresh(subtask)
    return subtask

def get_subtasks_by_task(db: Session, task_id: int):
    return db.query(Subtask).filter(Subtask.task_id == task_id).all()

def update_subtask(db: Session, subtask_id: int, data: SubtaskUpdate):
    subtask = db.query(Subtask).filter(Subtask.id == subtask_id).first()
    if not subtask:
        return None

    for field, value in data.dict(exclude_unset=True).items():
        setattr(subtask, field, value)

    db.commit()
    db.refresh(subtask)
    return subtask

def delete_subtask(db: Session, subtask_id: int):
    subtask = db.query(Subtask).filter(Subtask.id == subtask_id).first()
    if not subtask:
        return False

    db.delete(subtask)
    db.commit()
    return True
