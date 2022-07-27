from sqlalchemy import Column, DateTime, Integer, Float
from sqlalchemy.sql import func
from db.session import Base



class Weather(Base):
    __tablename__ = "weather"
    
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Float)
    created = Column(DateTime, default=func.now(), nullable=False)

    class Config:
        orm_mode = True

