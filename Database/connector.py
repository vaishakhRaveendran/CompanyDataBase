import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database='employeemanagement',
    password='l@xmi2421'
)
dbCursor = mydb.cursor()


if __name__ == '__main__':
    app.run(debug=True)