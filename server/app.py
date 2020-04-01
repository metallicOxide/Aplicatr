from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, reqparse
import sys
import os
import jwt
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
  '''  
  There is inconsistency in the root directory when running from repository root
  or within server. Append repository root when run from within server to get all 
  imports working.
  '''
  sys.path.insert(0, './..')
  
from server.models import engine
from server.utils import logicScript

if __name__ == '__main__':
  '''
  Run script to generate a calendar file based on input search terms.
  '''
  logicScript()


''' Server global variables '''

db_session = sessionmaker(bind=engine) # to be used for any database session

app = Flask(__name__)
api = Api(app).namespace('', description='Uni Job Scraper APIs')
  
token_parser = reqparse.RequestParser().add_argument('token', type = str, required = True)
