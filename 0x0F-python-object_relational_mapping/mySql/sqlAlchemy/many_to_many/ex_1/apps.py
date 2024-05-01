#!/usr/bin/python3

from models import User, Group ,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# session.add_all([
#     User(username="mohamed"),
#     User(username="Ali"),
#     User(username="Mona"),
#     User(username="shimaa"),]
# )

# session.add_all([
#     Group(group_name="C_lovers"),
#     Group(group_name="Python_is_fun"),
#     Group(group_name="Javascript_Horrible"),
#     Group(group_name="Django-tutorial")
#     ]
# )

u1 = session.query(User).filter_by(id=1).first()
u2 = session.query(User).filter_by(id=2).first()
u3 = session.query(User).filter_by(id=3).first()

g1 = session.query(Group).filter_by(id=1).first()
g2 = session.query(Group).filter_by(id=2).first()
g3 = session.query(Group).filter_by(id=3).first()

u1.groups.append(g3)
session.commit()