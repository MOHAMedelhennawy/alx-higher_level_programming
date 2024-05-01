#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table

engine = create_engine('mysql+pymysql://root:root@localhost:3306/coursera') # to connect with DB

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Association table using ORM
class StudentCourse(Base):
    __tablename__ = 'student_course'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column('course_id', Integer, ForeignKey('courses.id'))

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    courses = relationship("Course", secondary="student_course", back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    students = relationship("Student", secondary="student_course", back_populates="courses")

Base.metadata.create_all(engine)