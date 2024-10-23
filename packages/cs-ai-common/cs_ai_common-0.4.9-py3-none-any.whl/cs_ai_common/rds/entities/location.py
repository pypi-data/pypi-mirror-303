from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from cs_ai_common.rds.entities.base import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(20), nullable=False)
    advertisements = relationship('Advertisement', back_populates='location')