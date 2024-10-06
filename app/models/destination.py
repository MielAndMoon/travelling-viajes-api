from app.config.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    location = Column(String(255))
    image_url = Column(String(255))

    bookings = relationship('Booking', back_populates='destination')
    favorites = relationship('Favorite', back_populates='destination')
