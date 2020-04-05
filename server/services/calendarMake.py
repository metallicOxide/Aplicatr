from ics import Calendar, Event
from typing import List, Dict, Any, IO
from datetime import datetime, timedelta
from requests_html import HTMLSession
from requests.sessions import RequestsCookieJar

from server.utils.Jobs import JobsList, Job
from server.services import SupportedPortals, UnswScraper

def generateCalendarDeadlines(jobs: JobsList, cookies: RequestsCookieJar, portal: SupportedPortals) -> (Calendar):
  applicationDeadlines = Calendar()
  for job in jobs.getJobs():
    detail = portal.extractJobDetail(cookies=cookies, link=job.link)
    description = ''
    if portal == UnswScraper:
      description = detail.description + "\n\n" + detail.procedure + "\n\View listing on https://careersonline.unsw.edu.au{}".format(job.link)
    e = Event(name=job.title, 
              description=description,
              location=job.location, 
              url=job.link,
              begin=job.closing_date)
    applicationDeadlines.events.add(e)
  return applicationDeadlines