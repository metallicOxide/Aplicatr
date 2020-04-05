from requests_html import HTMLSession
from abc import ABCMeta, abstractmethod
from requests.sessions import RequestsCookieJar
from typing import List, Dict, Any, Text
from server.utils.Jobs import JobsList, Job

class ScraperSession(metaclass=ABCMeta):
  '''
  Abstract class for supported online scraping functionalities
  '''
  # def __init__(self, username, password):
  #   self.username = username
  #   self.password = password
  #   self.session = None
    
  @abstractmethod
  def login(self, username: Text = '', password: Text = '') -> (HTMLSession):
    '''
    Abstract method for logging into the online data source.
    
    If successful, self.session must be assigned the HTMLSession value.
    
    :returns: a valid HTMLSession if successful.
    '''
    pass
  
  @abstractmethod
  def extractJobs(self, cookies: RequestsCookieJar = {}, keywords: Text = '', location: Text = '', username: Text = '') -> (JobsList):
    '''
    Abstract method for extracting data from the online data source.
    
    The attribute self.session must be assigned to a valid HTMLSession value.
    
    :returns: JobsList
    '''
    pass
  
  @abstractmethod
  def extractJobDetails(self, cookies: RequestsCookieJar = {}, link: Text = ''):
    '''
    Abstract method for extracting details of a particular job listing from the online data source.
    '''
  