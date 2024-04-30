#!/usr/bin/python3
"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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

    all_state = session.query(State)
    for state in all_state:
        print("{}: {}".format(state.id, state.name))
        for city in session.query(City).join(State).where(City.state_id == state.id):
            print("\t{}: {}".format(city.id, city.name))