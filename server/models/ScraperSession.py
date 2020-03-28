from requests_html import HTMLSession
from server.services.Jobs import Job, JobsList
from abc import ABCMeta, abstractmethod

class ScraperSession(metaclass=ABCMeta):
  '''
  Abstract class for supported online scraping functionalities
  '''
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.session = None
    
  @abstractmethod
  def login(self) -> (HTMLSession):
    '''
    Abstract method for logging into the online data source.
    
    If successful, self.session must be assigned the HTMLSession value.
    
    :returns: a valid HTMLSession if successful.
    '''
    pass
  
  @abstractmethod
  def extractData(self) -> (JobsList):
    '''
    Abstract method for extracting data from the online data source.
    
    The attribute self.session must be assigned to a valid HTMLSession value.
    
    :returns: JobsList
    '''
    pass