from pydantic import BaseModel
from datetime import datetime


class WeatherBase(BaseModel):
    city_id : int
    temperature : float
    humidity : float

class WeatherDisplay(WeatherBase):
    created : datetime


class WeatherGet(BaseModel):
    city_id : str



