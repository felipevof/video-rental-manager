"""
    The configuration for the top-level object that represents the Web server.
"""

from flask import Flask, g

from domain.base import engine, Base, session
from domain.users import Client, Employee
from presentation.endpoints import *


# --- Database setup
Base.metadata.create_all(engine)

app = Flask('video-rental-manager')

# --- Routes
@app.before_request
def before_request():
    g.db_session = session

app.add_url_rule('/', 'home', home)

app.add_url_rule('/clients', 'client_list', client_list, methods=['GET'])
app.add_url_rule('/clients/new', 'client_create', client_create, methods=['GET', 'POST'])
app.add_url_rule('/clients/<id>', 'client_details', client_details, methods=['GET'])
app.add_url_rule('/clients/<id>', 'client_delete', client_delete, methods=['DELETE'])

app.add_url_rule('/employees', 'employee_list', employee_list, methods=['GET'])
app.add_url_rule('/employees/new', 'employee_create', employee_create, methods=['GET', 'POST'])
app.add_url_rule('/employees/<id>', 'employee_details', employee_details, methods=['GET'])
app.add_url_rule('/employees/<id>', 'employee_delete', employee_delete, methods=['DELETE'])

app.add_url_rule('/credit_cards', 'credit_card_list', credit_card_list, methods=['GET'])
app.add_url_rule('/credit_cards/new', 'credit_card_create', credit_card_create, methods=['GET', 'POST'])
app.add_url_rule('/credit_cards/<id>', 'credit_card_details', credit_card_details, methods=['GET'])
app.add_url_rule('/credit_cards/<id>', 'credit_card_delete', credit_card_delete, methods=['DELETE'])

app.add_url_rule('/rentals', 'rental_event_list', rental_event_list, methods=['GET'])
app.add_url_rule('/rentals/new', 'rental_event_create', rental_event_create, methods=['GET', 'POST'])
app.add_url_rule('/rentals/<id>', 'rental_event_details', rental_event_details, methods=['GET'])
app.add_url_rule('/rentals/<id>', 'rental_event_delete', rental_event_delete, methods=['DELETE'])

app.add_url_rule('/rentables', 'rentable_list', rentable_list, methods=['GET'])
app.add_url_rule('/rentables/<id>', 'rentable_delete', rentable_delete, methods=['DELETE'])

app.add_url_rule('/live_action_series', 'live_action_series_list', live_action_series_list, methods=['GET'])
app.add_url_rule('/live_action_series/new', 'live_action_series_create', live_action_series_create, methods=['GET', 'POST'])
app.add_url_rule('/live_action_series/<id>', 'live_action_series_details', live_action_series_details, methods=['GET'])

app.add_url_rule('/animated_series', 'animated_series_list', animated_series_list, methods=['GET'])
app.add_url_rule('/animated_series/new', 'animated_series_create', animated_series_create, methods=['GET', 'POST'])
app.add_url_rule('/animated_series/<id>', 'animated_series_details', animated_series_details, methods=['GET'])

app.add_url_rule('/documentary_series', 'documentary_series_list', documentary_series_list, methods=['GET'])
app.add_url_rule('/documentary_series/new', 'documentary_series_create', documentary_series_create, methods=['GET', 'POST'])
app.add_url_rule('/documentary_series/<id>', 'documentary_series_details', documentary_series_details, methods=['GET'])

app.add_url_rule('/stand_up_comedy_specials', 'stand_up_comedy_special_list', stand_up_comedy_special_list, methods=['GET'])
app.add_url_rule('/stand_up_comedy_specials/new', 'stand_up_comedy_special_create', stand_up_comedy_special_create, methods=['GET', 'POST'])
app.add_url_rule('/stand_up_comedy_specials/<id>', 'stand_up_comedy_special_details', stand_up_comedy_special_details, methods=['GET'])

app.add_url_rule('/live_action_movies', 'live_action_movie_list', live_action_movie_list, methods=['GET'])
app.add_url_rule('/live_action_movies/new', 'live_action_movie_create', live_action_movie_create, methods=['GET', 'POST'])
app.add_url_rule('/live_action_movies/<id>', 'live_action_movie_details', live_action_movie_details, methods=['GET'])

app.add_url_rule('/animated_movies', 'animated_movie_list', animated_movie_list, methods=['GET'])
app.add_url_rule('/animated_movies/new', 'animated_movie_create', animated_movie_create, methods=['GET', 'POST'])
app.add_url_rule('/animated_movies/<id>', 'animated_movie_details', animated_movie_details, methods=['GET'])

app.add_url_rule('/musical_shows', 'musical_show_list', musical_show_list, methods=['GET'])
app.add_url_rule('/musical_shows/new', 'musical_show_create', musical_show_create, methods=['GET', 'POST'])
app.add_url_rule('/musical_shows/<id>', 'musical_show_details', musical_show_details, methods=['GET'])

app.add_url_rule('/documentaries', 'documentary_list', documentary_list, methods=['GET'])
app.add_url_rule('/documentaries/new', 'documentary_create', documentary_create, methods=['GET', 'POST'])
app.add_url_rule('/documentaries/<id>', 'documentary_details', documentary_details, methods=['GET'])

app.add_url_rule('/video_games', 'video_game_list', video_game_list, methods=['GET'])
app.add_url_rule('/video_games/new', 'video_game_create', video_game_create, methods=['GET', 'POST'])
app.add_url_rule('/video_games/<id>', 'video_game_details', video_game_details, methods=['GET'])

app.add_url_rule('/sports_events', 'sports_event_list', sports_event_list, methods=['GET'])
app.add_url_rule('/sports_events/new', 'sports_event_create', sports_event_create, methods=['GET', 'POST'])
app.add_url_rule('/sports_events/<id>', 'sports_event_details', sports_event_details, methods=['GET'])
