from fastapi import APIRouter
from app.schemas.user_schema import UserRegister

router = APIRouter()

@router.get("/test")
def test():
    return {"status": "Auth API is working"}

@router.post("/register")
def register(user : UserRegister):
    
    if user.password != user.confirm_password:
        return {"error":"Passwords does not match"}

    return {        
        "username": user.username,
        "email": user.email,
        "message": "User data received"
    }