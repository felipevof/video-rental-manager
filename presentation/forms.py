from datetime import datetime

from wtforms import HiddenField
from wtforms_alchemy import ModelForm
from wtforms_alchemy.fields import QuerySelectField, SelectField, QuerySelectMultipleField

from domain.users import Client, Employee, Gender, EmployeePerformance
from domain.payment_methods import CreditCard, PaymentNetwork
from domain.events import RentalEvent, RentalStatus
from domain.rentables import (Rentable, LiveActionSeries, AnimatedSeries, DocumentarySeries,
                              StandUpComedySpecial, LiveActionMovie, AnimatedMovie,
                              MusicalShow, Documentary, VideoGame, SportsEvent)


class ClientForm(ModelForm):
    class Meta:
        model = Client

    gender = SelectField(choices=Gender.choices(), coerce=Gender.coerce)


class EmployeeForm(ModelForm):
    class Meta:
        model = Client

    gender = SelectField(choices=Gender.choices(), coerce=Gender.coerce)
    performance = SelectField(choices=EmployeePerformance.choices(), coerce=EmployeePerformance.coerce)


class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard

    client_id = QuerySelectField(query_factory=lambda: Client.query.all(), allow_blank=False)
    payment_network = SelectField(choices=PaymentNetwork.choices(), coerce=PaymentNetwork.coerce)


class RentalEventForm(ModelForm):
    class Meta:
        model = RentalEvent

    status = SelectField(choices=RentalStatus.choices(), coerce=RentalStatus.coerce)
    client_id = QuerySelectField(query_factory=lambda: Client.query.all(), allow_blank=False)
    employee_id = QuerySelectField(query_factory=lambda: Employee.query.all(), allow_blank=False)
    rentables = QuerySelectMultipleField(query_factory=lambda: Rentable.query.all(), allow_blank=False)

class LiveActionSeriesForm(ModelForm):
    class Meta:
        model = LiveActionSeries

    rentable_type = HiddenField(default="live_action_series")


class AnimatedSeriesForm(ModelForm):
    class Meta:
        model = AnimatedSeries

    rentable_type = HiddenField(default="animated_series")


class DocumentarySeriesForm(ModelForm):
    class Meta:
        model = DocumentarySeries

    rentable_type = HiddenField(default="documentary_series")


class StandUpComedySpecialForm(ModelForm):
    class Meta:
        model = StandUpComedySpecial

    rentable_type = HiddenField(default="stand_up_comedy_special")


class LiveActionMovieForm(ModelForm):
    class Meta:
        model = LiveActionMovie

    rentable_type = HiddenField(default="live_action_series")


class AnimatedMovieForm(ModelForm):
    class Meta:
        model = AnimatedMovie

    rentable_type = HiddenField(default="live_action_movie")


class MusicalShowForm(ModelForm):
    class Meta:
        model = MusicalShow

    rentable_type = HiddenField(default="musical_show")


class DocumentaryForm(ModelForm):
    class Meta:
        model = Documentary

    rentable_type = HiddenField(default="documentary")


class VideoGameForm(ModelForm):
    class Meta:
        model = VideoGame

    rentable_type = HiddenField(default="video_game")


class SportsEventForm(ModelForm):
    class Meta:
        model = SportsEvent

    rentable_type = HiddenField(default="sports_event")
