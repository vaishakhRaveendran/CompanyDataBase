from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/add_employee")
def add_employee():
    return render_template("add_employee.html")

@app.route("/home_page")
def home_page():
    return render_template("home_page.html")

@app.route("/add_project")
def add_project():
    return render_template("add_project.html")

if __name__ == '__main__':
    app.run(debug=True)
