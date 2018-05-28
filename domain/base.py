from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite+pysqlite:///../rental.db', module=sqlite)
Session = sessionmaker(bind=engine)

Base = declarative_base()
