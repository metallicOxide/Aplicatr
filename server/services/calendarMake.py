from ics import Calendar, Event
from typing import List, Dict, Any, IO
from datetime import datetime, timedelta
from requests_html import HTMLSession
from requests.sessions import RequestsCookieJar

from server.utils.Jobs import JobsList, Job
from server.services import SupportedPortals, UnswScraper

def generateCalendarSummarized(jobs: JobsList) -> (Calendar):
  applicationDeadlines = Calendar()
  for job in jobs.getJobs():
    #TODO: make events span as an all_day event
    e = Event(name=job.title, 
              description=job.company + "\n\n" + job.summary + "\n\nView listing on " + job.link, 
              location=job.location, 
              url=job.link,
              begin=job.reminder_date)
    applicationDeadlines.events.add(e)
  return applicationDeadlines