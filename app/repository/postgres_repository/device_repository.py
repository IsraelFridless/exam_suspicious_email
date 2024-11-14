from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import Device


def insert_device(device: Device):
    with session_maker() as session:
        try:
            session.add(device)
            session.commit()
            session.refresh(device)
            return device.id
        except Exception as e:
            session.rollback()
            print(e)
