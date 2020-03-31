from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, reqparse
from server.utils import logicScript
import sys
import os
import jwt

app = Flask(__name__)
api = Api(app).namespace('', description='Uni Job Scraper APIs')
  
token_parser = reqparse.RequestParser().add_argument('token', type = str, required = True)

if __name__ == '__main__':
  sys.path.insert(0, './..')   # to get imports working properly when running app.py directly
  logicScript()
