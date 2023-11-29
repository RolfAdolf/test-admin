from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', foreign_keys=[user_id], backref='tasks')
    status = relationship('Status', foreign_keys=[status_id], backref='tasks')

    def __repr__(self):
        return self.name
