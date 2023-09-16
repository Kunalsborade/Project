from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from process.response.producer import produce_responce

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://kunal:kbpassword@localhost:5432/mydatabase'

db = SQLAlchemy(app)
app.app_context().push()

topic = 'employee'

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('firstname',db.String(50))
    last_name = db.Column('lastname', db.String(50))
    email = db.Column('email', db.String(120), unique=True)
    number = db.Column('number', db.String(120))
    
    def __init__(self, first_name, last_name, email, number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
    
    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
    
def create(data):
    insert_employee = Employee(
        first_name = data["firstname"], 
        last_name = data["lastname"],
        email = data["email"],
        number = data["number"] 
    )
    db.session.add(insert_employee)
    db.session.commit()
    employee = get_employee_id(data["firstname"])
    produce_responce(employee)

    
def get_employee_id(firstname):
    employee = Employee.query.filter_by(first_name=firstname).first()
    print(employee)
    if employee:
        return employee.id
    else:
        return None
