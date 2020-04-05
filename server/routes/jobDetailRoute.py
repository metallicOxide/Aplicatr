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

job_detail_model = api.model('Job_Detail_Model', {
  'link': fields.String,
}, required=True)

@api.route('/jobs/detail')
class JobDetail(Resource):
  @api.expect(token_parser, job_detail_model, validate=True)
  @api.doc(description='''
    Scrape portal for extra details of a particular job listing using the link
    provided by user in the request payload. 
    ''')
  @api.response(400, 'Invalid input or error processing data encountered.')
  @api.response(404, 'Error connecting to data source.')
  @api.response(200, 'Data sucessfully processed and returned.')
  def post(self):
    link = request.get_json().get('link')
    token = token_parser.parse_args().get('token')

    try:
      user, portal, cookies = authentication(token)
    except jwt.ExpiredSignatureError:
      return {'message': 'Expired token.'}, 400
    except (jwt.InvalidTokenError, jwt.DecodeError, jwt.InvalidSignatureError):
      return {'message': 'Invalid token.'}, 400
    except:
      return {'message': 'Error fetching data from database.'}, 400

    # try:
    detail = portal.extractJobDetails(portal, cookies=cookies, link=link)
    # except ValueError:
    #   return {'message': 'Invalid link.'}, 400
    # except ConnectionError:
    #   return {'message': 'Error connecting to data source.'}, 404
    # except KeyError:
    #   return {'message': 'Error processing extracted data.'}, 400
    # except:
    #   return {'message': 'Error extracting data'}, 400
    
    return {'detail': detail.serialize()}, 200