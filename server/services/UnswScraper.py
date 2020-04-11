from requests_html import HTMLSession
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Text
from abc import ABCMeta, abstractmethod
from datetime import datetime
from requests.sessions import RequestsCookieJar

from server.utils.ScraperSession import ScraperSession
from server.services import SupportedPortals
from server.utils.Jobs import JobsList, Job, JobDetail

class UnswScraper(ScraperSession):
  '''
  UNSW Careers Online scraping functions
  '''
  def __init__(self):
    ScraperSession.__init__(self)
    
  def login(self, username = '', password = ''):
    '''
    Login to uni career portal.
    
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
      'LDAPUsername': username, 
      'LDAPPassword': password,
      '__RequestVerificationToken': requestVerificationToken
    }
    
    setCookies = sesh.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
    if not setCookies.ok: 
      raise ValueError
    login = sesh.post('https://careersonline.unsw.edu.au/') # I don't know entirely what this second post request is for but kept it.
    if not login.ok: 
      raise ValueError
    
    return sesh

  def extractJobs(self, cookies: RequestsCookieJar = {}, keywords: Text = '', location: Text = '', username: Text = '') -> (JobsList):
    '''
    Extract job data from the uni career portal.
    
    :param sesh: A valid session that has already been authenticated with a valid username and password.
    :param keywords: Search for and filter relevant jobs by search keyword terms.
    :param jobType: Search for and filter relevant jobs by a job type.
    :param location: Search for and filter relevant jobs by location. 
    
    :returns: JobsList.  
    '''
    sesh = HTMLSession()
    jobBoard = sesh.get('https://careersonline.unsw.edu.au/students/jobs/Search?text={}&location={}&page=1&take=1000'.format(
      keywords, location
    ), cookies=cookies)
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
            title = listing.find('a').get_text().replace('\r\n', '').strip(),
            company = listing.find('h5').get_text().replace('\r\n', '').strip(),
            link = "https://careersonline.unsw.edu.au{}".format(listing.find('a')['href']),
            summary = listing.find('p', {'class': 'job-list-summary'}).get_text(strip=True),
            closing_date = str(closingDate),
            location = listing.find('div', {'class': 'job-list-location'}).get_text(strip=True)
          ))
    except:
      raise KeyError
    
    return jobs
  
  def extractJobDetails(self, cookies: RequestsCookieJar = {}, link: Text = '') -> (JobDetail):
    '''
    Extract details of a job listing from the uni career portal.
    '''
    sesh = HTMLSession()
    if '/students/jobs/detail/' not in link:
      raise ValueError
    
    jobDetail = sesh.get(link, cookies=cookies)
    if not jobDetail.ok:
      raise ConnectionError
    
    try:
      jobDetailSoup = BeautifulSoup(jobDetail.content, features='html.parser')
      procedureSoup = jobDetailSoup.find('div', {'id': 'procedures'})
      procedure = procedureSoup.get_text().replace('Application Procedures', '').replace('\r', '').replace('\t', '').strip() + '\n[' + procedureSoup.find('a')['href'] + ']'
    except:
      procedure = ''
    
    try:
      description = jobDetailSoup.find('div', {'class': 'job-details'}).get_text().strip()
    except:
      description = ''
    
    return JobDetail(description=description, procedure=procedure)
    
