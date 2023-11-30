from models import Employee,Project,Department

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/add_employees",methods=['POST','GET'])
def add_employees():
    form=addEmployeeForm()
    if form.validate_on_submit():
        flash(f'Welcome Aboard {form.fname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_employee.html',title='add employee',form=form)


@app.route("/add_projects",methods=['POST','GET'])
def add_projects():
    form=addProjectForm()
    if form.validate_on_submit():
        flash(f'Work Alert : {form.pname.data.upper()}!','success')
        return redirect(url_for('home'))
    return render_template('add_project.html', title='add project', form=form)

