from typing import List

from app.db.postgres_db.database import session_maker
from app.db.postgres_db.models import SentenceExplosive


def insert_many_explosive_sentences(explosive_sentences: List[SentenceExplosive]):
    with session_maker() as session:
        try:
            session.add_all(explosive_sentences)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)