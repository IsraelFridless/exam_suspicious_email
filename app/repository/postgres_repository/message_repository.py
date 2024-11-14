from typing import List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import Message, Device, Location, SentenceExplosive, SentenceHostage


def insert_message(message: Message) -> int:
    with session_maker() as session:
        try:
            session.add(message)
            session.commit()
            session.refresh(message)
            return message.id
        except Exception as e:
            session.rollback()
            print(e)


def get_suspicious_data_by_email(email: str) -> List[Message]:
    with session_maker() as session:
        try:
            result = (
                session.query(Message)
                .options(
                    joinedload(Message.device),
                    joinedload(Message.location),
                    joinedload(Message.explosive_sentences),
                    joinedload(Message.hostage_sentences),
                )
                .filter(Message.email == email)
                .all()
            )
            return result
        except SQLAlchemyError as e:
            print(f"Error retrieving data for email {email}: {e}")
            return []

