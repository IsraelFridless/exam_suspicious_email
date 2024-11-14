from sqlalchemy.orm import declarative_base, DeclarativeMeta

Base: DeclarativeMeta = declarative_base()

from .Message import Message
from .Device import Device
from .Location import Location
from .SentanceHostage import SentenceHostage
from .SentenceExplosive import SentenceExplosive