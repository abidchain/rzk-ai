from fastapi import APIRouter
from .schemas import UserCreate

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to RZK AI API"
    }


@router.post("/signup")
def signup(user: UserCreate):
    return {
        "success": True,
        "message": "User registered successfully",
        "user": user
    }
