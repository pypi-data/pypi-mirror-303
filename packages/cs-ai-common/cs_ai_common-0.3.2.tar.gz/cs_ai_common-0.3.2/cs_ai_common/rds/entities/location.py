from sqlalchemy import Column, Integer, String
from cs_ai_common.rds.entities.base import Base
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(20), nullable=False)
    articles = relationship('Advertisement', backref='location')
