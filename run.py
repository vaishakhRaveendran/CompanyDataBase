from flask import Flask, render_template,flash,redirect,url_for
from forms import addEmployeeForm, addProjectForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba3090250e17faed336ea51e083266e0'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:l@xmi2421@localhost/employeemanagement'
db = SQLAlchemy(app)

class Employee(db.Model):
    fname = db.Column(db.String(30), nullable=False)
    minit = db.Column(db.String(20))
    lname = db.Column(db.String(30), nullable=False)
    ssn = db.Column(db.Integer, primary_key=True)
    bdate = db.Column(db.Date)
    address = db.Column(db.String(60))
    sex = db.Column(db.String(5))
    salary = db.Column(db.Integer)
    superSsn = db.Column(db.Integer, db.ForeignKey('Employee.ssn', ondelete='SET NULL'))
    dno = db.Column(db.Integer, nullable=False, default=1)
    supervisor = db.relationship('employee', remote_side=[ssn])

    def __repr__(self):
        return f"Employee('{self.fname}','{self.ssn}')"


class Project(db.Model):
    pname = db.Column(db.String(30), nullable=False)
    pnumber = db.Column(db.Integer, primary_key=True)
    plocation = db.Column(db.String(30))
    dnum = db.Column(db.Integer, nullable=False,default=1)
    def __repr__(self):
        return f"Project('{self.pname}','{self.pnumber}')"


class Department(db.Model):
    dnumber = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(40), nullable=False, unique=True)
    mgrSsn = db.Column(db.Integer, default=133557799)
    mgrStartDate = db.Column(db.Date)
    employees = db.relationship('Employee', back_populates='department')
    projects = db.relationship('Project', back_populates='department')

    def __repr__(self):
        return f"Department('{self.dname}', '{self.dnumber}')"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/add_employees",methods=['POST','GET'])
def add_employees():
    form=addEmployeeForm()
    if form.validate_on_submit():
        flash(f'Welcome Aboard {form.fname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_employee.html',title='add employee',form=form)


@app.route("/add_projects",methods=['POST','GET'])
def add_projects():
    form=addProjectForm()
    if form.validate_on_submit():
        flash(f'Work Alert : {form.pname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_project.html', title='add project', form=form)


if __name__ == '__main__':
    app.run(debug=True)
