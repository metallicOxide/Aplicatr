from server.utils.Jobs import JobsList, Job
from typing import List, Dict
from server.utils.SupportedPortals import SupportedPortals

def convertJobsFromListDicts(jobs: List[Dict]) -> (JobsList):
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