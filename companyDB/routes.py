from companyDB.models import Employee,Project,Department,Skill,Stack
from flask import Flask, render_template,flash,redirect,url_for,request
from companyDB.forms import addEmployeeForm, addProjectForm,addSkill,viewProfile,removeForm
from companyDB import app,db
from sqlalchemy.orm import aliased

@app.route("/")
@app.route("/home")
def home():
    employees = Employee.query.all()
    departments = Department.query.all()
    projects=Project.query.all()
    return render_template('home.html',employees=employees,departments=departments,projects=projects)

@app.route("/add_skill",methods=['POST','GET'])
def add_skill():
    form = addSkill()
    stacks = Stack.query.all()
    employees = Employee.query.all()
    form.stackId.choices = [(stack.id, stack.stack) for stack in stacks]
    form.employeeSsn.choices = [(employee.ssn,f'{employee.fname} {employee.lname}') for employee in employees]
    if form.validate_on_submit():
        skill_instance = Skill(
            employeeSsn = form.employeeSsn.data,
            stackId = form.stackId.data
        )
        db.session.add(skill_instance)
        db.session.commit()
        flash(f'New Skill Unlocked !', 'success')
        return redirect(url_for('view_profile'))
    return render_template('add_skill.html', title='add skill', form=form)


@app.route('/view_profile', methods=['GET', 'POST'])
def view_profile():
    form = viewProfile(request.form)
    employees = Employee.query.all()
    form.employeeSsn.choices = [(employee.ssn, f'{employee.fname} {employee.lname}') for employee in employees]
    if request.method == 'POST' and form.validate():
        employee_ssn = form.employeeSsn.data
        stacks_alias = aliased(Stack)
        profiles = (
            db.session.query(Skill.employeeSsn, stacks_alias.stack, Skill.stackId)
            .join(stacks_alias, Skill.stackId == stacks_alias.id)
            .filter(Skill.employeeSsn == employee_ssn)
            .all()
        )
        return render_template('view_profile.html', form=form, profiles=profiles)

    return render_template('view_profile.html', form=form)




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





@app.route('/remove_entity', methods=['GET', 'POST'])
def remove_entity():
    form = removeForm()

    if form.validate_on_submit():
        if form.confirmation.data.upper() == 'DELETE':
            entity_type = form.entity_type.data
            entity_id = form.entity_id.data

            if entity_type == 'employee':
                employee_to_delete = Employee.query.filter_by(ssn=entity_id).first()
                if employee_to_delete:
                    db.session.delete(employee_to_delete)
                    db.session.commit()
                    flash('Employee deleted successfully!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Employee not found.', 'danger')
                    return redirect(url_for('home'))

            elif entity_type == 'project':
                project_to_delete = Project.query.filter_by(pnumber=entity_id).first()
                if project_to_delete:
                    db.session.delete(project_to_delete)
                    db.session.commit()

                    flash('Project deleted successfully!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Project not found.', 'danger')
                    return redirect(url_for('home'))
    return render_template('remove_entity.html', form=form)