from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

basedir=os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:////' + os.path.join(basedir,"app.db"), convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import User, Movie

    Base.metadata.create_all(bind=engine)
