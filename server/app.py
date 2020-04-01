from flask import Flask
from flask_restx import Api, reqparse
import sys
import os

if __name__ == '__main__':
  '''  
  There is inconsistency in the root directory when running from repository root
  or within server. Append repository root when run from within server to get all 
  imports working.
  '''
  sys.path.insert(0, './..')

from server.utils import logicScript

if __name__ == '__main__':
  '''
  Run script to generate a calendar file based on input search terms.
  '''
  logicScript()


app = Flask(__name__)
api = Api(app).namespace('', description='Uni Job Scraper APIs')

token_parser = reqparse.RequestParser().add_argument('token', type = str, required = True)

from server.routes import calendarRoute,loginRoute,scrapeRoute
