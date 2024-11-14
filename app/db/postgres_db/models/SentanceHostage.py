from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class SentenceHostage(Base):
    __tablename__ = "suspicious_hostage_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    message_id = Column(Integer, ForeignKey('messages.id'), nullable=False)

    message = relationship(
        'Message',
        back_populates='hostage_sentences'
    )