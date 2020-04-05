from ics import Calendar, Event
from typing import List, Dict, Any, IO
from datetime import datetime, timedelta
from requests_html import HTMLSession
from requests.sessions import RequestsCookieJar

from server.utils.Jobs import JobsList, Job
from server.services import SupportedPortals, UnswScraper

## TODO: explore generating more comprehensive calendar events descriptions, whether the extra info is worth the extra wait time.

# def generateCalendarDescriptive(jobs: JobsList, cookies: RequestsCookieJar, portal: SupportedPortals) -> (Calendar):
#   applicationDeadlines = Calendar()
#   for job in jobs.getJobs():
#     # this makes the generation process extra slow
#     detail = portal.extractJobDetail(cookies=cookies, link=job.link)
#     e = Event(name=job.title, 
#               description=detail.description + "\n\n" + detail.procedure + "\n\nView listing on {}".format(job.link),
#               location=job.location, 
#               url=job.link,
#               begin=job.closing_date)
#     applicationDeadlines.events.add(e)
#   return applicationDeadlines

def generateCalendarSummarized(jobs: JobsList) -> (Calendar):
  applicationDeadlines = Calendar()
  for job in jobs.getJobs():
    e = Event(name=job.title, 
              description=job.company + "\n\n" + job.summary + "\n\nView listing on " + job.link, 
              location=job.location, 
              url=job.link,
              begin=job.closing_date)
    applicationDeadlines.events.add(e)
  return applicationDeadlines