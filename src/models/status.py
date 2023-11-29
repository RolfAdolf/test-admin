from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .schemes import StatusSchema


class Status(Base):
    __tablename__ = 'status'
    __pydantic_model__ = StatusSchema

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True, index=True)

    def __repr__(self):
        return self.name
