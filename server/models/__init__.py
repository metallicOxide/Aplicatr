from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from server.config import DATABASE

DeclarativeBase = declarative_base()

"""
Performs database connection using database settings from config.py.
Returns sqlalchemy engine instance.
"""
print("Connecting to database...")
engine = create_engine(URL(**DATABASE))

# import all database models
from server.models.Base import Base
from server.models.Searches import Searches
from server.models.Users import Users

'''
Creates database tables from models attached to DeclarativeBase
'''
print("Creating database tables...")
DeclarativeBase.metadata.create_all(engine)
