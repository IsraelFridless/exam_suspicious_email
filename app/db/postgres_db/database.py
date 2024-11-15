from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.db.postgres_db.models import Base
from app.settings.postgres_config import DB_URL

from app.db.postgres_db.models import *

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)



def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)