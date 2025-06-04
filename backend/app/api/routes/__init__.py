from fastapi import APIRouter
from . import auth, users, dar_reports

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(dar_reports.router)
