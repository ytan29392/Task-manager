from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.subtask import Subtask

router = APIRouter(prefix="/history", tags=["History"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def completed_subtasks(db: Session = Depends(get_db), month: int = None, year: int = None):
    query = db.query(Subtask).filter(Subtask.status == "Done")

    if month and year:
        from datetime import datetime
        from sqlalchemy import extract
        query = query.filter(
            extract("month", Subtask.updated_at) == month,
            extract("year", Subtask.updated_at) == year
        )

    subtasks = query.all()
    return [
        {
            "id": s.id,
            "title": s.title,
            "objective": s.objective,
            "notes": s.notes,
            "learned_summary": s.learned_summary,
            "time_spent_minutes": s.time_spent_minutes,
            "completed_at": s.updated_at
        } for s in subtasks
    ]
