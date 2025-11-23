from fastapi import FastAPI
from app.database import Base, engine
from app.routers import task_router
from app.routers import subtask_router
import asyncio
from app.services.alarm_service import check_alarms_periodically
from app.routers import alarm_router
from app.routers import dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Learning Scheduler Backend")

app.include_router(subtask_router.router)
app.include_router(task_router.router)
app.include_router(dashboard_router.router)
app.include_router(alarm_router.router)


@app.get("/")
def root():
    return {"message": "Learning Scheduler API running"}


@app.on_event("startup")
async def start_alarm_service():
    asyncio.create_task(check_alarms_periodically())

