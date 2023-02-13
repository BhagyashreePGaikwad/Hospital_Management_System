from __init__ import db
import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, date

class Userstore(db.Model):
    __tablename__ = 'userstore'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20))
    password = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default=datetime.now)

class Patients(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    ssn_id = db.Column(db.Integer)
    pname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now)
    ldate = db.Column(db.DateTime, default=datetime.now)
    tbed = db.Column(db.String(10))
    address = db.Column(db.String(20))
    city = db.Column(db.String(20))
    state = db.Column(db.String(20))
    status = db.Column(db.String(20))

  

class Medicines(db.Model):
    __tablename__ = 'medicines'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    mname = Column(db.String(20))
    mid = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    qissued = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now)

    children = relationship("MedicineMaster")

class MedicineMaster(db.Model):
    __tablename__ = 'medicinemaster'
    mid = Column(Integer, ForeignKey('medicines.mid'), primary_key=True)
    mname = Column(db.String(20))
    qavailable = Column(db.Integer)
    rate = Column(db.Integer)

class Diagnostics(db.Model):
    __tablename__ = 'diagnostics'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    tname = Column(db.String(20))
    tid = db.Column(db.Integer)
    tcharge = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now)

    children = relationship("DiagnosticsMaster")

class DiagnosticsMaster(db.Model):
    __tablename__ = 'diagnosticsmaster'
    tid = Column(Integer, ForeignKey('diagnostics.tid'), primary_key=True)
    tname = Column(db.String(20))
    tcharge = Column(db.Integer)

