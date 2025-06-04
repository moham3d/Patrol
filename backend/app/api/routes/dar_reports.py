from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.crud.dar_report import create_dar_report, get_dar_reports
from app.db.session import get_db
from app.schemas.dar_report import DARReportCreate, DARReport
from app.models.user import User

router = APIRouter()


@router.post('/dar_reports/', response_model=DARReport)
def create_report(dar_in: DARReportCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_dar_report(db, current_user.id, dar_in)


@router.get('/dar_reports/', response_model=list[DARReport])
def read_reports(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_dar_reports(db)
