from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields
from server.app import api, app
from server.services.UnswScraper import UnswScraper
from server.utils.SupportedPortals import SupportedPortals

search_model = api.model('Search_Model', {
  'Username': fields.String,
  'Password': fields.String,
  'Uni': fields.String,
  'Keywords': fields.String,
  'Location': fields.String,
}, required=True)

@api.route('/jobs')
class SearchJobs(Resource):
  @api.expect(search_model, validate=True)
  @api.doc(description='Extract job data using login credentials and search parameters.')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
  def post(self):
    search = request.get_json()
    username, password, uni, keywords, location = search.values()
    if uni not in [portal.name for portal in SupportedPortals]:
      return {'message': 'Error, functionalities for {} not supported.'.format(uni)}, 400
    
    if uni == SupportedPortals.UNSW.name:
      portal = UnswScraper(username = username, password = password)
      login = portal.login
      extractData = portal.extractData
      
    try:
      sesh = login()
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except ValueError:
      return {'message': 'Invalid username or password.'}, 400
    except:
      return {'message': 'Error logging in.'}, 400

    try:
      jobs = extractData(keywords = keywords, location = location)
    except ValueError:
      return {'message': 'Invalid inputs.'}, 400
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except KeyError:
      return {'message': 'Error processing extracted data.'}, 400
    except:
      return {'message': 'Error extracting data'}, 400
        
    return {'jobs': jobs.serialize()}, 200