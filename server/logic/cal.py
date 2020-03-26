from ics import Calendar, Event
from typing import List, Dict, Any, IO
from datetime import datetime, timedelta

def generateCalendarDeadlines(jobs: List[Dict]) -> (Calendar):
  applicationDeadlines = Calendar()
  print('Generating calendar...')
  for job in jobs:
    e = Event(name=job['title'], 
              description=job['summary'], 
              location=job['location'], 
              url=job['link'],
              begin=job['closing_date'])
    applicationDeadlines.events.add(e)
  return applicationDeadlines

def createCalendar(myCalendar: Calendar) -> (IO):
  print('Creating calendar...')
  with open('myApplicationDeadlines.ics', 'w') as calendarFile:
    calendarFile.writelines(myCalendar)
    print('Job application deadlines calendar successfully created!')
    return calendarFile