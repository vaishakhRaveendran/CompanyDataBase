from flask import Flask, redirect, url_for, render_template
from forms import addEmployeeForm,addProjectForm

app = Flask(__name__)

@app.route("/add_employee")
def add_employee():
    form=addEmployeeForm()
    return render_template("add_employee.html",form=form)

@app.route("/home_page")
def home_page():
    return render_template("home_page.html")

@app.route("/add_project")
def add_project():
    return render_template("add_project.html")

if __name__ == '__main__':
    app.run(debug=True)
