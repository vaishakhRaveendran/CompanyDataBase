from flask import Flask, render_template
from forms import addEmployeeForm, addProjectForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba3090250e17faed336ea51e083266e0'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/add_employees")
def add_employees():
    form=addEmployeeForm()
    return render_template('add_employee.html',title='add employee',form=form)

if __name__ == '__main__':
    app.run(debug=True)
