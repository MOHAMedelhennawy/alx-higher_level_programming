#!/usr/bin/python3

from models import Student, Course ,engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# math = Course(title="Mathematics")
# physics = Course(title="physics")

# khalid = Student(name="Khalid", courses=[math, physics])
# john = Student(name="John", courses=[math])
# session.add_all([khalid, john])


student = session.query(Student).first()
courses = [course.title for course in student.courses]
print(f"{student.name} courses: {', '.join(courses)}")
session.commit()