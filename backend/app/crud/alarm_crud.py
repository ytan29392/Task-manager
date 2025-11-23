from sqlalchemy.orm import Session
from datetime import datetime
from app.models.alarm import Alarm, AlarmStatus
from app.schemas.alarm_schema import AlarmCreate, AlarmUpdate

def create_alarm(db: Session, data: AlarmCreate):
    alarm = Alarm(
        subtask_id=data.subtask_id,
        trigger_time=data.trigger_time,
        status=AlarmStatus.PENDING
    )
    db.add(alarm)
    db.commit()
    db.refresh(alarm)
    return alarm

def get_pending_alarms(db: Session):
    return db.query(Alarm).filter(Alarm.status == AlarmStatus.PENDING).all()

def mark_triggered(db: Session, alarm: Alarm):
    alarm.status = AlarmStatus.TRIGGERED
    db.commit()

def mark_missed(db: Session, alarm: Alarm):
    alarm.status = AlarmStatus.MISSED
    db.commit()

def update_alarm(db: Session, alarm_id: int, data: AlarmUpdate):
    alarm = db.query(Alarm).filter(Alarm.id == alarm_id).first()
    if not alarm:
        return None
    
    for k, v in data.dict(exclude_unset=True).items():
        setattr(alarm, k, v)

    db.commit()
    db.refresh(alarm)
    return alarm
