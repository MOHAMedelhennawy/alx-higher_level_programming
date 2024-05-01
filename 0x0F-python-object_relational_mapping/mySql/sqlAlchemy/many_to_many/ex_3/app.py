#!/usr/bin/python3

from models import Appointment, Doctor, Patient, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
Session = sessionmaker(bind=engine)
session = Session()

# dr_smith = Doctor(name="Dr. Smith", specialty="Cardiology")
# mohamed_elhe = Patient(name="Mohammed Elhennawy", dob=datetime(2002, 2, 2))
# appointment = Appointment(doctor=dr_smith, patient=mohamed_elhe)

# dr_aboura = Doctor(name="Dr. Aboura", specialty="Cardiology")
# mohamed_ramia = Patient(name="Mohammed Ramia", dob=datetime(2002, 2, 2))
# appointment = Appointment(doctor=dr_aboura, patient=mohamed_ramia)

# session.add([appointment,mohamed_ramia, dr_aboura])
# # session.commit()

# Find all appointments for Dr. Smith
appointments_for_dr_smith = session.query(Appointment).filter(Appointment.doctor.has(name='Dr. Smith')).all()
print("Dr. Smith's appointments")
print(appointments_for_dr_smith)

# Find all appointments for John Doe
appointments_for_john_doe = session.query(Appointment).filter(Appointment.patient.has(name='Mohammed Elhennawy')).all()

print("John Doe's appointments")
print(appointments_for_john_doe)