from os import environ

scraper_token_key = environ['TOKEN_SECRET'] if 'TOKEN_SECRET' in environ.keys() else 'hihihihiheyeh&yesadiusadpw21321'

DATABASE = {
  'drivername': 'postgres+psycopg2',
  'host': environ['DB_HOST'] if 'DB_HOST' in environ.keys() else 'localhost',
  'port': environ['DB_PORT'] if 'DB_PORT' in environ.keys() else '5432',
  'username': environ['DB_USERNAME'] if 'DB_USERNAME' in environ.keys() else 'aplicatr',
  'password': environ['DB_PASSWORD'] if 'DB_PASSWORD' in environ.keys() else 'aplicatr',
  'database': environ['DB'] if 'DB' in environ.keys() else 'aplicatr'
}