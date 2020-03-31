from server import db_session

class Base(object):
  
  @classmethod
  def create(cls, **kw):
    obj = cls(**kw)
    session = db_session()
    session.add(obj)
    session.commit()
    
  @classmethod
  def remove(cls, **kw):
    obj = cls(**kw)
    session = db_session()
    session.delete(obj)
    session.commit()