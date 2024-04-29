#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa,
Results must be display as they are in the example below:
(<state name>: (<city id>) <city name>)
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
        session.query(City, State)
        .filter(City.state_id == State.id)
        )

    for city, state in filtered_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
