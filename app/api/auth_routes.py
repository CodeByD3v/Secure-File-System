from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserRegister
from app.services.auth_service import register_user
from app.database.connection import get_db

router = APIRouter()

@router.get("/test")
def test():
    return {"status": "Auth API is working"}

@router.post("/register")
def register(user : UserRegister , db:Session = Depends(get_db)):
    return register_user(user , db)
