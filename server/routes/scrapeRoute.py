import jwt
import pickle

from flask import Flask, request, send_file, request
from flask_restx import Resource, Api, fields, reqparse

from server.app import api, app, token_parser
from server.config import scraper_token_key
from server.services.UnswScraper import UnswScraper
from server.models import db_session
from server.models.User import User
from server.models.Search import Search
from server.utils import authentication
from server.services import SupportedPortals

search_model = api.model('Search_Model', {
  'keywords': fields.String,
  'location': fields.String,
}, required=True)

@api.route('/jobs')
class ScrapeRoute(Resource):
  @api.expect(token_parser, search_model, validate=True)
  @api.doc(description='''
    Scrape portal for job listings using provided search terms and a cookie 
    previously stored in the db. Search terms will then be stored in the db 
    then return the resulting list of jobs.
    ''')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
  def post(self):
    search = request.get_json()
    keywords, location = search.values()
    
    args = token_parser.parse_args()
    token = args.get('token')

    try:
      user, portal, cookies = authentication(token)
    except jwt.ExpiredSignatureError:
      return {'message': 'Expired token.'}, 400
    except (jwt.InvalidTokenError, jwt.DecodeError, jwt.InvalidSignatureError):
      return {'message': 'Invalid token.'}, 400
    except:
      return {'message': 'Error fetching data from database.'}, 400

    try:
      jobs = portal.extractJobs(portal, 
                                cookies = cookies, 
                                keywords = keywords, 
                                username = user.username)
    except ValueError:
      return {'message': 'Invalid inputs.'}, 400
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except KeyError:
      return {'message': 'Error processing extracted data.'}, 400
    except:
      return {'message': 'Error extracting data'}, 400
    
    session = db_session()
    session.add(Search(user_id = user.id, keywords = keywords, location = location))
    session.commit()
    return {'jobs': jobs.serialize()}, 200