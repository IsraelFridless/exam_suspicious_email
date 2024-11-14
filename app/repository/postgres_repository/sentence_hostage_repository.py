from typing import List

from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import SentenceHostage


def insert_many_hostage_sentences(hostage_sentences: List[SentenceHostage]):
    with session_maker() as session:
        try:
            session.add_all(hostage_sentences)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)