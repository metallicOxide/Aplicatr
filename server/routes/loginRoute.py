from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, reqparse
from server.app import api, app
import jwt
from server.services.UnswScraper import UnswScraper
from server.utils.SupportedPortals import SupportedPortals
from server.config import scraper_token_key
from datetime import datetime, timedelta

authentication_model = api.model('Search_Model', {
  'Username': fields.String,
  'Password': fields.String,
  'Uni': fields.String,
}, required=True)

@api.route('/jobs/login')
class LoginRoute(Resource):
  @api.expect(authentication_model, validate=True)
  @api.doc(description='Provide a valid username and password for a supported online job portal.')
  def post(self):
    authentication = request.get_json()
    username, password, uni = authentication.values()
    
    if uni not in [portal.name for portal in SupportedPortals]:
      return {'message': 'Error, functionalities for {} not supported.'.format(uni)}, 400
    
    if uni == SupportedPortals.UNSW.name:
      portal = UnswScraper(username = username, password = password)
      login = portal.login

    try:
      sesh = login()
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except ValueError:
      return {'message': 'Invalid username or password.'}, 400
    except:
      return {'message': 'Error logging in.'}, 400
    
    #### make db entry with username, store sesh.cookies in database, uni
    
    payload = jwt.encode({
      'username': username, 
      'exp': datetime.now() + timedelta(minutes=45)
    }, key=scraper_token_key, algorithm='HS256')
    
    return {
      'token': payload, 
    }, 200