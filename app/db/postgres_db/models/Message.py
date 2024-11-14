from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    message_created_at = Column(String, nullable=False)

    location = relationship(
        'Location',
        back_populates='message',
        uselist=False
    )

    device = relationship(
        'Device',
        back_populates='message',
        uselist=False
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