from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, marshal
from server.app import api, app
from server.logic.cal import generateCalendarDeadlines, createCalendar

job_model = api.model('Job_Model', {
  'title': fields.String,
  'link': fields.String,
  'summary': fields.String,
  'chosen_date': fields.DateTime,
  'location': fields.String
})

@api.route('/jobs/calendar')
class CalendarJobs(Resource):
  
  @api.expect([job_model], validate=True)
  @api.doc(description="Generate ics file from jobs. This assumes the front-end would have processed all the jobs by user preferences for file generation.")
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(200, 'Data sucessfully processed and ics file generated.')
  def post(self):
    jobs_args = request.get_json()
    # MAYBE: If we populate db with searched jobs, no need to have bloated payload, can just take list of job ids for db reference?
    
    jobs = jobs_args['Jobs']
    try:
      calendar = generateCalendarDeadlines(jobs)
    except:
      return {'message': 'Error generating calendar from jobs.'}, 400
    
    try:
      calendarFile = createCalendar(calendar)
    except:
      return {'message': 'Error creating calendar file.'}, 400
    
    return send_file(calendarFile, attachment_filename='myJobDeadlines.ics'), 200