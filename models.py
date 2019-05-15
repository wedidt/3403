from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(32))

    def __init__(self, email=None, password=None):
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.email)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    info = Column(String)
    vote = Column(Integer)

    def __init__(self, name=None, info=None, vote=0):
        self.name = name
        self.info = info
        self.vote = vote

    def __repr__(self):
        return '<Movie %r>' % (self.name)
