#!/usr/bin/python3
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, Date
from datetime import datetime

engine = create_engine('mysql+pymysql://root:root@localhost:3306/medical') # to connect with DB

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Association table using ORM

class Appointment(Base):
    __tablename__ = 'Appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_date = Column(Date, default=datetime.utcnow)

    doctor = relationship("Doctor", backref='Appointments')
    patient = relationship("Patient", backref='Appointments')

    def __repr__(self):
        return f"<Appointment on {self.appointment_date}>"


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    specialty = Column(String(50))


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    dob = Column(Date)

Base.metadata.create_all(engine)