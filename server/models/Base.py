from sqlalchemy import Column, String, Integer, LargeBinary, DateTime
import datetime
class Base():
  '''
  Add any common attributes or methods for models
  '''
  id = Column(Integer, primary_key=True)
  created_date = Column(DateTime, default=datetime.datetime.utcnow)
