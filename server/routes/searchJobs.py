from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
from server.app import api, app
from server.logic.unswScraper import extractData, login
from server.logic.unswJobTypes import JobTypes
from server.logic.unswJobTypeService import getAllUNSWJobTypes

search_model = api.model('Search_Model', {
  'Username': fields.String,
  'Password': fields.String,
  'Keywords': fields.String,
  'JobType': fields.String,
  'Location': fields.String,
}, required=True)

@api.route('/getJobTypes')
class GetAllUNSWJobTypes(Resource):
  @api.doc(description='Get the avaliable job types for UNSW.')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
  def get(self):
    jobTypeList = getAllUNSWJobTypes()
    return {'jobTypes' : jobTypeList} , 200

@api.route('/jobs')
class SearchJobs(Resource):
  
  @api.expect(search_model, validate=True)
  @api.doc(description='Extract job data using login credentials and search parameters.')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
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
    return {'jobs': jobs}, 200