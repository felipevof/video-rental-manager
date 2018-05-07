"""
    Defines classes related addresses.
"""
from enum import IntEnum


class AddressType(IntEnum):
    COMMERCIAL=0
    RESIDENTIAL=1


class Address(object):
    """
        How an address is modeled in the application.
    """
    def __init__(self,
                 street:str,
                 # not all street numbers are integer-only (for instance: 415B), hence the str
                 number:str,
                 extra:str,
                 zip_code:int,
                 city:str,
                 state:str,
                 country:str,
                 reference:str,
                 address_type:AddressType,
                 distance_fee_applicable:bool):
        self.street = street
        self.number = number
        self.extra = extra
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country
        self.reference = reference
        self.address_type = address_type
        self.distance_fee_applicable = distance_fee_applicable

    def getStreet(self):
        return self.street

    def setStreet(self, value):
        self.street = value

    def getNumber(self):
        return self.number

    def setNumber(self, value):
        self.number = value

    def getExtra(self):
        return self.extra

    def setExtra(self, value):
        self.extra = value

    def getZIPCode(self):
        return self.zip_code

    def setZIPCode(self, value):
        self.zip_code = value

    def getCity(self):
        return self.city

    def setCity(self, value):
        self.city = value

    def getState(self):
        return self.state

    def setState(self, value):
        self.state = value

    def getCountry(self):
        return self.country

    def setCountry(self, value):
        self.country = value

    def getReference(self):
        return self.reference

    def setReference(self, value):
        self.reference = value

    def getAddressType(self):
        return self.address_type

    def setAddressType(self, value):
        self.address_type = value

    def getDistanceFeeApplicable(self):
        return self.distance_fee_applicable

    def setDistanceFeeApplicable(self, value):
        self.distance_fee_applicable = value
