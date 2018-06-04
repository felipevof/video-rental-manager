from enum import IntEnum

from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey

from .base import Base


class PaymentNetwork(IntEnum):
    VISA = 0
    MASTERCARD = 1
    ELO = 2
    HIPER = 3


class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    holder = Column(String)
    number = Column(String)
    expires_at = Column(Date)
    payment_network = Column(Enum(PaymentNetwork))

    def getClientId(self):
        return self.client_id

    def setClientId(self, value):
        self.client_id = value

    def getHolder(self):
        return self.holder

    def setHolder(self, value):
        self.holder = value

    def getNumber(self):
        return self.number

    def setNumber(self, value):
        self.number = value

    def getExpiresAt(self):
        return self.expires_at

    def setExpiresAt(self, value):
        self.expires_at = value

    def getPaymentNetwork(self):
        return self.payment_network

    def setPaymentNetwork(self, value):
        self.payment_network = value
