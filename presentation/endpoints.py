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

from .utils import build_context, list_response


def home():
    return render_template('home.html', **build_context())


def client_list():
    return list_response(Client, g.db_session, 'client/list.html')


def employee_list():
    return list_response(Employee, g.db_session, 'employee/list.html')


def credit_card_list():
    return list_response(CreditCard, g.db_session, 'credit_card/list.html')


def rental_event_list():
    return list_response(RentalEvent, g.db_session, 'rental_event/list.html')


def rentable_list():
    return list_response(Rentable, g.db_session, 'rentable/list.html')


def live_action_series_list():
    return list_response(LiveActionSeries, g.db_session, 'rentable/live_action_series/list.html')


def animated_series_list():
    return list_response(AnimatedSeries, g.db_session, 'rentable/animated_series/list.html')


def documentary_series_list():
    return list_response(DocumentarySeries, g.db_session, 'rentable/documentary_series/list.html')


def stand_up_comedy_special_list():
    return list_response(StandUpComedySpecial, g.db_session, 'rentable/stand_up_comedy_special/list.html')


def live_action_movie_list():
    return list_response(LiveActionMovie, g.db_session, 'rentable/live_action_movie/list.html')


def animated_movie_list():
    return list_response(AnimatedMovie, g.db_session, 'rentable/animated_movie/list.html')


def musical_show_list():
    return list_response(MusicalShow, g.db_session, 'rentable/musical_show/list.html')


def documentary_list():
    return list_response(Documentary, g.db_session, 'rentable/documentary/list.html')


def video_game_list():
    return list_response(VideoGame, g.db_session, 'rentable/video_game/list.html')


def sports_event_list():
    return list_response(SportsEvent, g.db_session, 'rentable/sports_event/list.html')