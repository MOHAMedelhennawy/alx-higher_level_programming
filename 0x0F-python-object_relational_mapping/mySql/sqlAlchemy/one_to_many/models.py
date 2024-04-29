#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/my_db2') # to connect with DB

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    post = relationship("Post", back_populates='user',
                        cascade='all, delete, save-update')

    def __repr__(self):
        return f"user {self.name} with id: {self.id}"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    post_body = Column(String(640))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship("User", back_populates="post")
    def __repr__(self):
        return f"<Post>: {self.post_body}"
# Base.metadata.create_all(engine)

