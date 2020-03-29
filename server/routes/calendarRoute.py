from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, marshal
from server.app import api, app
from server.services.calendarMake import generateCalendarDeadlines, createCalendar
from server.utils.helpers import convertJobsFromListDicts
from server.utils.SupportedPortals import SupportedPortals

job_model = api.model('Job_Model', {
  'title': fields.String,
  'link': fields.String,
  'summary': fields.String,
  'chosen_date': fields.DateTime,
  'location': fields.String
})

@api.route('/jobs/calendar')
class CalendarRoutes(Resource):
  @api.expect([job_model], validate=True)
  @api.doc(description="Generate ics file from jobs. This assumes the front-end would have processed all the jobs by user preferences for file generation.")
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(200, 'Data sucessfully processed and ics file generated.')
  def post(self):
    jobs = request.get_json()
    processedJobs = convertJobsFromListDicts(jobs)
    try:
      calendar = generateCalendarDeadlines(processedJobs)
    except:
      return {'message': 'Error generating calendar from jobs.'}, 400
    
    try:
      calendarFile = createCalendar(calendar)
    except:
      return {'message': 'Error creating calendar file.'}, 400
    
    # TODO: add database upload metadata like username, uni, etc
    
    return send_file(calendarFile, attachment_filename='myJobDeadlines.ics'), 200