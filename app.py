"""
    The configuration for the top-level object that represents the Web server.
"""

from flask import Flask, g
# import flask_restless as restless

from domain.base import engine, Base, Session
# from domain.events import RentalEvent
# from domain.payment_methods import CreditCard
# from domain.rentables import (Rentable, LiveActionSeries, AnimatedSeries, DocumentarySeries,
#                               StandUpComedySpecial, LiveActionMovie, AnimatedMovie, MusicalShow,
#                               Documentary, VideoGame, SportsEvent)
from domain.users import Client, Employee
from presentation.endpoints import *


# --- Database setup
Base.metadata.create_all(engine)
# db_session = Session()

app = Flask('video-rental-manager')
# api_manager = restless.APIManager(app, session=db_session)

# --- Routes
@app.before_request
def before_request():
    g.db_session = Session()

app.add_url_rule('/', 'home', home)

app.add_url_rule('/clients', 'client_list', client_list)
app.add_url_rule('/clients/<id>', 'client_details', client_details, methods=['GET'])
app.add_url_rule('/clients/<id>', 'client_delete', client_delete, methods=['DELETE'])

app.add_url_rule('/employees', 'employee_list', employee_list)
app.add_url_rule('/employees/<id>', 'employee_details', employee_details, methods=['GET'])
app.add_url_rule('/employees/<id>', 'employee_delete', employee_delete, methods=['DELETE'])

app.add_url_rule('/credit_cards', 'credit_card_list', credit_card_list)
app.add_url_rule('/credit_cards/<id>', 'credit_card_details', credit_card_details, methods=['GET'])
app.add_url_rule('/credit_cards/<id>', 'credit_card_delete', credit_card_delete, methods=['DELETE'])

app.add_url_rule('/rentals', 'rental_event_list', rental_event_list)
app.add_url_rule('/rentals/<id>', 'rental_event_details', rental_event_details, methods=['GET'])
app.add_url_rule('/rentals/<id>', 'rental_event_delete', rental_event_delete, methods=['DELETE'])

app.add_url_rule('/rentables', 'rentable_list', rentable_list)
app.add_url_rule('/rentables/<id>', 'rentable_delete', rentable_delete, methods=['DELETE'])

app.add_url_rule('/live_action_series', 'live_action_series_list', live_action_series_list)
app.add_url_rule('/live_action_series/<id>', 'live_action_series_details', live_action_series_details, methods=['GET'])

app.add_url_rule('/animated_series', 'animated_series_list', animated_series_list)
app.add_url_rule('/animated_series/<id>', 'animated_series_details', animated_series_details, methods=['GET'])

app.add_url_rule('/documentary_series', 'documentary_series_list', documentary_series_list)
app.add_url_rule('/documentary_series/<id>', 'documentary_series_details', documentary_series_details, methods=['GET'])

app.add_url_rule('/stand_up_comedy_specials', 'stand_up_comedy_special_list', stand_up_comedy_special_list)
app.add_url_rule('/stand_up_comedy_specials/<id>', 'stand_up_comedy_special_details', stand_up_comedy_special_details, methods=['GET'])

app.add_url_rule('/live_action_movies', 'live_action_movie_list', live_action_movie_list)
app.add_url_rule('/live_action_movies/<id>', 'live_action_movie_details', live_action_movie_details, methods=['GET'])

app.add_url_rule('/animated_movies', 'animated_movie_list', animated_movie_list)
app.add_url_rule('/animated_movies/<id>', 'animated_movie_details', animated_movie_details, methods=['GET'])

app.add_url_rule('/musical_shows', 'musical_show_list', musical_show_list)
app.add_url_rule('/musical_shows/<id>', 'musical_show_details', musical_show_details, methods=['GET'])

app.add_url_rule('/documentaries', 'documentary_list', documentary_list)
app.add_url_rule('/documentaries/<id>', 'documentary_details', documentary_details, methods=['GET'])

app.add_url_rule('/video_games', 'video_game_list', video_game_list)
app.add_url_rule('/video_games/<id>', 'video_game_details', video_game_details, methods=['GET'])

app.add_url_rule('/sports_events', 'sports_event_list', sports_event_list)
app.add_url_rule('/sports_events/<id>', 'sports_event_details', sports_event_details, methods=['GET'])

# api_manager.create_api(Client, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(Employee, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(RentalEvent, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(CreditCard, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(Rentable, methods=['GET'])
# api_manager.create_api(LiveActionSeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(AnimatedSeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(DocumentarySeries, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(StandUpComedySpecial, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(LiveActionMovie, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(AnimatedMovie, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(MusicalShow, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(Documentary, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(VideoGame, methods=['GET', 'POST', 'PUT', 'DELETE'])
# api_manager.create_api(SportsEvent, methods=['GET', 'POST', 'PUT', 'DELETE'])
