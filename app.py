"""
    The configuration for the top-level object that represents the Web server.
"""

from flask import Flask
import flask_restless as restless

from domain.base import engine, Base, Session
from domain.events import RentalEvent
from domain.payment_methods import CreditCard
from domain.rentables import (Rentable, LiveActionSeries, AnimatedSeries, DocumentarySeries,
                              StandUpComedySpecial, LiveActionMovie, AnimatedMovie, MusicalShow,
                              Documentary, VideoGame, SportsEvent)
from domain.users import Client, Employee
from endpoints import home


# --- Database setup
Base.metadata.create_all(engine)
db_session = Session()

app = Flask('video-rental-manager')
api_manager = restless.APIManager(app, session=db_session)

# --- Routes
app.add_url_rule('/', 'home', home)

api_manager.create_api(Client, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(Employee, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(RentalEvent, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(CreditCard, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(Rentable, methods=['GET'])
api_manager.create_api(LiveActionSeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(AnimatedSeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(DocumentarySeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(StandUpComedySpecial, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(LiveActionMovie, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(AnimatedMovie, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(MusicalShow, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(Documentary, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(VideoGame, methods=['GET', 'POST', 'PUT', 'DELETE'])
api_manager.create_api(SportsEvent, methods=['GET', 'POST', 'PUT', 'DELETE'])
