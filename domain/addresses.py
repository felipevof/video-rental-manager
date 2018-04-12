"""
    Defines classes related addresses.
"""


class Address(object):
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
    def __init__(self,
                 street:str,
                 # not all street numbers are integer-only (for instance: 415B), hence the str
                 number:str,
                 extra:str,
                 zip_code:int,
                 city:str,
                 state:str,
                 country:str):
        self.street = street
        self.number = number
        self.extra = extra
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country

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
