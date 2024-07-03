from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..auth import oauth2_scheme
from ..schemas import Task, TaskCreate,User
from ..crud import create_task, get_tasks
from ..database import SessionLocal
from jose import JWTError, jwt
from typing import List
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception
    return user

@router.post("/tasks/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db=db, task=task, user_id=current_user.id)

@router.get("/tasks/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = get_tasks(db, user_id=current_user.id)
    return tasks
