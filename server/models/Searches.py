from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from server.models.Base import Base
from server.models import DeclarativeBase
from sqlalchemy.orm import relationship
from server import db_session

class Searches(DeclarativeBase, Base):
  __tablename__ = "searches"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("Users", back_populates = 'searches')
  keywords = Column('keywords', String)
  location = Column('location', String)
  generated_calendar = Column('generated_calendar', Boolean)

  def __repr__(self):
    return '<Searches model {}>'.format(self.id)