from app.config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    destination_id = Column(Integer, ForeignKey(
        'destinations.id'), nullable=False)

    user = relationship('User', back_populates='favorites')
    destination = relationship('Destination', back_populates='favorites')
