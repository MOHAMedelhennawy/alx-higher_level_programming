#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
format: <city id>: <city name> -> <state name>
"""
from relationship_state import Base, State
from relationship_city import City
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

    all_cities = session.query(City, State).where(City.state_id == State.id)
    for city, state in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
