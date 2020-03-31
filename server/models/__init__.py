from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from server.config import DATABASE

DeclarativeBase = declarative_base()
print(DATABASE)
def dbConnect():
    """
    Performs database connection using database settings from config.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))

def dbCreateTables(engine):
  DeclarativeBase.metadata.create_all(engine)