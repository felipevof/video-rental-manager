import datetime

from sqlalchemy import Column, String, Integer, Date, Enum, Boolean
from sqlalchemy.orm import relationship

from .base import Base
from .payment_methods import CreditCard
from .utils import FormEnum


class Gender(FormEnum):
    MALE=0
    FEMALE=1
    UNDISCLOSED=2


class EmployeePerformance(FormEnum):
    BAD=0
    REGULAR=1
    EXCEPTIONAL=2
    NOT_ASSESSED=3


class User(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String, info={'label': 'Name'})
    email = Column(String, info={'label': 'Email'})
    birthdate = Column(Date, info={'label': 'Birth Date'})
    registered_at = Column(Date, default=datetime.date.today, info={'label': 'Registration Date'})
    gender = Column(Enum(Gender), info={'label': 'Gender'})
    active = Column(Boolean, default=True, info={'label': 'Active'})
    phone = Column(String, info={'label': 'Phone'})
    cpf = Column(String, info={'label': 'CPF'})

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getEmail(self):
        return self.email

    def setEmail(self, value):
        self.email = value

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, value):
        self.birthdate = value

    def getRegisteredAt(self):
        return self.registered_at

    def setRegisteredAt(self, value):
        self.registered_at = value

    def getGender(self):
        return self.gender

    def setGender(self, value):
        self.gender = value

    def getActive(self):
        return self.active

    def setActive(self, value):
        self.active = value

    def getPhone(self):
        return self.phone

    def setPhone(self, value):
        self.phone = value

    def getCPF(self):
        return self.cpf

    def setCPF(self, value):
        self.cpf = value


class Client(User):
    __tablename__ = 'clients'

    blacklisted = Column(Boolean, default=False, info={'label': 'Blacklisted'})
    address = Column(String, info={'label': 'Address'})
    credit_cards = relationship(CreditCard, backref="client")

    def getBlacklisted(self):
        return self.blacklisted

    def setBlacklisted(self, value):
        self.blacklisted = value

    def getAddress(self):
        return self.address

    def setAddress(self, value):
        self.address = value

    def getCreditCards(self):
        return self.credit_cards


class Employee(User):
    __tablename__ = 'employees'

    performance = Column(Enum(EmployeePerformance), default=EmployeePerformance.NOT_ASSESSED, info={'label': 'Performance'})
    in_training = Column(Boolean, default=True, info={'label': 'In Training'})

    def getPerformance(self):
        return self.performance

    def setPerformance(self, value):
        self.performance = value

    def getInTraining(self):
        return self.in_training

    def setInTraining(self, value):
        self.in_training = value
