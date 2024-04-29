#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/my_db5') # to connect with DB
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    # addresses = relationship("Address", back_populates="user", uselist=False)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="addresses")
    # user = relationship("User", back_populates="address")

Base.metadata.create_all(engine)

# names = ["Ali", "Khaled", "Mohammed", "Mahmoud", "Ahmed", "Jihan", "Roaa", "Ibrahem"]
# for i in range(20):
#     name_ = random.choice(names)
#     email_ = name_ + str(random.randrange(1, 100000)) + '@gmail.com'
#     new_user = User(name=name_)
#     new_address = Address(email=email_, user=new_user)
#     session.add(new_user)
#     session.add(new_address)
#     session.commit()


user = session.query(User).filter(User.name == 'Roaa').first()
print(f"name: {user.name}, id: {user.id}")