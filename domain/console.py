import datetime

from base import Session, engine, Base
from users import Client, Employee, Gender
from rentables import Rentable, StandUpComedySpecial
from events import RentalEvent
from payment_methods import CreditCard, PaymentNetwork


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



r1 = Rentable(title="Avengers 2", description="A great marvel movie!", age_restriction=13, language='English', rent_price=5)
r2 = Rentable(title="Cowboy Bebop", description="A great anime!", age_restriction=18, language='English', rent_price=4)
r3 = StandUpComedySpecial(title="You people are all the same",
                          description="Cool special from billy boy",
                          age_restriction=18, duration_minutes=70, headliner_comedian="Bill Burr",
                          opener_comedian='Joe DeRosa', language='English', rent_price=10,
                          offensive_language=True, venue='Ohio Theater')

session.add(e)
session.add(c)
session.add(r1)
session.add(r2)
session.add(r3)

session.commit()

ca = CreditCard(client_id=c.id, holder='H P S', number='123456782389',
                expires_at=datetime.date(day=1, month=2, year=2020),
                payment_network=PaymentNetwork.VISA)

rt = RentalEvent(rented_at=datetime.datetime.now(), ends_at=datetime.datetime.now(),
                 rentables=[r1,r2, r3], employee_id=e.id, client_id=c.id)

session.add(ca)
session.add(rt)

session.commit()
session.close()