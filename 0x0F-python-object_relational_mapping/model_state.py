#!/usr/bin/python3
"""
Create simple table using sqlAlchmey
"""
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
