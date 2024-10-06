from pydantic import BaseModel
from datetime import date


class BookingBase(BaseModel):
    user_id: int
    destination_id: int
    start_date: date
    end_date: date


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int

    class Config:
        from_attributes = True


class BookingUpdate(BookingBase):
    pass
