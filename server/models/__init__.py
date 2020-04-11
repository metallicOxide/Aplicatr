from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from server.config import DATABASE
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()

#TODO: implement migrations support with new database updates (using alembic?)

"""
Performs database connection using database settings from config.py.
Returns sqlalchemy engine instance.
"""
print("Connecting to database...")
engine = create_engine(URL(**DATABASE))
db_session = sessionmaker(bind=engine) # to be used for any database session

# import all database models
from server.models.Base import Base
from server.models.Search import Search
from server.models.User import User

'''
Creates database tables from models attached to DeclarativeBase
'''
# TODO: create a script to reset database / run migrations
print("Creating database tables...")
DeclarativeBase.metadata.create_all(engine)
