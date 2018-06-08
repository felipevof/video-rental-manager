"""
    Endpoints defined by the Web server, which constitutes its public interface.
"""

from datetime import date

from flask import render_template, g

from domain.users import Client, Employee
from domain.payment_methods import CreditCard
from domain.events import RentalEvent
from domain.rentables import (Rentable, LiveActionSeries, AnimatedSeries, DocumentarySeries,
                              StandUpComedySpecial, LiveActionMovie, AnimatedMovie,
                              MusicalShow, Documentary, VideoGame, SportsEvent)

from .utils import build_context, list_response, details_response, delete_response


def home():
    return render_template('home.html', **build_context())


def client_list():
    return list_response(Client, g.db_session, 'client/list.html')

def client_details(id):
    return details_response(Client, id, g.db_session, 'client/details.html')

def client_delete(id):
    return delete_response(Client, id, g.db_session)


def employee_list():
    return list_response(Employee, g.db_session, 'employee/list.html')

def employee_details(id):
    return details_response(Employee, id, g.db_session, 'employee/details.html')

def employee_delete(id):
    return delete_response(Employee, id, g.db_session)


def credit_card_list():
    return list_response(CreditCard, g.db_session, 'credit_card/list.html')

def credit_card_details(id):
    return details_response(CreditCard, id, g.db_session, 'credit_card/details.html')

def credit_card_delete(id):
    return delete_response(CreditCard, id, g.db_session)


def rental_event_list():
    return list_response(RentalEvent, g.db_session, 'rental_event/list.html')

def rental_event_details(id):
    return details_response(RentalEvent, id, g.db_session, 'rental_event/details.html')

def rental_event_delete(id):
    return delete_response(RentalEvent, id, g.db_session)


def rentable_list():
    return list_response(Rentable, g.db_session, 'rentable/list.html')

def rentable_delete(id):
    return delete_response(Rentable, id, g.db_session)


def live_action_series_list():
    return list_response(LiveActionSeries, g.db_session, 'rentable/live_action_series/list.html')

def live_action_series_details(id):
    return details_response(LiveActionSeries, id, g.db_session, 'rentable/live_action_series/details.html')


def animated_series_list():
    return list_response(AnimatedSeries, g.db_session, 'rentable/animated_series/list.html')

def animated_series_details(id):
    return details_response(AnimatedSeries, id, g.db_session, 'rentable/animated_series/details.html')


def documentary_series_list():
    return list_response(DocumentarySeries, g.db_session, 'rentable/documentary_series/list.html')

def documentary_series_details(id):
    return details_response(DocumentarySeries, id, g.db_session, 'rentable/documentary_series/details.html')


def stand_up_comedy_special_list():
    return list_response(StandUpComedySpecial, g.db_session, 'rentable/stand_up_comedy_special/list.html')

def stand_up_comedy_special_details(id):
    return details_response(StandUpComedySpecial, id, g.db_session, 'rentable/stand_up_comedy_special/details.html')


def live_action_movie_list():
    return list_response(LiveActionMovie, g.db_session, 'rentable/live_action_movie/list.html')

def live_action_movie_details(id):
    return details_response(LiveActionMovie, id, g.db_session, 'rentable/live_action_movie/details.html')


def animated_movie_list():
    return list_response(AnimatedMovie, g.db_session, 'rentable/animated_movie/list.html')

def animated_movie_details(id):
    return details_response(AnimatedMovie, id, g.db_session, 'rentable/animated_movie/details.html')


def musical_show_list():
    return list_response(MusicalShow, g.db_session, 'rentable/musical_show/list.html')

def musical_show_details(id):
    return details_response(MusicalShow, id, g.db_session, 'rentable/musical_show/details.html')


def documentary_list():
    return list_response(Documentary, g.db_session, 'rentable/documentary/list.html')

def documentary_details(id):
    return details_response(Documentary, id, g.db_session, 'rentable/documentary/details.html')


def video_game_list():
    return list_response(VideoGame, g.db_session, 'rentable/video_game/list.html')

def video_game_details(id):
    return details_response(VideoGame, id, g.db_session, 'rentable/video_game/details.html')


def sports_event_list():
    return list_response(SportsEvent, g.db_session, 'rentable/sports_event/list.html')

def sports_event_details(id):
    return details_response(SportsEvent, id, g.db_session, 'rentable/sports_event/details.html')
