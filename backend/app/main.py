import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import task_router
from app.routers import subtask_router
from app.services.alarm_service import check_alarms_periodically
from app.routers import alarm_router
from app.routers import dashboard_router
from app.routers import notification_router
from app.routers import history_router
from app.routers import analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Learning Scheduler Backend")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],         
)

app.include_router(subtask_router.router)
app.include_router(task_router.router)
app.include_router(dashboard_router.router)
app.include_router(alarm_router.router)
app.include_router(notification_router.router)
app.include_router(history_router.router)
app.include_router(analytics_router.router)


@app.get("/")
def root():
    return {"message": "Learning Scheduler API running"}


@app.on_event("startup")
async def start_alarm_service():
    asyncio.create_task(check_alarms_periodically())

