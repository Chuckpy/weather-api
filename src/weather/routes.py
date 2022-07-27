from fastapi import APIRouter, Depends
from db import schemas
from db.session import get_db
from sqlalchemy.orm import Session

from weather.services import store_weather,get_weather, get_weather_by_id


weather_router = APIRouter(
    prefix = "/weather",
    tags=["weather"]
)


@weather_router.get("/")
async def home():
    return {"Hello":"World"}

@weather_router.get("/list/")
async def read_weather(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list = get_weather(db, skip=skip, limit=limit)
    return list

@weather_router.get("/{weather_id}/")
async def read_weather_id(weather_id,db: Session = Depends(get_db)):
    return get_weather_by_id(db,weather_id)

@weather_router.post("/")
async def get_info(city_id : schemas.WeatherGet, db:Session = Depends(get_db)):
    return store_weather(city_id,db)


