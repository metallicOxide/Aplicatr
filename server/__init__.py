import server.models as models
from sqlalchemy.orm import sessionmaker

print('Setting up database...')
engine = models.dbConnect()
print('Creating tables...')
models.dbCreateTables(engine)

db_session = sessionmaker(bind=engine)
