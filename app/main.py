from fastapi import FastAPI
from app.config.database import engine, Base
from app.routes import destination_route, favorite_route, user_route, booking_route

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.route, prefix="/api/v1")
app.include_router(destination_route.route, prefix="/api/v1")
app.include_router(favorite_route.route, prefix="/api/v1")
app.include_router(booking_route.route, prefix="/api/v1")
