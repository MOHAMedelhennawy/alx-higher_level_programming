#!/usr/bin/python3

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    '''
    Table has two columns id, name
    '''
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
