from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class Device(Base):
    __tablename__ = "devices"
    id = Column(String, primary_key=True)
    os = Column(String, nullable=True)
    browser = Column(String, nullable=True)


    message = relationship(
        'Message',
        back_populates='device'
    )