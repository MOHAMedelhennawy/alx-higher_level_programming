#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table

engine = create_engine('mysql+pymysql://root:root@localhost:3306/my_db11') # to connect with DB

Base = declarative_base()


# This association table using sqlalchemy core
broup_user = Table(
    "group_users",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True)
)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    groups = relationship("Group", secondary=broup_user, back_populates='users')
    def __repr__(self):
        return f"user {self.name} with id: {self.id}"

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(20))
    users = relationship("User", secondary=broup_user, back_populates='groups')
    def __repr__(self):
        return f"This profile with id: {self.id} it's owned by {self.user_id}"

Base.metadata.create_all(engine)

