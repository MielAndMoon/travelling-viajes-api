from fastapi import APIRouter, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserResponse
from app.schemas.user_schema import UserCreate, UserSignIn
from app.services import user_service
from app.config.database import get_db

route = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@route.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await user_service.get_user(db, user_id)


@route.get("/email/{email}", response_model=UserResponse)
async def get_user_by_email(email: EmailStr, db: Session = Depends(get_db)):
    return await user_service.get_user_by_email(db, email)


@route.get("/", response_model=list[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await user_service.get_users(db, skip, limit)


@route.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return await user_service.register_user(db, user)


@route.post("/signin", response_model=UserResponse)
async def sign_in_user(user: UserSignIn, db: Session = Depends(get_db)):
    return await user_service.sign_in_user(db, user)


@route.post('/bulk', response_model=list[UserResponse])
async def create_users(users: list[UserCreate], db: Session = Depends(get_db)):
    return await user_service.create_users(db, users)
