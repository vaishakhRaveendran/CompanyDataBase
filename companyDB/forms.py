from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length



class addEmployeeForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Length(min=3,max=30)])
    minit = StringField('Middle Initial', validators=[Length(max=20)])
    lname = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    ssn = IntegerField('Social Security Number', validators=[DataRequired()])
    bdate = DateField('Birthdate', validators=[DataRequired()])
    address = StringField('Address', validators=[Length(max=60)])
    sex = SelectField('Sex', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    dno = IntegerField('Department Number',default=1,validators=[DataRequired()])
    super_ssn = IntegerField('Supervisor SSN',default=123456009)
#submit field will send back info back to us.
    submit = SubmitField('ADD')

class addProjectForm(FlaskForm):
    pname = StringField('Project Name', validators=[DataRequired(), Length(max=30)])
    pnumber = IntegerField('Project Number', validators=[DataRequired()])
    plocation = StringField('Project Location', validators=[Length(max=30)])
    dnum = IntegerField('Department Number', validators=[DataRequired()])
    submit = SubmitField('ADD')

class addSkill(FlaskForm):
    employeeSsn = SelectField('Employee SSN', coerce=str,validators=[DataRequired()])
    stackId = SelectField('Stack ID', coerce=int, validators=[DataRequired()])
    submit = SubmitField('ADD')

class addStacks(FlaskForm):
    stack = StringField('Stack', validators=[DataRequired()])
    id = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('ADD')


class viewProfile(FlaskForm):
    employeeSsn = SelectField('Employee SSN', coerce=str, validators=[DataRequired()])
    submit = SubmitField('SUBMIT')

class removeForm(FlaskForm):
    entity_type = SelectField('Select Entity Type', choices=[('project', 'Project'), ('employee', 'Employee')])
    entity_id = StringField('Entity ID')
    confirmation = StringField('Type "DELETE" to confirm', validators=[validators.DataRequired(), validators.EqualTo('DELETE', message='Confirmation mismatch')])
    delete_button = SubmitField('Remove')