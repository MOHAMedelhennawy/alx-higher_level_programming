#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter 'a' from the database hbtn_0e_6_usa
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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id).all()
              )

    for state in states:
        print("{}: {}".format(state.id, state.name))
