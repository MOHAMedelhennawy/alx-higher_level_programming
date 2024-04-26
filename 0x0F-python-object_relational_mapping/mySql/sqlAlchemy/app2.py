#!/usr/bin/python3

import random
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

#           This code to add random users
# names = ["Ali", "Khaled", "Mohammed", "Mahmoud", "Ahmed", "Jihan", "Roaa", "Ibrahem"]
# ages = [43, 12, 2, 52, 66, 21, 6]

# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)

# session.commit()


#           now, i need to query all users ordered by age, and name:
#           "SELECT * FROM users OREDER BY age, name"
users = session.query(User).order_by(User.age.desc(), User.name).all() # .desc: to query in descending order
for user in users:
    print(user)
