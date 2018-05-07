"""
    Defines classes related to payments.
"""
from enum import IntEnum
from datetime import datetime

from .users import User


class PaymentMethod(IntEnum):
    CASH=0
    DEBIT_CARD=1
    CREDIT_CARD=2


class Payment(object):
    """
        Represents a payment made by a user.
    """
    def __init__(self,
                 user:User,
                 method:PaymentMethod,
                 amount:float,
                 made_at:datetime):
        self.user = user
        self.method = method
        self.amount = amount
        self.made_at = made_at

    def getUser(self):
        return self.user

    def setUser(self, value):
        self.user = value

    def getMethod(self):
        return self.method

    def setMethod(self, value):
        self.method = value

    def getAmount(self):
        return self.amount

    def setAmount(self, value):
        self.amount = value

    def getMadeAt(self):
        return self.made_at

    def setMadeAt(self, value):
        self.made_at = value
