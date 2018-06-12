import datetime

from sqlalchemy import Column, String, Integer, Date, Boolean, Table, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .base import Base
from .rentables import Rentable
from .utils import FormEnum


class RentalStatus(FormEnum):
    WAITING_RETURN=0
    ITEMS_RETURNED_OK=1
    ITEMS_RETURNED_DAMAGED=2
    ITEMS_RETURNED_MISSING=3
    ITEMS_NOT_RETURNED=4


rental_event_rentables_association = Table('rental_events_rentables', Base.metadata,
    Column('rental_event_id', Integer, ForeignKey('rental_events.id')),
    Column('rentable_id', Integer, ForeignKey('rentables.id'))
)


class RentalEvent(Base):
    __tablename__ = 'rental_events'

    id = Column(Integer, primary_key=True)
    rented_at = Column(Date, default=datetime.date.today, info={'label': 'Rent Date'})
    ends_at = Column(Date, info={'label': 'End Date'})
    returned_at = Column(Date, nullable=True, info={'label': 'Return Date'})
    rentables = relationship("Rentable", secondary=rental_event_rentables_association, info={'label': 'Rentables'})
    employee_id = Column(Integer, ForeignKey('employees.id'), info={'label': 'Employee'})
    employee = relationship("Employee")
    client_id = Column(Integer, ForeignKey('clients.id'), info={'label': 'Client'})
    client = relationship("Client")
    notes = Column(String, nullable=True, info={'label': 'Notes'})
    status = Column(Enum(RentalStatus), default=RentalStatus.WAITING_RETURN, info={'label': 'Status'})
    ignore_end_date = Column(Boolean, default=False, info={'label': 'Ignore End Date'})
    ignore_missing = Column(Boolean, default=False, info={'label': 'Ignore Missing'})

    def getRentedAt(self):
        return self.rented_at

    def setRentedAt(self, value):
        self.rented_at = value

    def getEndsAt(self):
        return self.ends_at

    def setEndsAt(self, value):
        self.ends_at = value

    def getReturnedAt(self):
        return self.returned_at

    def setReturnedAt(self, value):
        self.returned_at = value

    def getRentables(self):
        return self.rentables

    def setRentables(self, value):
        self.rentables.clear()
        for v in value:
            self.rentables.append(v)

    def getEmployee(self):
        return self.employee

    def setEmployee(self, value):
        self.employee = value

    def getClient(self):
        return self.client

    def setClient(self, value):
        self.client = value

    def getNotes(self):
        return self.notes

    def setNotes(self, value):
        self.notes = value

    def getStatus(self):
        return self.status

    def setStatus(self, value):
        self.status = value

    def getIgnoreEndDate(self):
        return self.ignore_end_date

    def setIgnoreEndDate(self, value):
        self.ignore_end_date = value

    def getIgnoreMissing(self):
        return self.ignore_missing

    def setIgnoreMissing(self, value):
        self.ignore_missing = value
