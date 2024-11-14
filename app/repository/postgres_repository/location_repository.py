from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import Location


def insert_location(location: Location) -> int:
    with session_maker() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return location.id
        except Exception as e:
            session.rollback()
            print(e)