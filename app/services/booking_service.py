from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.schemas.booking_schema import BookingCreate, BookingUpdate


async def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()


async def get_bookings_by_user(db: Session, user_id: int):
    bookings = db.query(Booking).filter(Booking.user_id == user_id).all()
    if not bookings:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No bookings found")
    return bookings


async def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    bookings = db.query(Booking).offset(skip).limit(limit).all()
    if not bookings:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No bookings found")
    return bookings


async def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


async def update_booking(db: Session, booking_id: int, booking: BookingUpdate):
    db_booking = await get_booking(db, booking_id)
    if not db_booking:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

    for key, value in booking.model_dump().items():
        setattr(db_booking, key, value)

    db.commit()
    db.refresh(db_booking)
    return db_booking


async def create_bookings(db: Session, bookings: list[BookingCreate]):
    for booking in bookings:
        _ = await create_booking(db, booking)
    return await get_bookings(db)
