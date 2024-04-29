#!/usr/bin/python3
"""
Create simple table using sqlAlchmey
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    '''
    Table has two columns id, name
    '''
    __tablename__ = "cities"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates='city')