from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
import sys
from pprint import pprint
import os
import getpass

if __name__ == '__main__':
  # to get imports working properly when running app.py directly
  sys.path.insert(0, './..')
  
from server.services.UnswScraper import UnswScraper
from server.services.calendarMake import generateCalendarDeadlines, createCalendar

app = Flask(__name__)
api = Api(app).namespace('', description='Uni Job Scraper APIs')

from server.routes import scrapeRoute, calendarRoute

if __name__ == '__main__':
  print("Running job webscraper...")
  username = input("Username: ")
  password = getpass.getpass(prompt='Password: ')
  
  print('Logging in UNSW Careers Online...')
  portal = UnswScraper(username = username, password = password)
  sesh = portal.login()
  print('Successfully logged in UNSW Careers Online!')
  
  keywords = input('Enter search keywords: ')
  location = input('Enter location: ')
  print('Searching for jobs and extracting data...')
  jobs = portal.extractData(keywords=keywords, location=location)
  pprint(jobs.serialize())
  
  print('Generating application deadline data...')
  myCalendar = generateCalendarDeadlines(jobs)
  print('Creating application deadline ics file...')
  createCalendar(myCalendar)
  print('Successfully created ics file!')
