from companyDB.models import Employee,Project,Department
from flask import Flask, render_template,flash,redirect,url_for
from companyDB.forms import addEmployeeForm, addProjectForm
from companyDB import app,db

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/add_employees",methods=['POST','GET'])
def add_employees():
    form=addEmployeeForm()
    if form.validate_on_submit():
        employee_instance = Employee(
            fname=form_instance.fname.data,
            minit=form_instance.minit.data,
            lname=form_instance.lname.data,
            ssn=form_instance.ssn.data,
            bdate=form_instance.bdate.data,
            address=form_instance.address.data,
            sex=form_instance.sex.data,
            salary=form_instance.salary.data,
            superSsn=form_instance.superSsn.data,
            dno=form_instance.dno.data
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
            pname=form_instance.pname.data,
            pnumber=form_instance.pnumber.data,
            plocation=form_instance.plocation.data,
            dnum=form_instance.dnum.data
        )
        db.session.add(project_instance)
        db.session.commit()
        flash(f'Work Alert : {form.pname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_project.html', title='add project', form=form)

