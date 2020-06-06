from requests_html import HTMLSession
from abc import ABCMeta, abstractmethod
from requests.sessions import RequestsCookieJar
from typing import List, Dict, Any, Text
from server.utils.Jobs import JobsList, Job, JobDetail

class ScraperSession(metaclass=ABCMeta):
  '''
  Abstract class for supported online scraping functionalities
  '''
  def __init__(self):
    # add any shared attributes here.
    pass
    
  @abstractmethod
  def login(self, username: Text = '', password: Text = '') -> (HTMLSession):
    '''
    Login to uni career portal.
    
    :param username: A valid portal username.
    :param password: A corresponding valid password.
    
    :returns: A valid persistent session to access the portal past the authentication screen.  
    '''
    pass
  
  @abstractmethod
  def extractJobs(self, cookies: RequestsCookieJar = {}, keywords: Text = '', username: Text = '') -> (JobsList):
    '''
    Extract job data from the uni career portal.
    
    :param cookies: A valid session that has already been authenticated with a valid username and password.
    :param keywords: Search for and filter relevant jobs by search keyword terms.
    :param jobType: Search for and filter relevant jobs by a job type.
    
    :returns: JobsList.  
    '''
    pass
  
  @abstractmethod
  def extractJobDetails(self, cookies: RequestsCookieJar = {}, link: Text = '') -> (JobDetail):
    '''
    Extract details of a job listing from the uni career portal.
    
    :param cookies: A valid session that has already been authenticated with a valid username and password.
    :param link: URL path of the description page of the particular job
    '''
  