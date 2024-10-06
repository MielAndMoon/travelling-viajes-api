from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.favorite import Favorite
from app.schemas.favorite_schema import FavoriteCreate


async def get_favorites_by_user(db: Session, user_id: int):
    favorites = db.query(Favorite).filter(
        Favorite.user_id == user_id).all()
    if not favorites:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No favorites found")
    return favorites


async def get_favorites(db: Session, skip: int = 0, limit: int = 100):
    favorites = db.query(Favorite).offset(skip).limit(limit).all()
    if not favorites:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No favorites found")
    return favorites


async def add_favorite(db: Session, favorite: FavoriteCreate):
    db_favorite = Favorite(**favorite.model_dump())
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite


async def remove_favorite(db: Session, favorite_id: int):
    db_favorite = db.query(Favorite).filter(
        Favorite.id == favorite_id).first()
    if not db_favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Favorite not found")
    db.delete(db_favorite)
    db.commit()
    return db_favorite


async def remove_favorite_by_user_and_destination(db: Session, user_id: int, destination_id: int):
    db_favorite = db.query(Favorite).filter(
        Favorite.user_id == user_id, Favorite.destination_id == destination_id).first()
    if not db_favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Favorite not found")
    db.delete(db_favorite)
    db.commit()
    return db_favorite


async def is_favorite_by_user_and_destination(db: Session, user_id: int, destination_id: int):
    db_favorite = db.query(Favorite).filter(
        Favorite.user_id == user_id, Favorite.destination_id == destination_id).first()
    if not db_favorite:
        return False
    return True


async def create_favorites(db: Session, favorites: list[FavoriteCreate]):
    for favorite in favorites:
        _ = await add_favorite(db, favorite)

    return await get_favorites(db)
