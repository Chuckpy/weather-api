from sqlalchemy.orm import Session
from db import models, schemas
from pydantic import ValidationError
import requests
import os


api_url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY", None)


def get_weather(db:Session, skip: int = 0, limit : int = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()


def get_weather_by_id(db:Session, id: int):
    return db.query(models.Weather).filter(models.Weather.id == id).first()


def store_weather(city_id, db:Session):   
    response  = requests.get(f"{api_url}?id={city_id.city_id}&appid={API_KEY}")
    if response.status_code == 200:
        try :
            response_dict = response.json()
            weather = schemas.WeatherBase.parse_obj({
                "city_id" : city_id.city_id,
                "temperature" : (response_dict['main']['temp'] - 273.15),
                "humidity" : response_dict['main']['humidity']
            })
            db_weather = models.Weather(**weather.dict())
            db.add(db_weather)
            db.commit()
            db.refresh(db_weather)
            return db_weather
        except ValidationError as e :
            return e.str()
    return response.json()

