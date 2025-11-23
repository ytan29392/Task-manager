from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.alarm import Alarm, AlarmStatus
from datetime import datetime, timedelta

router = APIRouter(prefix="/notifications", tags=["Notifications"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    now = datetime.now()

    triggered = db.query(Alarm).filter(
        Alarm.status == AlarmStatus.TRIGGERED
    ).all()

    missed = db.query(Alarm).filter(
        Alarm.status == AlarmStatus.MISSED,
        Alarm.reschedule_prompted == True
    ).all()

    return {
        "triggered": [
            {
                "alarm_id": a.id,
                "subtask_id": a.subtask_id,
                "time": a.trigger_time,
                "type": "start"
            } for a in triggered
        ],
        "missed": [
            {
                "alarm_id": a.id,
                "subtask_id": a.subtask_id,
                "time": a.trigger_time,
                "type": "missed"
            } for a in missed
        ]
    }
