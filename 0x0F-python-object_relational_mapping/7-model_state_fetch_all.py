#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
using sqlalchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))

Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()
for state in states:
    print(f"{state.id}: {state.name}")
