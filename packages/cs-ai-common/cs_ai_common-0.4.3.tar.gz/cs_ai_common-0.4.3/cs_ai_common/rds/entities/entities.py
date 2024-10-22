from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(20), nullable=False)
    advertisements = relationship('Advertisement', back_populates='location')

class Advertisement(Base):
    __tablename__ = "advertisements"

    id = Column(Integer(), primary_key=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    production_year = Column(Integer(), nullable=False)
    engine_capacity = Column(Integer(), nullable=False)
    engine_power = Column(Integer(), nullable=False)
    mileage = Column(Integer(), nullable=False)
    transmission = Column(String(30), nullable=False)
    fuel_type = Column(String(30), nullable=False)
    cache_hash = Column(String(100), nullable=False)
    source = Column(String(30), nullable=False)
    link = Column(String(200), nullable=False)
    thumbnail = Column(String(200), nullable=False)
    price = Column(Integer(), nullable=False)
    price_currency = Column(String(20), nullable=False)
    location_code = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    location_id = Column(Integer(), ForeignKey('public.locations.id'))
    location = relationship('Location', back_populates='advertisements')
