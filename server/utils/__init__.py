import getpass
from server.services.UnswScraper import UnswScraper
from server.services.calendarMake import generateCalendarDeadlines, createCalendar
from pprint import pprint
from server.utils.Jobs import JobsList, Job
from typing import List, Dict
from server.utils.SupportedPortals import SupportedPortals

def logicScript():
  '''
  Runs business logic script from command line
  '''
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


def convertJobsFromListDicts(jobs: List[Dict]) -> (JobsList):
  '''
  Helper function for converting post body data from list of dicts form to our 
  JobsList class.
  '''
  try:
    res = JobsList()
    for job in jobs:
      res.addJob(Job(title = job['title'], 
                link = job['link'], 
                summary = job['summary'], 
                closing_date = job['closing_date'], 
                location = job['location']))
  except:
    raise KeyError
  return res  