#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
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

    filtered_cities = (
        session.query(City)
        .join(State).
        filter(City.state_id == State.id)
        )
    for city in filtered_cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
