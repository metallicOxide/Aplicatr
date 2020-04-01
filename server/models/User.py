from sqlalchemy import Column, String, Integer, LargeBinary
from server.models import DeclarativeBase
from server.models.Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

class User(Base, DeclarativeBase):
  __tablename__ = "user"
  __table_args__ = (
    UniqueConstraint('username'),
  )
  username = Column('username', String)
  uni = Column('uni', String)
  last_session_cookie_jar = Column('last_session_cookie_jar', LargeBinary) # for the uni job portal cookie, not our app jwt token. requestcookiejar stored in pickled form
  searches = relationship("Search", back_populates='user', cascade="all,delete") # if user gets deleted, all the corresponding searches are deleted as well.
  
  def __repr__(self):
    return '<Users model {}>'.format(self.id)
  