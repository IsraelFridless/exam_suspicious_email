from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base, Message


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    message_id = Column(Integer, ForeignKey('messages.id'))

    message = relationship(
        'Message',
        back_populates='location',
    )