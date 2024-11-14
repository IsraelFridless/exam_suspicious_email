from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgres_db.models import Base


class Mission(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    device_id = Column(String, ForeignKey('devices.id'))
    location_id = Column(String, ForeignKey('locations.id'))


    device = relationship(
        'Device',
        back_populates='user'
    )