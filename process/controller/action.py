from app import Employee, db
from process.response.producer import produce_responce

def create(data):
    insert_employee = Employee(
        first_name = data["firstname"], 
        last_name = data["lastname"],
        email = data["email"],
        number = data["number"] 
    )
    db.session.add(insert_employee)
    db.session.commit()
    # employee = Employee.query.filter_by(data["firstname"]).first()
    employee = Employee.query.filter_by(first_name=data["firstname"]).first()
    response = {
        "message" : "Employee Created successfully",
        "id" : employee.id
    }
    produce_responce(response)

    
def get(id):
    if id is not None:
        employee = Employee.query.get(id)
        if employee:
            employee_data = {
                "id": employee.id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "email": employee.email,
                "number": employee.number
            }
            produce_responce(employee_data)

def update(data, id):
    print("In Update function")
    print("ID", id)
    
    if id is not None:
        employee = Employee.query.get(id)
        if employee:
            if "firstname" in data:
                employee.first_name = data["firstname"]
            if "lastname" in data:
                employee.last_name = data["lastname"]
            if "email" in data:
                employee.email = data["email"]
            if "number" in data:
                employee.number = data["number"]     
            db.session.commit()
            response = {
                "message" : "Employee updated successfully",
                "id" : employee.id
            }
            produce_responce(response)
    
def delete(data):
    employee_id = data.get("employee_id")
    if employee_id is not None:
        employee = Employee.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            response = {
                "message" : "Employee Deleted successfully",
                "id" : employee.id
            }
            produce_responce(response)


def delete(id):
    if id is not None:
        employee = Employee.query.get(id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            response =  {
                "message": "Employee deleted successfully",
                "id": id
            }
            produce_responce(response)
    
