from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    postal_code = Column(String(20), nullable=False)
    articles = relationship('Advertisement', backref='location')
