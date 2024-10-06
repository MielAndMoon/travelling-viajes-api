from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.favorite_schema import FavoriteResponse, FavoriteCreate
from app.schemas.destination_schema import DestinationResponse
from app.services import favorite_service
from app.config.database import get_db

route = APIRouter(
    prefix="/favorites",
    tags=["Favorites"],
    responses={404: {"description": "Not found"}},
)


@route.get("/{user_id}", response_model=list[DestinationResponse])
async def get_favorites_by_user(user_id: int, db: Session = Depends(get_db)):
    favorites = await favorite_service.get_favorites_by_user(db, user_id)
    destinations = [favorite.destination for favorite in favorites]
    return destinations


@route.post("/add", response_model=FavoriteResponse)
async def add_favorite(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return await favorite_service.add_favorite(db, favorite)


@route.delete("/{favorite_id}", response_model=FavoriteResponse)
async def remove_favorite(favorite_id: int, db: Session = Depends(get_db)):
    return await favorite_service.remove_favorite(db, favorite_id)


@route.delete("/remove/{user_id}/{destination_id}", response_model=FavoriteResponse)
async def remove_favorite_by_user_and_destination(user_id: int, destination_id: int, db: Session = Depends(get_db)):
    return await favorite_service.remove_favorite_by_user_and_destination(db, user_id, destination_id)


@route.get("/{user_id}/{destination_id}", response_model=bool)
async def is_favorite_by_user_and_destination(user_id: int, destination_id: int, db: Session = Depends(get_db)):
    return await favorite_service.is_favorite_by_user_and_destination(db, user_id, destination_id)


@route.post('/bulk', response_model=list[FavoriteResponse])
async def create_favorites(favorites: list[FavoriteCreate], db: Session = Depends(get_db)):
    return await favorite_service.create_favorites(db, favorites)


@route.get("/", response_model=list[FavoriteResponse])
async def get_favorites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await favorite_service.get_favorites(db, skip, limit)
