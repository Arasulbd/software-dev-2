"""
NAME=Aminur Rasul
Lab13: FLASK application
"""
from flask import Flask, render_template , redirect,url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

"""creat an object "app" from the FLASK module
__name__set to__main__if the script is running directly from the main file
"""
app=Flask(__name__)
# connection to postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/DemoDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create an object db
db=SQLAlchemy(app)

# define a model (create table in the demodb database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), nullable=False)

    #Define an employee model
class Employee(db.model):
    id=db.Column(db.Integer, primary_key=True)
    

# set the routing to main page
#'route' decorator use to access the root url
@app.route('/', method=['GET', 'POST'])
def index():
    if request.method=='POST':
        return 'Successfully requested Enter password=' +request.form['password']
    name = "Rasul"
    checkfruit="kiwi"
    fruits=['Apple', 'orange','mango']
    return render_template('index.html', username=name, listfruits=fruits,checkfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', method=['GET', 'POST'])
def users():
    if request.method=='POST':
        form=request.form
        emp_name=form['employee_name']
        emp_id=form['employee_id']

        existing_employee=Employee.query.filter_by(employee_name=emp_name).first() #bollean (treue, false)
        existing_id=Employee.query.filter_by(emp_id=emp_id).first()#boolean true and falsr

        if existing_employee :
            flash(f"Employee wiht name '{emp_name} already exists")
        if existing_id :
            flash(f"Employee id '{emp_id} already exists")
        
        # create new employee object
        new_employee=Employee(employee_id=emp_id,employee_name=emp_name)
        #
        session['employee']= new_employee.employee_name
        # add the new object to database
        db.session.add(new_employee)
        db.session.commit()
        #messege
        flash request.form[employee_name] + 'successfully added!'
    except:
    flash("Fail to insert data Try again" )

    return render_template('users.html')

@app.route('/quotes')
def quotes():

    return redirect(url_for('index.html'))

# set tbe 'app' to run if you excute the file directory( not when it is imported)
if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True, port=8000)

    
    