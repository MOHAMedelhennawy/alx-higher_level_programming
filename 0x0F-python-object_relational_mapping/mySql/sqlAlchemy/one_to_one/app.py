#!/usr/bin/python3

from models import User, Profile, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

p1 = Profile(first_name="saied2", last_name="seka2")
u1 = User(name="seka2", password='4324', profile=p1)

# print(u1)
# print(u1.profile)
# print(u1.profile.first_name)
# print(u1.profile.user_id)
# print(type(u1.profile))
# print(type(u1.profile.user_id))

u1 = session.query(Profile).filter(Profile.user_id == None).first()
session.delete(u1)
# session.add(u1)
session.commit()

all_users = session.query(User).join(Profile).all()
for u in all_users:
    print(u)