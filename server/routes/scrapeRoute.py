from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, reqparse
from server.app import api, app, token_parser
from server.services.UnswScraper import UnswScraper
from server.utils.SupportedPortals import SupportedPortals
import jwt
from server.config import scraper_token_key

search_model = api.model('Search_Model', {
  # 'Username': fields.String,
  # 'Password': fields.String,
  # 'Uni': fields.String,
  'Keywords': fields.String,
  'Location': fields.String,
}, required=True)

@api.route('/jobs')
class ScrapeRoute(Resource):
  @api.expect(token_parser, validate=True)
  @api.expect(search_model, validate=True)
  @api.doc(description='Extract job data using login credentials and search parameters.')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
  def post(self):
    args = token_parser.parse_args()
    token = args.get('token')
    try:
      decoded = jwt.decode(token, key=scraper_token_key, algorithms='HS256')
      username = decoded.get('username')
    except jwt.ExpiredSignatureError:
      return {'message': 'Expired token.'}, 400
    except:
      return {'message': 'Invalid token received.'}, 400
    
    ###### search db for matching username and retrieve cookie session for extracting job
    # cookie = retrieve from db
    
    search = request.get_json()
    keywords, location = search.values()

    try:
      jobs = extractData(cookie = cookie, keywords = keywords, location = location)
    except ValueError:
      return {'message': 'Invalid inputs.'}, 400
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except KeyError:
      return {'message': 'Error processing extracted data.'}, 400
    except:
      return {'message': 'Error extracting data'}, 400
    
    # search db by username, add information search term keywords and location
    return {'jobs': jobs.serialize()}, 200