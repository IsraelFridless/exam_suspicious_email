from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings.postgres_config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)