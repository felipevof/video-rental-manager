from enum import IntEnum

from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean, Table, ForeignKey, Enum
from sqlalchemy.orm import relationship

from base import Base


class RentalStatus(IntEnum):
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
    rented_at = Column(DateTime)
    ends_at = Column(DateTime)
    returned_at = Column(DateTime)
    rentables = relationship("Rentable", secondary=rental_event_rentables_association)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    notes = Column(String, nullable=True)
    status = Column(Enum(RentalStatus), default=RentalStatus.WAITING_RETURN)
    ignore_end_date = Column(Boolean, default=False)
    ignore_missing = Column(Boolean, default=False)

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

    def getEmployeeId(self):
        return self.employee_id

    def setEmployeeId(self, value):
        self.employee_id = value

    def getClientId(self):
        return self.client_id

    def setClientId(self, value):
        self.client_id = value

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
