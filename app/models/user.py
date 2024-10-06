from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    username = Column(String(50), unique=True)
    password = Column(String(100))
    email = Column(String(50), unique=True)
    image_url = Column(String(255))

    bookings = relationship('Booking', back_populates='user')
    favorites = relationship('Favorite', back_populates='user')
