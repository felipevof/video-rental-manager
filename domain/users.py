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
    UNDISCLOSED=2


class EmployeePerformance(IntEnum):
    BAD=0
    REGULAR=1
    EXCEPTIONAL=2


class User(ABC):
    """
        The base object for all types of users of the system.
        This is an abstract class (extends ABC, Abstract Base Class)
    """
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
                 active:bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.registered_at = registered_at
        self.updated_at = updated_at
        self.birthdate = birthdate
        self.gender = gender
        self.cpf = cpf
        self.active = active

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

    def getActive(self):
        return self.active

    def setActive(self, value):
        self.active = value


class Employee(User):
    """
        A user that is an employee.
        Can approve a rent operation.
    """
    def __init__(self,
                 current_performance:EmployeePerformance,
                 in_training:bool):
        self.current_performance = current_performance
        self.in_training = in_training

    def getCurrentPerformance(self):
        return self.current_performance

    def setCurrentPerformance(self, value):
        self.current_performance = value

    def getInTraining(self):
        return self.in_training

    def setInTraining(self, value):
        self.in_training = value


class Client(User):
    """
        A user that is a client.
        Can rent rentables.
    """
    def __init__(self,
                 blacklisted:bool):
        self.blacklisted = blacklisted

    def getBlacklisted(self):
        return self.blacklisted

    def setBlacklisted(self, value):
        self.blacklisted = value
