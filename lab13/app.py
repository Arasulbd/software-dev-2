from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/DemoDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

# Define the UserLogin model
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(100), unique=True, nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Successfully requested. Entered password = ' + request.form['password']
    
    name = "Rasul"
    checkfruit = "kiwi"
    fruits = ['Apple', 'orange', 'mango']
    
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']

            existing_employee = Employee.query.filter_by(employee_name=emp_name).first()
            existing_id = Employee.query.filter_by(employee_id=emp_id).first()

            if existing_employee:
                flash(f"Employee with name '{emp_name}' already exists.")
            if existing_id:
                flash(f"Employee ID '{emp_id}' already exists.")
            if not existing_employee and not existing_id:
                new_employee = Employee(employee_id=emp_id, employee_name=emp_name)
                session['employee1'] = new_employee.employee_name
                db.session.add(new_employee)
                db.session.commit()
                flash(f"{emp_name} successfully added!")
        except:
            flash("Failed to insert data. Try again.")
    
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
