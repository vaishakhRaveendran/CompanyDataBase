from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba3090250e17faed336ea51e083266e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:l%40xmi2421@localhost/employeemanagement'
db = SQLAlchemy(app)

from companyDB import routes