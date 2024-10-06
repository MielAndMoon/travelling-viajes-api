from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.booking_schema import BookingCreate, BookingResponse, BookingUpdate
from app.services import booking_service

route = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
    responses={404: {"description": "Not found"}},
)


@route.get("/{user_id}", response_model=list[BookingResponse])
async def get_bookings_by_user(user_id: int, db: Session = Depends(get_db)):
    return await booking_service.get_bookings_by_user(db, user_id)


@route.post("/", response_model=BookingResponse)
async def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return await booking_service.create_booking(db, booking)


@route.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: int, db: Session = Depends(get_db)):
    return await booking_service.get_booking(db, booking_id)


@route.put("/{booking_id}", response_model=BookingResponse)
async def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    return await booking_service.update_booking(db, booking_id, booking)


@route.post('/bulk', response_model=list[BookingResponse])
async def create_bookings(bookings: list[BookingCreate], db: Session = Depends(get_db)):
    return await booking_service.create_bookings(db, bookings)
