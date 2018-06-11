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

from .forms import *

from .utils import build_context, list_response, details_response, delete_response, creation_response


def home():
    return render_template('home.html', **build_context())


def client_list():
    return list_response(Client, g.db_session, 'client/list.html')

def client_create():
    def _mapping(form, obj):
        obj.setName(form.name.data)
        obj.setEmail(form.email.data)
        obj.setBirthdate(form.birthdate.data)
        obj.setGender(form.gender.data)
        obj.setActive(form.active.data)
        obj.setPhone(form.phone.data)
        obj.setCPF(form.cpf.data)
        obj.setBlacklisted(form.blacklisted.data)
        obj.setAddress(form.address.data)

    return creation_response(Client, ClientForm, g.db_session, _mapping,
                             'client/create.html', 'client_list')

def client_details(id):
    return details_response(Client, id, g.db_session, 'client/details.html')

def client_delete(id):
    return delete_response(Client, id, g.db_session)


def employee_list():
    return list_response(Employee, g.db_session, 'employee/list.html')

def employee_create():
    def _mapping(form, obj):
        obj.setName(form.name.data)
        obj.setEmail(form.email.data)
        obj.setBirthdate(form.birthdate.data)
        obj.setGender(form.gender.data)
        obj.setActive(form.active.data)
        obj.setPhone(form.phone.data)
        obj.setCPF(form.cpf.data)
        obj.setPerformance(form.performance.data)

    return creation_response(Employee, EmployeeForm, g.db_session, _mapping,
                             'employee/create.html', 'employee_list') 

def employee_details(id):
    return details_response(Employee, id, g.db_session, 'employee/details.html')

def employee_delete(id):
    return delete_response(Employee, id, g.db_session)


def credit_card_list():
    return list_response(CreditCard, g.db_session, 'credit_card/list.html')

def credit_card_create():
    def _mapping(form, obj):
        obj.setClientId(form.client_id.data.id)
        obj.setHolder(form.holder.data)
        obj.setNumber(form.number.data)
        obj.setExpiresAt(form.expires_at.data)
        obj.setPaymentNetwork(form.payment_network.data)

    return creation_response(CreditCard, CreditCardForm, g.db_session, _mapping,
                             'credit_card/create.html', 'credit_card_list') 

def credit_card_details(id):
    return details_response(CreditCard, id, g.db_session, 'credit_card/details.html')

def credit_card_delete(id):
    return delete_response(CreditCard, id, g.db_session)


def rental_event_list():
    return list_response(RentalEvent, g.db_session, 'rental_event/list.html')

def rental_event_create():
    def _mapping(form, obj):
        obj.setEndsAt(form.ends_at.data)
        obj.setReturnedAt(form.returned_at.data)
        obj.setRentables(form.rentables.data)
        obj.setEmployeeId(form.employee_id.data.id)
        obj.setClientId(form.client_id.data.id)
        obj.setNotes(form.notes.data)

    return creation_response(RentalEvent, RentalEventForm, g.db_session, _mapping,
                             'rental_event/create.html', 'rental_event_list')

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

def live_action_series_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # season
        obj.setSeasonNumber(form.season_number.data)
        obj.setEpisodeCount(form.episode_count.data)
        obj.setEpisodeDurationMinutes(form.episode_duration_minutes.data)
        obj.setNetwork(form.network.data)
        obj.setGenre(form.genre.data)

        obj.setCast(form.cast.data)
        obj.setDirector(form.director.data)
        obj.setWriter(form.writer.data)
        obj.setEmmyNominee(form.emmy_nominee.data)
        obj.setEmmyWinner(form.emmy_winner.data)

    return creation_response(LiveActionSeries, LiveActionSeriesForm, g.db_session, _mapping,
                             'rentable/live_action_series/create.html', 'live_action_series_list')

def live_action_series_details(id):
    return details_response(LiveActionSeries, id, g.db_session, 'rentable/live_action_series/details.html')


def animated_series_list():
    return list_response(AnimatedSeries, g.db_session, 'rentable/animated_series/list.html')

