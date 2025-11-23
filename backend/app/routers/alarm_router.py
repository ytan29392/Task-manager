from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.alarm_schema import AlarmCreate, AlarmResponse, AlarmUpdate
from app.crud import alarm_crud

router = APIRouter(prefix="/alarms", tags=["Alarms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AlarmResponse)
def create_alarm(data: AlarmCreate, db: Session = Depends(get_db)):
    return alarm_crud.create_alarm(db, data)

@router.put("/{alarm_id}", response_model=AlarmResponse)
def update_alarm(alarm_id: int, data: AlarmUpdate, db: Session = Depends(get_db)):
    alarm = alarm_crud.update_alarm(db, alarm_id, data)
    if not alarm:
        raise HTTPException(404, "Alarm not found")
    return alarm
