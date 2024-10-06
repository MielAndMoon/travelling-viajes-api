from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    image_url: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
