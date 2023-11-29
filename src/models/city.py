from sqlalchemy import Column, String, Integer

from .base import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)

    def __repr__(self):
        return self.name
