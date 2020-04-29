
from typing import List, Dict, Text
from server.services import SupportedPortals

class JobDetail:
  '''
  Representation of a job's details.
  '''
  def __init__(self, description, procedure):
    self.description = description
    self.procedure = procedure
  
  def serialize(self):
    return {
      'description': self.description,
      'procedure': self.procedure
    }
  
class Job:
  '''
  Representation of a job's key information.
  '''
  
  def __init__(self, company, title, link, summary, reminder_date, location):
    self.title = title
    self.company = company
    self.link = link
    self.summary = summary
    self.reminder_date = reminder_date
    self.location = location
  
  def serialize(self):
    return {
      'title': self.title,
      'company': self.company,
      'link': self.link,
      'summary': self.summary,
      'reminder_date': self.reminder_date,
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