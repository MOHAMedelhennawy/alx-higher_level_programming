#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/my_db') # to connect with DB

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    profile = relationship("Profile", backref='user', uselist=False, cascade='all, delete, save-update')

    def __repr__(self):
        return f"user {self.name} with id: {self.id}"

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, onupdate='CASCADE') # Define the foreign key relationship

    def __repr__(self):
        return f"This profile with id: {self.id} it's owned by {self.user_id}"

# Base.metadata.create_all(engine)

