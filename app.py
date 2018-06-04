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
from presentation.endpoints import (home, client_list, employee_list, credit_card_list,
                                    rental_event_list, rentable_list, live_action_series_list,
                                    animated_series_list, documentary_series_list,
                                    stand_up_comedy_special_list, live_action_movie_list,
                                    animated_movie_list, musical_show_list, documentary_list,
                                    video_game_list, sports_event_list)


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
app.add_url_rule('/employees', 'employee_list', employee_list)
app.add_url_rule('/credit_card', 'credit_card_list', credit_card_list)
app.add_url_rule('/rentals', 'rental_event_list', rental_event_list)
app.add_url_rule('/rentables', 'rentable_list', rentable_list)
app.add_url_rule('/live_action_series', 'live_action_series_list', live_action_series_list)
app.add_url_rule('/animated_series', 'animated_series_list', animated_series_list)
app.add_url_rule('/documentary_series', 'documentary_series_list', documentary_series_list)
app.add_url_rule('/stand_up_comedy_specials', 'stand_up_comedy_special_list', stand_up_comedy_special_list)
app.add_url_rule('/live_action_movies', 'live_action_movie_list', live_action_movie_list)
app.add_url_rule('/animated_movies', 'animated_movie_list', animated_movie_list)
app.add_url_rule('/musical_shows', 'musical_show_list', musical_show_list)
app.add_url_rule('/documentaries', 'documentary_list', documentary_list)
app.add_url_rule('/video_games', 'video_game_list', video_game_list)
app.add_url_rule('/sports_events', 'sports_event_list', sports_event_list)

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
