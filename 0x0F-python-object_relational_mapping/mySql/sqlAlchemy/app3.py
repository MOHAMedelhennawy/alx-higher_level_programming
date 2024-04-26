#!/usr/bin/python3

import random
from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)

session = Session()

users_all = session.query(User).all()
print("Number of all users: ", len(users_all))

#       SQL command: SELECT * FROM users WHERE age >= 25 AND name == 'Mahmoud';
# you can use 'where' using the same syntax but replace 'filter' with 'where'
filtered_users = session.query(User).filter(User.age >= 25, User.name == 'Mahmoud').all()
print("Number of users those age greater that 25: ", len(filtered_users))

for user in filtered_users:
    print(user)

#       SQL command: SELECT * FROM users WHERE age = 22;
# note that 'filter_by' don't support complex filtering like >=, <=, !=
# just filter and where do
filtered_users = session.query(User).filter_by(age=22).all()
print("Number of users those age greater that 25: ", len(filtered_users))

for user in filtered_users:
    print(user)

# ==========================================================================================
print("-" * 100)

# What about you need to use 'or', 'and' condations?
print("Using and_:")
filtered_users = session.query(User).filter(and_(User.age >= 25, User.name == 'Mahmoud')).all()
for user in filtered_users:
    print(user)

# using the same code but different syntax:
print("Using &: ")
filtered_users = session.query(User).filter((User.age >= 25) & (User.name == 'Mahmoud')).all()
for user in filtered_users:
    print(user)


# ==========================================================================================
print("-" * 100)

# You can use not_:
filtered_users = session.query(User).filter(not_(User.age >= 25) & (User.name == 'Mahmoud')).all()
for user in filtered_users:
    print(user)

# ==========================================================================================
print("-" * 100)

filtered_users = (
    session.query(User).filter(
        or_(
            not_(User.name == 'ٌRoaa'),
            and_(
                User.age > 25,
                User.age < 50
                )
        )
    )
)

# print(len(filtered_users))
for user in filtered_users:
    print(user)
