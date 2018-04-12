"""
    Defines classes related to users of the system.
"""
from abc import ABC
from datetime import datetime, date
from enum import IntEnum

from .addresses import Address


class Gender(IntEnum):
    MALE=0
    FEMALE=1
    UNDISCLOSED=3


class User(ABC):
    """
        The base object for all types of users of the system.
        This is an abstract class (extends ABC, Abstract Base Class)
    """
    # [x] 10 attributes
    # [ ] Attributes encapsulated
    # [ ] Clients can set all 10 attributes
    # [ ] Persistent?
    # [x] Inheritance base?
    # [x] Abstract?
    # [ ] At least one one to many?
    # [ ] At least one many to many?
    # [ ] CRUD
    # [ ] Uses a relational DB
    def __init__(self,
                 name:str,
                 email:str,
                 phone:str,
                 address:Address,
                 registered_at:datetime,
                 updated_at:datetime,
                 birthdate:date,
                 gender:Gender,
                 cpf:str,
                 rg:str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.registered_at = registered_at
        self.updated_at = updated_at
        self.birthdate = birthdate
        self.gender = gender
        self.cpf = cpf
        self.rg = rg

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getEmail(self):
        return self.email

    def setEmail(self, value):
        self.email = value

    def getPhone(self):
        return self.phone

    def setPhone(self, value):
        self.phone = value

    def getAddress(self):
        return self.address

    def setAddress(self, value):
        self.address = value

    def getRegisteredAt(self):
        return self.registered_at

    def setRegisteredAt(self, value):
        self.registered_at = value

    def getUpdatedAt(self):
        return self.updated_at

    def setUpdatedAt(self, value):
        self.updated_at = value

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, value):
        self.birthdate = value

    def getGender(self):
        return self.gender

    def setGender(self, value):
        self.gender = value

    def getCPF(self):
        return self.cpf

    def setCPF(self, value):
        self.cpf = value

    def getRG(self):
        return self.rg

    def setRG(self, value):
        self.rg = value


class Employee(User):
    """
        A user that is an employee.
        Can approve a rent operation.
    """
    # [ ] 10 attributes
    # [ ] Attributes encapsulated
    # [ ] Clients can set all 10 attributes
    # [ ] Persistent?
    # [ ] Inheritance base?
    # [ ] Abstract?
    # [ ] At least one one to many?
    # [ ] At least one many to many?
    # [ ] CRUD
    # [ ] Uses a relational DB
    pass
    # TODO: fields
