from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from server.models.Base import Base
from server.models import DeclarativeBase
from sqlalchemy.orm import relationship

class Search(Base, DeclarativeBase):
  __tablename__ = "search"
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship("User", back_populates='searches')
  keywords = Column('keywords', String)
  location = Column('location', String)

  def __repr__(self):
    return '<Searches model {}>'.format(self.id)