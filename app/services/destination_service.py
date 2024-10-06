from sqlalchemy.orm import Session
from app.models.destination import Destination
from app.schemas.destination_schema import DestinationCreate


async def get_destination(db: Session, destination_id: int):
    return db.query(Destination).filter(Destination.id == destination_id).first()


async def get_destinations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Destination).offset(skip).limit(limit).all()


async def create_destination(db: Session, destination: DestinationCreate):
    db_destination = Destination(**destination.model_dump())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination


async def create_destinations(db: Session, destinations: list[DestinationCreate]):
    for destination in destinations:
        _ = await create_destination(db, destination)

    return await get_destinations(db)
