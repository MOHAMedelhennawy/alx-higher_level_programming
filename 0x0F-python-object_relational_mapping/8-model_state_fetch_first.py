#!/usr/bin/python3
"""
script that lists first State objects from the database hbtn_0e_6_usa
using sqlalchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3])
                        )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    print(state.id, state.name, sep=': ')
