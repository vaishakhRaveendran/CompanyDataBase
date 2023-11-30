from flask import Flask, render_template,flash,redirect,url_for
from forms import addEmployeeForm, addProjectForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba3090250e17faed336ea51e083266e0'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)