from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.task import Task
from app.models.subtask import Subtask
from app.models.alarm import Alarm, AlarmStatus
from datetime import datetime
from app.utils.helpers import calculate_task_progress, count_statuses

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def dashboard_summary(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    subtasks = db.query(Subtask).all()

    # Task progress summary
    task_progress = []
    for task in tasks:
        progress = calculate_task_progress(task.subtasks)
        task.progress = progress
        db.commit()
        task_progress.append({
            "task_id": task.id,
            "title": task.title,
            "progress": progress,
            "status": task.status
        })

    # Subtask status summary
    subtask_summary = count_statuses(subtasks)

    # Today's alarms
    now = datetime.now().date()
    todays_alarms = db.query(Alarm).filter(
        Alarm.trigger_time >= datetime(now.year, now.month, now.day),
        Alarm.trigger_time < datetime(now.year, now.month, now.day + 1),
        Alarm.status == AlarmStatus.PENDING
    ).all()

    upcoming_sessions = [
        {
            "alarm_id": a.id,
            "subtask_id": a.subtask_id,
            "trigger_time": a.trigger_time
        }
        for a in todays_alarms
    ]

    # Overdue subtasks
    overdue_subtasks = db.query(Subtask).filter(Subtask.status == "Overdue").all()

    return {
        "task_progress": task_progress,
        "subtask_summary": subtask_summary,
        "upcoming_sessions": upcoming_sessions,
        "overdue_subtasks": [
            {"id": s.id, "title": s.title, "task_id": s.task_id}
            for s in overdue_subtasks
        ]
    }
