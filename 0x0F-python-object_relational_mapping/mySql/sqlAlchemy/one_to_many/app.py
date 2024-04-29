#!/usr/bin/python3

from models import User, Post, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

u1 = User(name="Alaa")
session.add(u1)
# u1 = session.query(Post).all()
posts = ["Learn sqlalchemy", "Learn python", "Learn flask", "Learn c"]

for p in posts:
    new_post = Post(post_body=p, user=u1)
    session.add(new_post)
    session.commit()
