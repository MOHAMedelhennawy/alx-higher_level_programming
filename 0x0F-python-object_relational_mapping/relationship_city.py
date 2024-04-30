#!/usr/bin/python3
"""
    Module that performs creates a States class based off of Base.
"""
from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base


class City(Base):
    """
        The ``City`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
