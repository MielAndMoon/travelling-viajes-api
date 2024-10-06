from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.config.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserSignIn


async def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


async def get_user_by_email(db: Session, email: EmailStr):
    return db.query(User).filter(User.email == email).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


async def register_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(first_name=user.first_name, last_name=user.last_name,
                   username=user.username, email=user.email,
                   password=hashed_password, image_url=user.image_url)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def sign_in_user(db: Session, user: UserSignIn):
    db_user = await get_user_by_email(db, user.email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    return db_user


async def create_users(db: Session, users: list[UserCreate]):
    for user in users:
        _ = await register_user(db, user)

    return await get_users(db)
