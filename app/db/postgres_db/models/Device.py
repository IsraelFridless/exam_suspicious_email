from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    os = Column(String, nullable=False)
    browser = Column(String, nullable=False)
    message_id = Column(Integer, ForeignKey('messages.id'), nullable=False)

    message = relationship(
        'Message',
        back_populates='device'
    )