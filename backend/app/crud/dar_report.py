from sqlalchemy.orm import Session
from app.models.dar_report import DARReport
from app.schemas.dar_report import DARReportCreate


def create_dar_report(db: Session, user_id: int, dar_in: DARReportCreate):
    dar = DARReport(user_id=user_id, content=dar_in.content)
    db.add(dar)
    db.commit()
    db.refresh(dar)
    return dar


def get_dar_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DARReport).offset(skip).limit(limit).all()
