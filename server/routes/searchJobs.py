from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
from server.app import api, app
from server.logic.unswScraper import extractData, login
from server.logic.unswJobTypes import JobTypes, getUnswJobTypes

search_model = api.model('Search_Model', {
  'Username': fields.String,
  'Password': fields.String,
  'Keywords': fields.String,
  'JobType': fields.String,
  'Location': fields.String,
}, required=True)

login_model = api.model('Login_Model', {
  'Username': fields.String,
  'Password': fields.String,
}, required=True)

@api.route('/jobs/login')
class UnswLogin(Resource):
  @api.expect(login_model, validate=True)
  @api.doc(description='Login UNSW website.')
  @api.response(200, 'login successfully.')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  def post(self):
    credentials = request.get_json()
    username, password = credentials.values()
    try:
      login(username, password)
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except ValueError:
      return {'message': 'Invalid username or password.'}, 400
    except:
      return {'message': 'Error logging in.'}, 400

    return {'data': True}, 200

@api.route('/jobs/types/unsw')
class UnswJobTypes(Resource):
  @api.doc(description='Get the available job types for UNSW.')
  @api.response(200, 'Data successfully returned.')
  def get(self):
    # TODO: Job types shouldn't be hardcoded, should fetch from website itself
    jobTypeList = getUnswJobTypes()
    return {'data' : jobTypeList} , 200

@api.route('/jobs')
class SearchJobs(Resource):
  
  @api.expect(search_model, validate=True)
  @api.doc(description='Extract job data using login credentials and search parameters.')

  def post(self):
    search = request.get_json()
    username, password, keywords, jobtype, location = search.values()
    try:
      sesh = login(username, password)
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except ValueError:
      return {'message': 'Invalid username or password.'}, 400
    except:
      return {'message': 'Error logging in.'}, 400

    try:
      jobs = extractData(sesh, keywords, jobtype, location)
    except ValueError:
      return {'message': 'Invalid jobtype. Choose from: [' + ', '.join(JobTypes.keys()) + ']'}, 400
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except KeyError:
      return {'message': 'Error processing extracted data.'}, 400
    except:
      return {'message': 'Error extracting data'}, 400
    
    # TODO: add database upload metadata like username, uni, etc
    # MAYBE: maybe populate db with requested jobs
    return {'data': jobs}, 200