def animated_series_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # season
        obj.setSeasonNumber(form.season_number.data)
        obj.setEpisodeCount(form.episode_count.data)
        obj.setEpisodeDurationMinutes(form.episode_duration_minutes.data)
        obj.setNetwork(form.network.data)
        obj.setGenre(form.genre.data)

        obj.setAnimationStudio(form.animation_studio.data)
        obj.setOriginalAuthor(form.original_author.data)
        obj.setHas2D(form.has_2d.data)
        obj.setHas3D(form.has_3d.data)
        obj.setAdultContent(form.adult_content.data)

    return creation_response(AnimatedSeries, AnimatedSeriesForm, g.db_session, _mapping,
                             'rentable/animated_series/create.html', 'animated_series_list')

def animated_series_details(id):
    return details_response(AnimatedSeries, id, g.db_session, 'rentable/animated_series/details.html')


def documentary_series_list():
    return list_response(DocumentarySeries, g.db_session, 'rentable/documentary_series/list.html')

def documentary_series_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # season
        obj.setSeasonNumber(form.season_number.data)
        obj.setEpisodeCount(form.episode_count.data)
        obj.setEpisodeDurationMinutes(form.episode_duration_minutes.data)
        obj.setNetwork(form.network.data)
        obj.setGenre(form.genre.data)

        obj.setDirector(form.director.data)
        obj.setNarrator(form.narrator.data)
        obj.setLocations(form.locations.data)
        obj.setGuests(form.guests.data)
        obj.setLowBudget(form.low_budget.data)

    return creation_response(DocumentarySeries, DocumentarySeriesForm, g.db_session, _mapping,
                             'rentable/documentary_series/create.html', 'documentary_series_list')

def documentary_series_details(id):
    return details_response(DocumentarySeries, id, g.db_session, 'rentable/documentary_series/details.html')


def stand_up_comedy_special_list():
    return list_response(StandUpComedySpecial, g.db_session, 'rentable/stand_up_comedy_special/list.html')

