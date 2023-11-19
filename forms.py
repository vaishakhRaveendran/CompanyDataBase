from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

#AddEmployee forms will be created as class which inherits the FlaskForm class.
#The first argument is name of the field and it will be used as the label in the html
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
    submit = SubmitField('Add')

class addProjectForm(FlaskForm):
    pname = StringField('Project Name', validators=[DataRequired(), Length(max=30)])
    pnumber = IntegerField('Project Number', validators=[DataRequired()])
    plocation = StringField('Project Location', validators=[Length(max=30)])
    dnum = IntegerField('Department Number', validators=[DataRequired()])
    submit = SubmitField('Add Project')