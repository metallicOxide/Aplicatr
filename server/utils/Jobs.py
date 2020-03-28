
from typing import List, Dict, Text
from server.utils.SupportedPortals import SupportedPortals

class Job:
  '''
  Representation of a job's key information.
  '''
  
  def __init__(self, title, link, summary, closing_date, location):
    self.title = title
    self.link = link
    self.summary = summary
    self.closing_date = closing_date
    self.location = location
  
  def serialize(self):
    return {
      'title': self.title,
      'link': self.link,
      'summary': self.summary,
      'closing_date': self.closing_date,
      'location': self.location
    }
    
class JobsList:
  '''
  Holds a list of jobs, and contains useful methods for processing.
  '''
  
  # def __init__(self, uni: Text, keywords: Text, location: Text):
  def __init__(self):
    self.jobs = []
    # self.keywords = keywords
    # self.location = location
  
  def addJob(self, job: Job):
    if not isinstance(job, Job): 
      raise TypeError
    self.jobs.append(job)
  
  def serialize(self) -> (List[Dict]):
    return [job.serialize() for job in self.jobs]
  
  def getJobs(self) -> (List[Job]):
    return self.jobs