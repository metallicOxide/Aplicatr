from sqlalchemy import Column, String, Integer
from server.models import DeclarativeBase
from server.models.Base import Base
from sqlalchemy.orm import relationship

class Users(DeclarativeBase, Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  username = Column('username', String)
  uni = Column('uni', String)
  last_session = Column('last_session', String) # for the uni job portal cookie, not our app jwt token.
  searches = relationship("Searches", back_populates = 'users', cascade="all,delete") # if user gets deleted, all the corresponding searches are deleted as well.
  
  def __repr__(self):
    return '<Users model {}>'.format(self.id)
  