from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    is_admin = Column(Boolean, default=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)

    city = relationship('City', foreign_keys=[city_id], backref='users')

    def __repr__(self):
        return self.name
