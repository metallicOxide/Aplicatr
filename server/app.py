from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
from server.logic.unswScraper import extractData, login, JobTypes
from server.logic.cal import generateCalendarDeadlines, createCalendar

import os
import getpass

app = Flask(__name__)
api = Api(app).namespace('', description='Uni Job Scraper APIs')


from server.routes import searchJobs, calendarJobs

if __name__ == '__main__':
  print("Running job webscraper...")
  username = input("Username: ")
  password = getpass.getpass(prompt='Password: ')
  sesh = login(username=username, 
                password=password)
  keywords = input('Enter search keywords: ')
  print('Possible job types: [' + ', '.join(JobTypes.keys()) + ']')
  jobType = input('Enter job type: ')
  location = input('Enter location: ')
  jobs = extractData(sesh, keywords=keywords, jobType=jobType, location=location)
  myCalendar = generateCalendarDeadlines(jobs)
  createCalendar(myCalendar)
