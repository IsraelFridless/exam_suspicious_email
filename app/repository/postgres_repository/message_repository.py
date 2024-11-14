from returns.result import Result, Success, Failure

from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import Message


def insert_message(message: Message):
    with session_maker() as session:
        try:
            session.add(message)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)