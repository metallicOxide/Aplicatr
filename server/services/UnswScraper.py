from requests_html import HTMLSession
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Text
from abc import ABCMeta, abstractmethod
from server.models.ScraperSession import ScraperSession
from server.utils.Jobs import JobsList, Job
from server.utils.SupportedPortals import SupportedPortals
from datetime import datetime

class UnswScraper(ScraperSession):
  '''
  UNSW Careers Online scraping functions
  '''
  def __init__(self, username, password):
    ScraperSession.__init__(self, username, password)
    
  def login(self):
    '''
    Login to uni career portal and sets session property if successful.
    
    :param username: A valid portal username.
    :param password: A corresponding valid password.
    
    :returns: A valid persistent session to access the portal past the authentication screen.  
    '''
    
    sesh = HTMLSession()
    loginPage = sesh.get('https://careersonline.unsw.edu.au/students/login')
    if not loginPage.ok:
      raise ConnectionError
    
    soup = BeautifulSoup(loginPage.content, "html.parser")
    requestVerificationToken = soup.find("input", {'name': '__RequestVerificationToken'}).get('value')
    loginPayload = {
      'LDAPUsername': self.username, 
      'LDAPPassword': self.password,
      '__RequestVerificationToken': requestVerificationToken
    }
    
    setCookies = sesh.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
    if not setCookies.ok: 
      raise ValueError
    login = sesh.post('https://careersonline.unsw.edu.au/') # I don't know entirely what this second post request is for but kept it.
    if not login.ok: 
      raise ValueError
    
    self.session = sesh
    return sesh

  def extractData(self, keywords: Text = '', location: Text = '') -> (JobsList):
    '''
    Extract job data from the uni career portal.
    
    :param sesh: A valid session that has already been authenticated with a valid username and password.
    :param keywords: Search for and filter relevant jobs by search keyword terms.
    :param jobType: Search for and filter relevant jobs by a job type.
    :param location: Search for and filter relevant jobs by location. 
    
    :returns: JobsList.  
    '''
    if not isinstance(self.session, HTMLSession):
      raise AttributeError
    jobBoard = self.session.get('https://careersonline.unsw.edu.au/students/jobs/Search?text={}&location={}&page=1&take=1000'.format(
      keywords, location
    ))
    if not jobBoard.ok:
      raise ConnectionError
    
    months = {
      'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    jobSoup = BeautifulSoup(jobBoard.content, features='html.parser')
    try:
      jobs = JobsList()
      for listing in jobSoup.find_all("div", {"class": 'list-group-item'}):
          closingDateText = listing.find('div', {'class': 'job-list-close'}).get_text(strip=True).replace('Closes- ', '')
          day, monthWord, year = closingDateText.split(' ')
          closingDate = datetime(int(year), months[monthWord], int(day), hour=12)
          jobs.addJob(job = Job(
            title = listing.find('a').get_text().replace('\\r\\n', '').strip(),
            link = listing.find('a')['href'],
            summary = listing.find('p', {'class': 'job-list-summary'}).get_text(strip=True),
            closing_date = str(closingDate),
            location = listing.find('div', {'class': 'job-list-location'}).get_text(strip=True)
          ))
    except:
      raise KeyError
    
    return jobs