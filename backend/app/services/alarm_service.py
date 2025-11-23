import asyncio
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.alarm import AlarmStatus
from app.models.subtask import Subtask, SubtaskStatus
from app.crud import alarm_crud

CHECK_INTERVAL = 60   # seconds

async def check_alarms_periodically():
    while True:
        await asyncio.sleep(CHECK_INTERVAL)
        check_alarms()
        

def check_alarms():
    db: Session = SessionLocal()

    try:
        now = datetime.now()
        alarms = alarm_crud.get_pending_alarms(db)

        for alarm in alarms:
            # Trigger window: If within 1 minute after trigger_time
            if now >= alarm.trigger_time and now <= alarm.trigger_time + timedelta(minutes=1):
                # Mark alarm triggered
                alarm.status = AlarmStatus.TRIGGERED
                db.commit()

            # Missed alarm (learning didn’t happen)
            elif now > alarm.trigger_time + timedelta(minutes=1):
                alarm.status = AlarmStatus.MISSED
                alarm.reschedule_prompted = True

                # Mark subtask overdue
                subtask = db.query(Subtask).filter(Subtask.id == alarm.subtask_id).first()
                if subtask and subtask.status != SubtaskStatus.DONE:
                    subtask.status = SubtaskStatus.OVERDUE
                db.commit()

    finally:
        db.close()
