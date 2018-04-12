"""
    Defines classes related to items that can be rented by users.
"""
from abc import ABC
from datetime import datetime
from enum import IntEnum


class RentableStatus(IntEnum):
    AVAILABLE=0
    RENTED=1
    MISSING=2
    DAMAGED=3


class Rentable(ABC):
    """
        The base object for all objects that can be rented by users.
        This is an abstract class (extends ABC, Abstract Base Class).
    """
    # [ ] 10 attributes
    # [ ] Attributes encapsulated
    # [ ] Clients can set all 10 attributes
    # [ ] Persistent?
    # [x] Inheritance base?
    # [x] Abstract?
    # [ ] At least one one to many?
    # [x] At least one many to many?
    # [ ] CRUD
    # [ ] Uses a relational DB
    def __init__(self,
                 name:str,
                 description:str,
                 registered_at:datetime,
                 updated_at:datetime,
                 status:RentableStatus,
                 related_rentables:list):
        self.name = name
        self.description = description
        self.registered_at = registered_at
        self.updated_at = updated_at
        self.status = status
        self.related_rentables = related_rentables

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getDescription(self):
        return self.description

    def setDescription(self, value):
        self.description = value

    def getRegisteredAt(self):
        return self.registered_at

    def setRegisteredAt(self, value):
        self.registered_at = value

    def getUpdatedAt(self):
        return self.updated_at

    def setUpdatedAt(self, value):
        self.updatedAt = value

    def getStatus(self):
        return self.status

    def setStatus(self, value):
        self.status = value

    def getRelatedRentables(self):
        return self.related_rentables

    def setRelatedRentables(self, value):
        self.related_rentables = value


# TODO: The concrete types