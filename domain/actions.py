"""
    Defines classes related to actions performed in the system.
"""
from datetime import datetime
from enum import IntEnum

from .users import User, Employee
from .payments import Payment


class RentalStatus(IntEnum):
    ONGOING=0
    FINISHED=1


class Rental(object):
    """
        The action that is logged when a user rents one or multiple rentable assets.
    """
    def __init__(self,
                 rentables:list,
                 rented_by:User,
                 employee: Employee,
                 rented_at:datetime,
                 due_at:datetime,
                 returned_at:datetime,
                 status:RentalStatus,
                 notes:str,
                 payment:Payment,
                 damaged:bool):
        self.rentables = rentables
        self.rented_by = rented_by
        self.employee = employee
        self.rented_at = rented_at
        self.due_at = due_at
        self.returned_at = returned_at
        self.status = status
        self.notes = notes
        self.payment = payment
        self.damaged = damaged

    def getRentables(self):
        return self.rentables

    def setRentables(self, value):
        self.rentables = value

    def getRentedBy(self):
        return self.rented_by

    def setRentedBy(self, value):
        self.rented_by = value

    def getEmployee(self):
        return self.employee

    def setEmployee(self, value):
        self.employee = value

    def getRentedAt(self):
        return self.rented_at

    def setRentedAt(self, value):
        self.rented_at = value

    def getDueAt(self):
        return self.due_at

    def setDueAt(self, value):
        self.due_at = value

    def getReturnedAt(self):
        return self.returned_at

    def setReturnedAt(self, value):
        self.returned_at = value

    def getStatus(self):
        return self.status

    def setStatus(self, value):
        self.status = value

    def getNotes(self):
        return self.notes

    def setNotes(self, value):
        self.notes = value

    def getPayment(self):
        return self.payment

    def setPayment(self, value):
        self.payment = value

    def getDamaged(self):
        return self.damaged

    def setDamaged(self, value):
        self.damaged = value
