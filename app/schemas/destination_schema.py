from pydantic import BaseModel


class DestinationBase(BaseModel):
    name: str
    description: str
    location: str
    image_url: str


class DestinationCreate(DestinationBase):
    pass


class DestinationResponse(DestinationBase):
    id: int

    class Config:
        from_attributes = True
