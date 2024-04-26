#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user1 = User(name="Ahmed Elhennawy", age=22)
user2 = User(name="khaled elkelany", age=22)
user3 = User(name="Mohammed Ramia", age=22)
user4 = User(name="Ahmed ghazy", age=22)


#           To add columns to DB
# session.add(user1) -- to add one user
# session.add_all([user1, user2, user3, user4]) # to add multibull users
# session.commit()


#           To read from DB
# -1
# users = session.query(User).all()
# print(users)
# for user in users:
#     print(user)

# -2: return all users that have id = 1
# users = session.query(User).filter_by(id=1).all()

# -3: return only in case nothing matches, otherwise 'Error' is happen
# users = session.query(User).filter_by(id=1).one_or_none()

# -4: return just the first user that has id = 1
# users = session.query(User).filter_by(id=1).first()
# print(users)



#               how to update
# user = session.query(User).filter_by(id=1).one_or_none()
# user.name = "A different name"
# session.commit()

#               how to delete
user = session.query(User).filter_by(id=1).one_or_none()
session.delete(user)
session.commit()