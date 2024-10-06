from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.destination_schema import DestinationCreate, DestinationResponse
from app.services import destination_service

route = APIRouter(
    prefix="/destinations",
    tags=["Destinations"],
    responses={404: {"description": "Not found"}},
)


@route.get("/{destination_id}", response_model=DestinationResponse)
async def get_destination(destination_id: int, db: Session = Depends(get_db)):
    return await destination_service.get_destination(db, destination_id)


@route.get("/", response_model=list[DestinationResponse])
async def get_destinations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await destination_service.get_destinations(db, skip, limit)


@route.post("/", response_model=DestinationResponse)
async def create_destination(destination: DestinationCreate, db: Session = Depends(get_db)):
    return await destination_service.create_destination(db, destination)


@route.post('/bulk', response_model=list[DestinationResponse])
async def create_destinations(destinations: list[DestinationCreate], db: Session = Depends(get_db)):
    return await destination_service.create_destinations(db, destinations)
