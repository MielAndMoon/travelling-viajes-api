from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.config.database import Base


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey(
        'destinations.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    user = relationship('User', back_populates='bookings')
    destination = relationship('Destination', back_populates='bookings')
