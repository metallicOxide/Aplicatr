from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, LargeBinary
from server.models import DeclarativeBase
from server.models.Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

class Users(DeclarativeBase, Base):
  __tablename__ = "users"
  __table_args__ = (
    UniqueConstraint('username'),
  )
  id = Column(Integer, primary_key=True)
  username = Column('username', String)
  uni = Column('uni', String)
  last_session_cookie_jar = Column('last_session_cookie_jar', LargeBinary) # for the uni job portal cookie, not our app jwt token. requestcookiejar stored in pickled form
  searches = relationship("Searches", backref='user', cascade="all,delete") # if user gets deleted, all the corresponding searches are deleted as well.
  
  def __repr__(self):
    return '<Users model {}>'.format(self.id)

class Searches(DeclarativeBase, Base):
  __tablename__ = "searches"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey(Users.id))
  # user = relationship("Users", backref='searches')
  keywords = Column('keywords', String)
  location = Column('location', String)
  generated_calendar = Column('generated_calendar', Boolean)

  def __repr__(self):
    return '<Searches model {}>'.format(self.id)