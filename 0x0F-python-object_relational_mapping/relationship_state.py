#!/usr/bin/python3
"""
    Module that performs creates a States class based off of Base.
"""
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        The ``States`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
