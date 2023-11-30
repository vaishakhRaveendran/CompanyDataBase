from companyDB import db
from datetime import datetime
class Employee(db.Model):
    __tablename__ = 'employees'

    fname = db.Column(db.String(30), nullable=False)
    minit = db.Column(db.String(20))
    lname = db.Column(db.String(30), nullable=False)
    ssn = db.Column(db.Integer, primary_key=True)
    bdate = db.Column(db.Date)
    address = db.Column(db.String(60))
    sex = db.Column(db.String(5))
    salary = db.Column(db.Integer)
    superSsn = db.Column(db.Integer, db.ForeignKey('employees.ssn', ondelete='SET NULL'))
    dno = db.Column(db.Integer, db.ForeignKey('departments.dnumber', ondelete='SET DEFAULT'))

    def __repr__(self):
        return f"Employee('{self.fname}', '{self.ssn}')"

class Project(db.Model):
    __tablename__ = 'projects'

    pname = db.Column(db.String(30), nullable=False)
    pnumber = db.Column(db.Integer, primary_key=True)
    plocation = db.Column(db.String(30))
    dnum = db.Column(db.Integer, db.ForeignKey('departments.dnumber', onupdate='CASCADE'), nullable=False)
    department = db.relationship('Department')

    def __repr__(self):
        return f"Project('{self.pname}', '{self.pnumber}')"

class Department(db.Model):
    __tablename__ = 'departments'

    dnumber = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(40), nullable=False, unique=True)
    mgrSsn = db.Column(db.Integer, default=133557799)
    mgrStartDate = db.Column(db.Date,default=datetime.utcnow().date())

    def __repr__(self):
        return f"Department('{self.dname}', '{self.dnumber}')"
