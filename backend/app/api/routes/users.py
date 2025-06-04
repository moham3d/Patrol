from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, User
from app.crud.user import create_user
from app.db.session import get_db

router = APIRouter()


@router.post('/users/', response_model=User)
def create_new_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_in)
