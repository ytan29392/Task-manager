from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.subtask_schema import SubtaskCreate, SubtaskUpdate, SubtaskResponse
from app.crud import subtask_crud
from app.dependencies import get_current_user
from app.models.user import User
from app.models.subtask import Subtask

router = APIRouter(prefix="/subtasks", tags=["Subtasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_subtasks(
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    return db.query(Subtask).filter(Subtask.user_id == current_user.id).all()

@router.post("/", response_model=SubtaskResponse)
def create_subtask(data: SubtaskCreate, db: Session = Depends(get_db)):
    return subtask_crud.create_subtask(db, data)

@router.get("/task/{task_id}", response_model=list[SubtaskResponse])
def get_subtasks(task_id: int, db: Session = Depends(get_db)):
    return subtask_crud.get_subtasks_by_task(db, task_id)

@router.put("/{subtask_id}", response_model=SubtaskResponse)
def update_subtask(subtask_id: int, data: SubtaskUpdate, db: Session = Depends(get_db)):
    subtask = subtask_crud.update_subtask(db, subtask_id, data)
    if not subtask:
        raise HTTPException(404, "Subtask not found")
    return subtask

@router.delete("/{subtask_id}")
def delete_subtask(subtask_id: int, db: Session = Depends(get_db)):
    ok = subtask_crud.delete_subtask(db, subtask_id)
    if not ok:
        raise HTTPException(404, "Subtask not found")
    return {"message": "Subtask deleted"}

@router.get("/{subtask_id}", response_model=SubtaskResponse)
def get_subtask(subtask_id: int, db: Session = Depends(get_db)):
    subtask = db.query(Subtask).filter(Subtask.id == subtask_id).first()
    if not subtask:
        raise HTTPException(404, "Subtask not found")
    return subtask