def stand_up_comedy_special_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # feature film
        obj.setDurationMinutes(form.duration_minutes.data)
        obj.setPublisher(form.publisher.data)
        obj.setProducer(form.producer.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setGenre(form.genre.data)

        obj.setHeadlinerComedian(form.headliner_comedian.data)
        obj.setOpenerComedian(form.opener_comedian.data)
        obj.setVenue(form.venue.data)
        obj.setOffensiveLanguage(form.offensive_language.data)
        obj.setAdditionalEntertainers(form.additional_entertainers.data)

    return creation_response(StandUpComedySpecial, StandUpComedySpecialForm, g.db_session, _mapping,
                             'rentable/stand_up_comedy_special/create.html', 'stand_up_comedy_special_list')

def stand_up_comedy_special_details(id):
    return details_response(StandUpComedySpecial, id, g.db_session, 'rentable/stand_up_comedy_special/details.html')


def live_action_movie_list():
    return list_response(LiveActionMovie, g.db_session, 'rentable/live_action_movie/list.html')

def live_action_movie_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # feature film
        obj.setDurationMinutes(form.duration_minutes.data)
        obj.setPublisher(form.publisher.data)
        obj.setProducer(form.producer.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setGenre(form.genre.data)

        obj.setLead(form.lead.data)
        obj.setCast(form.cast.data)
        obj.setDirector(form.director.data)
        obj.setWriter(form.writer.data)
        obj.setOscarNominee(form.oscar_nominee.data)
        obj.setOscarWinner(form.oscar_winner.data)

    return creation_response(LiveActionMovie, LiveActionMovieForm, g.db_session, _mapping,
                             'rentable/live_action_movie/create.html', 'live_action_movie_list')

def live_action_movie_details(id):
    return details_response(LiveActionMovie, id, g.db_session, '/details.html')


def animated_movie_list():
    return list_response(AnimatedMovie, g.db_session, 'rentable/animated_movie/list.html')

def animated_movie_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # feature film
        obj.setDurationMinutes(form.duration_minutes.data)
        obj.setPublisher(form.publisher.data)
        obj.setProducer(form.producer.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setGenre(form.genre.data)

        obj.setAnimationStudio(form.animation_studio.data)
        obj.setOriginalAuthor(form.original_author.data)
        obj.setHas2D(form.has_2d.data)
        obj.setHas3D(form.has_3d.data)
        obj.setAdultContent(form.adult_content.data)

    return creation_response(AnimatedMovie, AnimatedMovieForm, g.db_session, _mapping,
                             'rentable/animated_movie/create.html', 'animated_movie_list')

def animated_movie_details(id):
    return details_response(AnimatedMovie, id, g.db_session, 'rentable/animated_movie/details.html')


def musical_show_list():
    return list_response(MusicalShow, g.db_session, 'rentable/musical_show/list.html')

def musical_show_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # feature film
        obj.setDurationMinutes(form.duration_minutes.data)
        obj.setPublisher(form.publisher.data)
        obj.setProducer(form.producer.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setGenre(form.genre.data)

        obj.setArtist(form.artist.data)
        obj.setVenue(form.venue.data)
        obj.setLive(form.live.data)
        obj.setAcoustic(form.acoustic.data)
        obj.setGrammyNominee(form.grammy_nominee.data)
        obj.setGrammyWinner(form.grammy_winner.data)

    return creation_response(MusicalShow, MusicalShowForm, g.db_session, _mapping,
                             'rentable/musical_show/create.html', 'musical_show_list')

def musical_show_details(id):
    return details_response(MusicalShow, id, g.db_session, 'rentable/musical_show/details.html')


def documentary_list():
    return list_response(Documentary, g.db_session, 'rentable/documentary/list.html')

def documentary_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        # feature film
        obj.setDurationMinutes(form.duration_minutes.data)
        obj.setPublisher(form.publisher.data)
        obj.setProducer(form.producer.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setGenre(form.genre.data)

        obj.setDirector(form.director.data)
        obj.setNarrator(form.narrator.data)
        obj.setLocations(form.locations.data)
        obj.setGuests(form.guests.data)
        obj.setLowBudget(form.low_budget.data)

    return creation_response(Documentary, DocumentaryForm, g.db_session, _mapping,
                             'rentable/documentary/create.html', 'documentary_list')

def documentary_details(id):
    return details_response(Documentary, id, g.db_session, 'rentable/documentary/details.html')


def video_game_list():
    return list_response(VideoGame, g.db_session, 'rentable/video_game/list.html')

def video_game_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        obj.setPublisher(form.publisher.data)
        obj.setDeveloper(form.developer.data)
        obj.setGenre(form.genre.data)
        obj.setPlatform(form.platform.data)
        obj.setDemo(form.demo.data)
        obj.setReleaseYear(form.release_year.data)
        obj.setSinglePlayer(form.single_player.data)
        obj.setLocalMultiplayer(form.local_multiplayer.data)
        obj.setOnlineMultiplayer(form.online_multiplayer.data)
        obj.setDLCIncluded(form.dlc_included.data)

    return creation_response(VideoGame, VideoGameForm, g.db_session, _mapping,
                             'rentable/video_game/create.html', 'video_game_list')

def video_game_details(id):
    return details_response(VideoGame, id, g.db_session, 'rentable/video_game/details.html')


def sports_event_list():
    return list_response(SportsEvent, g.db_session, 'rentable/sports_event/list.html')

def sports_event_create():
    def _mapping(form, obj):
        # rentables
        obj.setTitle(form.title.data)
        obj.setDescription(form.description.data)
        obj.setLanguage(form.language.data)
        obj.setAgeRestriction(form.age_restriction.data)
        obj.setRentPrice(form.rent_price.data)
        obj.setPosterImage(form.poster_image.data)

        obj.setNetwork(form.network.data)
        obj.setLeague(form.league.data)
        obj.setChampionshipPhase(form.championship_phase.data)
        obj.setLocation(form.location.data)
        obj.setPeriods(form.periods.data)
        obj.setPeriodDurationMinutes(form.period_duration_minutes.data)
        obj.setHomeTeam(form.home_team.data)
        obj.setAwayTeam(form.away_team.data)
        obj.setHomeTeamScore(form.home_team_score.data)
        obj.setAwayTeamScore(form.away_team_score.data)

    return creation_response(SportsEvent, SportsEventForm, g.db_session, _mapping,
                             'rentable/sports_event/create.html', 'sports_event_list')

def sports_event_details(id):
    return details_response(SportsEvent, id, g.db_session, 'rentable/sports_event/details.html')
