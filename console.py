import datetime

from domain.base import Session, engine, Base
from domain.users import Client, Employee, Gender
from domain.rentables import (Rentable, StandUpComedySpecial, LiveActionSeries, AnimatedSeries,
                              DocumentarySeries, LiveActionMovie, AnimatedMovie, MusicalShow,
                              Documentary, VideoGame, SportsEvent)
from domain.events import RentalEvent
from domain.payment_methods import CreditCard, PaymentNetwork


def new_session():
    return Session()


Base.metadata.create_all(engine)

session = new_session()

e = Employee(name='Monica Bezerra', email='mb@gmail.com',
             birthdate=datetime.date(day=10, month=10, year=1990),
             registered_at=datetime.datetime.now(),
             gender=Gender.FEMALE, phone="81989074523", cpf="12345678912")

c = Client(name='Marcos Ferreira', email='mf@gmail.com',
             birthdate=datetime.date(day=1, month=2, year=1980),
             registered_at=datetime.datetime.now(),
             gender=Gender.MALE, phone="81956123456", cpf="98765432190",
             address="Rua Rouxinol, 456")


r1 = LiveActionMovie(title="Avengers: Age of Ultron", description="A great marvel movie!", age_restriction=13,
                     language='English', rent_price=5, duration_minutes=180, publisher="Marvel", producer="Marvel",
                     release_year=2015, genre="action", lead="Multiple", cast="A,B,C", director="Joss Whedon",
                     writer="Joss Whedon", oscar_nominee=False, oscar_winner=False,
                     poster_image="https://images-na.ssl-images-amazon.com/images/I/71SIYxcSNOL._SY606_.jpg")

r2 = AnimatedSeries(title="Cowboy Bebop", description="A great anime!", age_restriction=18,
                    language='English', rent_price=4,
                    poster_image="https://img.etsystatic.com/il/ef493f/414494942/il_570xN.414494942_8lfw.jpg",
                    season_number=1, episode_count=7, episode_duration_minutes=45, network="Netflix", genre="sci-fi",
                    animation_studio="RSK Studio", original_author="Mazaki Kurumada", has_3d=False, has_2d=True, adult_content=False)

r3 = StandUpComedySpecial(title="You people are all the same",
                          description="Cool special from billy boy",
                          age_restriction=18, duration_minutes=70, headliner_comedian="Bill Burr",
                          opener_comedian='Joe DeRosa', language='English', rent_price=10,
                          publisher="Netflix", producer="Loner Productions", release_year=2012, genre="Observational Comedy",
                          offensive_language=True, venue='Ohio Theater',
                          poster_image="https://a.ltrbxd.com/resized/film-poster/1/3/7/8/5/0/137850-bill-burr-you-people-are-all-the-same-0-230-0-345-crop.jpg?k=e231260ea6")

r4 = LiveActionSeries(title="Black Mirror",
                      description="Weird tech stuff happens",
                      age_restriction=16, rent_price=4, poster_image="http://www.awardscircuit.com/wp-content/uploads/2016/12/black-mirror-season-3-poster.jpg",
                      season_number=1, episode_count=7, episode_duration_minutes=45, network="Netflix", genre="sci-fi",
                      cast="Varied", director="Charlie Brooker", writer="Charlie Brooker", emmy_nominee=False, emmy_winner=False)


r5 = DocumentarySeries(title="Planet Earth 2", description="Continuation of the famous BBC Planet Earth series", age_restriction=0,
                    language='English', rent_price=4, poster_image="http://dizw242ufxqut.cloudfront.net/images/product/movie/dvd/image5/planet_earth_2_nordic-39715318-.jpg",
                    season_number=1, episode_count=7, episode_duration_minutes=45, network="BBC", genre="nature",
                    director="David Attenborough", narrator="David Attenborough", locations="Africa,South America,Arctic",
                    low_budget=False)

r6 = AnimatedMovie(title="Akira", description="Legendary animated movie", age_restriction=15,
                   language='Japanese', rent_price=5, duration_minutes=130, publisher="Company", producer="Great Studio",
                   release_year=1988, genre="sci-fi",
                   animation_studio="RSK Studio", original_author="Mazaki Kurumada", has_3d=False, has_2d=True, adult_content=False,
                   poster_image="https://m.media-amazon.com/images/M/MV5BM2ZiZTk1ODgtMTZkNS00NTYxLWIxZTUtNWExZGYwZTRjODViXkEyXkFqcGdeQXVyMTE2MzA3MDM@._V1_SY1000_CR0,0,675,1000_AL_.jpg")



r7 = MusicalShow(title="Iron Maiden @ Rock in Rio", description="\m/", age_restriction=14,
                 language='English', rent_price=5, duration_minutes=180, publisher="XL", producer="XL",
                 release_year=2001, genre="music", artist="Iron Maiden", venue="Maracana", live=True, acoustic=False,
                 grammy_nominee=False, grammy_winner=False,
                 poster_image="https://images-na.ssl-images-amazon.com/images/I/5155YQVT2GL._SY445_.jpg")


r8 = Documentary(title="March of the Penguins", description="Documentary about penguins", age_restriction=0,
                 language='English', rent_price=5, duration_minutes=120, publisher="BBC", producer="BBC",
                 release_year=2005, genre="nature", director="David Attenborough", narrator="David Attenborough",
                 locations="Arctic", low_budget=False,
                 poster_image="https://m.media-amazon.com/images/M/MV5BMTM1NDc5MDYxMl5BMl5BanBnXkFtZTcwMjMzNDAzMQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg")


r9 = VideoGame(title="The Elder Scrolls V: Skyrim Special Edition", description="Fantasy RPG",
               age_restriction=13, language='English', rent_price=12,
               publisher="Bethesda", developer="Bethesda Studios", genre="RPG", platform="PS4",
               demo=False, release_year=2017, single_player=True, local_multiplayer=False,
               online_multiplayer=False, dlc_included=True,
               poster_image="https://images-na.ssl-images-amazon.com/images/I/71ZM5nJFayL._SX679_.jpg")

r10 = SportsEvent(title="Super Bowl LII", description="Finals of the NFL, 2018",
                   age_restriction=0, language='English', rent_price=3,
                   poster_image="https://cdn.shopify.com/s/files/1/2028/5101/products/super-bowl-lii-2018-minnesota-theme-art-logo-poster_large.jpg?v=1508211454",
                   network="CBS", league="NFL", championship_phase="Finals", location="Minnesota",
                   periods=5, period_duration_minutes=15, home_team="New England Patriots", away_team="Philadelphia Eagles",
                   home_team_score=33, away_team_score=41)

session.add(e)
session.add(c)
session.add(r1)
session.add(r2)
session.add(r3)
session.add(r4)
session.add(r5)
session.add(r6)
session.add(r7)
session.add(r8)
session.add(r9)
session.add(r10)

session.commit()

ca = CreditCard(client_id=c.id, holder='H P S', number='123456782389',
                expires_at=datetime.date(day=1, month=2, year=2020),
                payment_network=PaymentNetwork.VISA)

rt = RentalEvent(rented_at=datetime.datetime.now(), ends_at=datetime.datetime.now(),
                 rentables=[r1,r2, r3, r4], employee_id=e.id, client_id=c.id)

session.add(ca)
session.add(rt)

session.commit()
session.close()