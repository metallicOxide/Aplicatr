from ics import Calendar, Event
from typing import List, Dict, Any, IO
from datetime import datetime, timedelta

from server.utils.Jobs import JobsList, Job

def generateCalendarDeadlines(jobs: JobsList) -> (Calendar):
  applicationDeadlines = Calendar()
  for job in jobs.getJobs():
    e = Event(name=job.title, 
              description=job.summary, 
              location=job.location, 
              url=job.link,
              begin=job.closing_date)
    applicationDeadlines.events.add(e)
  return applicationDeadlines

def createCalendar(myCalendar: Calendar) -> (IO):
  with open('myApplicationDeadlines.ics', 'w') as calendarFile:
    calendarFile.writelines(myCalendar)
    return calendarFile