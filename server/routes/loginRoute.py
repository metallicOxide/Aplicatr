import jwt
import pickle

from flask import Flask, request, send_file, request
from flask_restx import Resource, Api, fields, reqparse
from datetime import datetime, timedelta

from server.app import api, app
from server.services.UnswScraper import UnswScraper
from server.utils.SupportedPortals import SupportedPortals
from server.config import scraper_token_key

from server.models import db_session
from server.models.User import User

login_model = api.model('Login_Model', {
  'Username': fields.String,
  'Password': fields.String,
  'Uni': fields.String,
}, required=True)

@api.route('/jobs/login')
class LoginRoute(Resource):
  @api.expect(login_model, validate=True)
  @api.doc(description='''
    Attempts to log into to portal with provided credentials. If successful, 
    then we upsert the user info (not password), and portal cookie into database. 
    We then return a jwt token to maintain user session on our application.
    ''')
  def post(self):
    login = request.get_json()
    username, password, uni = login.values()
    
    if uni not in [portal.name for portal in SupportedPortals]:
      return {'message': "Error, functionalities for '{}' portal not supported.".format(uni)}, 400
    
    if uni == SupportedPortals.UNSW.name:
      portal = UnswScraper()
      login = portal.login

    try:
      sesh = login(username = username, password = password)
    except ConnectionError:
      return {'message': 'Error connecting to data source.'}, 404
    except ValueError:
      return {'message': 'Invalid username or password.'}, 400
    except:
      return {'message': 'Error logging in.'}, 400
    
    # TODO: sort out proper way to catch db errors, a general try catch will still crash server if error in db
    try:
      session = db_session()
      user_lookup = session.query(User).filter_by(username = username)
      if user_lookup.one_or_none() == None:
        session.add(User(username = username, 
                        last_session_cookie_jar = pickle.dumps(sesh.cookies), 
                        uni = uni))
      else:
        session.query(User).filter_by(username = username).update({User.last_session_cookie_jar: pickle.dumps(sesh.cookies)})
      session.commit()
    except:
      return {'message': 'Error with database.'}, 400
    
    return {
      'token': jwt.encode({
        'username': username, 
        'exp': datetime.now() + timedelta(minutes=20)
      }, key=scraper_token_key, algorithm='HS256').decode('utf-8'), 
    }, 200