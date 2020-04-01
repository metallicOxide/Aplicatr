import getpass
import jwt
import pickle
from pprint import pprint
from typing import List, Dict, Text

from server.config import scraper_token_key
from server.services.UnswScraper import UnswScraper
from server.services.calendarMake import generateCalendarDeadlines, createCalendar
from server.utils.Jobs import JobsList, Job
from server.utils.SupportedPortals import SupportedPortals
from server.models import db_session
from server.models.User import User

def authentication(token: Text) -> (Dict):
  '''
  Decodes token if valid or not, then does db look up on extracted username from
  token. 
  
  Note that the jwt token != portal cookie. Jwt token is for maintaining session
  on our web app and authenticate users that have already provided a valid 
  login credential to the requested portal. Portal cookie is for maintaining 
  session with the requested portal, so we don't need to always log them in 
  to the requested job portal site when needing to webscrape. 
  
  :returns: a tuple of (user, portal, cookies), where:
    * user is the db model User, 
    * portal is a subclass of PortalSessions, and 
    * cookies is a Cookie Jar.
  '''
  decoded = jwt.decode(token.encode(), key=scraper_token_key, algorithms='HS256')
  username = decoded.get('username')

  portal = None
  session = db_session()
  user_lookup = session.query(User).filter_by(username = username)
  user = user_lookup.one_or_none()
  if user == None:
    raise Exception
  else:
    if user.uni == SupportedPortals.UNSW.name:
      portal = UnswScraper
    # elif:
    # Add more supportedportals here
  cookies = pickle.loads(user.last_session_cookie_jar)
  
  return (user, portal, cookies)

def logicScript():
  '''
  Runs business logic script from command line
  '''
  print("Running job webscraper...")
  username = input("Username: ")
  password = getpass.getpass(prompt='Password: ')
  
  print('Logging in UNSW Careers Online...')
  portal = UnswScraper()
  sesh = portal.login(username = username, password = password)
  print('Successfully logged in UNSW Careers Online!')
  
  keywords = input('Enter search keywords: ')
  location = input('Enter location: ')
  print('Searching for jobs and extracting data...')
  jobs = portal.extractData(cookies=sesh.cookies, keywords=keywords, location=location, username=username)
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