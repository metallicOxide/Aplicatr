from server.utils.ScraperSession import ScraperSession
from server.utils.Jobs import JobsList, Job, JobDetail
from requests.sessions import RequestsCookieJar
from typing import List, Dict, Any, Text

class WsuScraper(ScraperSession):
  '''
  WSU Careers Online scraping functions
  '''
  def __init__(self):
    raise NotImplementedError # Remove when done
    ScraperSession.__init__(self)
  
  def login(self, username = '', password = ''):
    raise NotImplementedError
  
  def extractJobs(self, cookies: RequestsCookieJar = {}, keywords: Text = '', location: Text = '', username: Text = '') -> (JobsList):
    raise NotImplementedError
  
  def extractJobDetails(self, cookies: RequestsCookieJar = {}, link: Text = '') -> (JobDetail):
    raise NotImplementedError
