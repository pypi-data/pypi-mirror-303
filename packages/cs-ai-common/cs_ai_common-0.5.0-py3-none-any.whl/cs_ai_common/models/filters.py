from typing import Optional
from pydantic import BaseModel

class Filter(BaseModel):
    make: str
    model: str
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    min_year: Optional[int] = None
    max_year: Optional[int] = None
    min_mileage: Optional[int] = None
    max_mileage: Optional[int] = None
    min_engine_capacity: Optional[int] = None
    max_engine_capacity: Optional[int] = None
    min_horsepower: Optional[int] = None
    max_horsepower: Optional[int] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    source: Optional[str] = None
    location: Optional[str] = None
