#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/my_db') # to connect with DB

base = declarative_base() # return a class to inherit to table class
class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    age = Column(Integer)

    def __str__(self):
        return f'user_{self.id}: my name is {self.name}, i {self.age} years old'

base.metadata.create_all(engine) # This command to execute the class and create the table in DB