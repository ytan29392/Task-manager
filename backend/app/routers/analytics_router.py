from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models.subtask import Subtask

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/monthly_summary")
def monthly_summary(db: Session = Depends(get_db), year: int = None):
    query = db.query(
        func.extract("month", Subtask.updated_at).label("month"),
        func.count(Subtask.id).label("completed_count"),
        func.sum(Subtask.time_spent_minutes).label("total_minutes")
    ).filter(Subtask.status == "Done")

    if year:
        from sqlalchemy import extract
        query = query.filter(extract("year", Subtask.updated_at) == year)

    query = query.group_by("month").order_by("month")
    results = query.all()

    return [{"month": int(r.month), "completed_count": r.completed_count, "total_minutes": r.total_minutes or 0} for r in results]
