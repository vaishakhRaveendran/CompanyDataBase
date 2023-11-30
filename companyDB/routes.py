from companyDB.models import Employee,Project,Department
from flask import Flask, render_template,flash,redirect,url_for
from companyDB.forms import addEmployeeForm, addProjectForm
from companyDB import app,db

@app.route("/")
@app.route("/home")
def home():
    employees = Employee.query.all()
    departments = Department.query.all()
    projects=Project.query.all()
    return render_template('home.html',employees=employees,departments=departments,projects=projects)

@app.route("/add_employees",methods=['POST','GET'])
def add_employees():
    form=addEmployeeForm()
    if form.validate_on_submit():
        employee_instance = Employee(
            fname=form.fname.data,
            minit=form.minit.data,
            lname=form.lname.data,
            ssn=form.ssn.data,
            bdate=form.bdate.data,
            address=form.address.data,
            sex=form.sex.data,
            salary=form.salary.data,
            superSsn=form.super_ssn.data,
            dno=form.dno.data
        )
        db.session.add(employee_instance)
        db.session.commit()
        flash(f'Welcome Aboard {form.fname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_employee.html',title='add employee',form=form)


@app.route("/add_projects",methods=['POST','GET'])
def add_projects():
    form=addProjectForm()
    if form.validate_on_submit():
        project_instance = Project(
            pname=form.pname.data,
            pnumber=form.pnumber.data,
            plocation=form.plocation.data,
            dnum=form.dnum.data
        )
        db.session.add(project_instance)
        db.session.commit()
        flash(f'Work Alert : {form.pname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_project.html', title='add project', form=form)

