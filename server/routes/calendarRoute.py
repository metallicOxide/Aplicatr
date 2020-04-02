import jwt
import json

from flask import Flask, send_file, request
from flask_restx import Resource, Api, fields

from server.app import api, app, token_parser
from server.services.calendarMake import generateCalendarDeadlines, createCalendar
from server.utils import convertJobsFromListDicts, authentication
from server.utils.SupportedPortals import SupportedPortals

jobs_model = api.model('Jobs_Model', {
  'jobs': fields.List(fields.Raw(
    description='''
      title: string,
      link: string,
      summary: string.
      chosen_date: string (datetime),
      location: string
    '''))
}, required=True)

@api.route('/jobs/calendar')
class CalendarRoute(Resource):
  @api.expect(token_parser, jobs_model, validate=True)
  @api.doc(description='''
    Generates a calendar file from given list of jobs after processing, then
    sends back an ics file.
    ''')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(200, 'Data sucessfully processed and ics file generated.')
  def post(self):
    args = token_parser.parse_args()
    token = args.get('token')
    try:
      username, portal, cookies = authentication(token)
    except jwt.ExpiredSignatureError:
      return {'message': 'Expired token.'}, 400
    except (jwt.InvalidTokenError, jwt.DecodeError, jwt.InvalidSignatureError):
      return {'message': 'Invalid token.'}, 400
    except:
      return {'message': 'Error fetching data from database.'}, 400
    
    body = request.get_json()
    jobs = body.get('jobs')
    try:
      processedJobs = convertJobsFromListDicts(jobs)
      calendar = generateCalendarDeadlines(processedJobs)
    except:
      return {'message': 'Error generating calendar from jobs.'}, 400
    
    try:
      calendarFile = createCalendar(calendar)
    except:
      return {'message': 'Error creating calendar file.'}, 400
        
    return send_file(calendarFile, attachment_filename='myJobDeadlines.ics'), 200