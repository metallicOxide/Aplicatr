from bs4 import BeautifulSoup
import os
from requests_html import HTMLSession
import sys
from typing import List, Dict, Any, Text
from pprint import pprint
from datetime import datetime

JobTypes = {
  'any': -1,
  "part-time-casual-employment": 1138,
  "vacation-employment-internships": 1139,
  "full-time-entry-level": 1140,
  "structured-graduate-program": 1164,
  "experienced-professional-employment": 1141,
  "full-time": 1142,
  "contract": 1143,
  "volunteering": 1144,
  "overseas-employment": 1145,
  "international-students": 1146,
  "on-Campus-employment": 1147,
  "postgraduates": 1148,
  "scholarships-cadetships": 1149,
  "disability-program": 1175,
  "indigenous-program": 1176,
  "equal-opportunity-program": 1177
}

def login(username: Text = '', password: Text = '') -> (HTMLSession):
  print("Creating session...")
  sesh = HTMLSession()

  print("Extracting login page tokens...")
  loginPage = sesh.get('https://careersonline.unsw.edu.au/students/login')
  if not loginPage.ok:
    print('Error getting onto careersonline...')
    raise ConnectionError
  
  soup = BeautifulSoup(loginPage.content, "html.parser")
  requestVerificationToken = soup.find("input", {'name': '__RequestVerificationToken'}).get('value')
  loginPayload = {
    'LDAPUsername': username, 
    'LDAPPassword': password,
    '__RequestVerificationToken': requestVerificationToken
  }
  
  print("Logging in to the UNSW careers online portal...")
  setCookies = sesh.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
  if not setCookies.ok: 
    print("Error setting cookies, exiting...")
    raise ValueError
  
  login = sesh.post('https://careersonline.unsw.edu.au/') # I don't know entirely what this second post request is for but kept it.
  if not login.ok: 
    print("Error logging in, exiting...")
    raise ValueError
  print("Logged into UNSW careers online portal!")
  
  return sesh

def extractData(sesh: HTMLSession, keywords: Text = '', jobType: Text = 'any', location: Text = '') -> (List[Dict]):
  if jobType not in JobTypes.keys(): 
    raise ValueError
  
  print("Extracting all job listings...")
  jobBoard = sesh.get('https://careersonline.unsw.edu.au/students/jobs/Search?text={}&typeofwork={}&location={}&page=1&take=1000'.format(
    keywords, JobTypes[jobType], location
  ))
  if not jobBoard.ok:
    print("Error retrieving data...")
    raise ConnectionError
  
  months = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
  }
  jobSoup = BeautifulSoup(jobBoard.content, features='html.parser')
  try:
      jobs = []
      for listing in jobSoup.find_all("div", {"class": 'list-group-item'}):
          closingDateText = listing.find('div', {'class': 'job-list-close'}).get_text(strip=True).replace('Closes- ', '')
          day, monthWord, year = closingDateText.split(' ')
          closingDate = datetime(int(year), months[monthWord], int(day), hour=12)
          jobs.append({
            'title': listing.find('a').get_text().replace('\\r\\n', '').strip(),
            'link': listing.find('a')['href'],
            'summary': listing.find('p', {'class': 'job-list-summary'}).get_text(strip=True),
            'closing_date': closingDate,
            'location': listing.find('div', {'class': 'job-list-location'}).get_text(strip=True)
          })
  except:
    print("Error extracting data, website may have changed...")
    raise KeyError
  pprint(jobs)
  
  return jobs

