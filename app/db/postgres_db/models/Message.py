from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(String, primary_key=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    message_created_at = Column(String, nullable=True)
    device_id = Column(String, ForeignKey('devices.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))

    location = relationship(
        'Location',
        back_populates='message',
        foreign_keys=[location_id]
    )

    device = relationship(
        'Device',
        back_populates='message',
        foreign_keys=[device_id]
    )

    explosive_sentences = relationship(
        'SentenceExplosive',
        back_populates='message',
        cascade='all, delete-orphan'
    )

    hostage_sentences = relationship(
        'SentenceHostage',
        back_populates='message',
        cascade='all, delete-orphan'
    )