from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine, or_
from sqlalchemy.inspection import inspect
from sqlalchemy.types import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite+pysqlite:///rental.db', module=sqlite)
Session = sessionmaker(bind=engine)

class Searchable(object):
    @classmethod
    def filter_by_str(cls, session, query):
        table = inspect(cls)

        columns = [col for col in table.c if isinstance(col.type, String)]
        filters = [col.contains(query) for col in columns]

        return session.query(cls).filter(or_(*filters))

Base = declarative_base(cls=Searchable)
