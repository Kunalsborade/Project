from app import Employee, db
from process.response.producer import produce_response
import logging
import json

logger = logging.getLogger('EmployeeController')
logger.setLevel(logging.INFO)

def send_response(employee, message):
    logger.info("IN send_response Function")
    # response = {"message": message}
    response = {
                "message": message,
                "employee": {
                    "id": employee.id,
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "email": employee.email,
                    "number": employee.number
                }
            }
    # response = json.dumps(response)
    produce_response(response)
    
def create_employee(data):
    try:
        logger.info("IN create_employee Function")
        insert_employee = Employee(
            first_name=data["firstname"],
            last_name=data["lastname"],
            email=data["email"],
            number=data["number"]
        )
        db.session.add(insert_employee)
        db.session.commit()
        employee = Employee.query.filter_by(first_name=data["firstname"]).first()
        messaage = "Employee Created successfully"
        send_response(employee,messaage)
        # produce_response(messaage)
    except Exception as e:
        logger.error(f"Error creating employee: {e}")
    
def get_employee(id):
    try:
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
                produce_response(employee_data)
        else:
            logger.error("Invalid employee ID")
    except Exception as e:
        logger.error(f"Error getting employee: {e}")

def update_employee(data, id):
    try:
        logger.info("In Update function")
        logger.info(f"ID: {id}")

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

                updated_employee = Employee.query.get(id)

                messaage = "Employee updated successfully"
                send_response(updated_employee, messaage)
            else:
                logger.error("Employee not found")
        else:
            logger.error("Invalid employee ID")
    except Exception as e:
        logger.error(f"Error updating employee: {e}")

def delete_employee(id):
    try:
        if id is not None:
            employee = Employee.query.get(id)
            if employee:
                db.session.delete(employee)
                db.session.commit()
                response = {
                    "message": "Employee deleted successfully",
                    "id": id
                }
                produce_response(response)
            else:
                logger.error("Employee not found")
        else:
            logger.error("Invalid employee ID")
    except Exception as e:
        logger.error(f"Error deleting employee: {e}")




# def create_employee(data):
#     insert_employee = Employee(
#         first_name = data["firstname"], 
#         last_name = data["lastname"],
#         email = data["email"],
#         number = data["number"] 
#     )
#     db.session.add(insert_employee)
#     db.session.commit()
#     # employee = Employee.query.filter_by(data["firstname"]).first()
#     employee = Employee.query.filter_by(first_name=data["firstname"]).first()
#     response = {
#         "message" : "Employee Created successfully",
#         "id" : employee.id
#     }
#     produce_response(response)

    
# def get_employee(id):
#     if id is not None:
#         employee = Employee.query.get(id)
#         if employee:
#             employee_data = {
#                 "id": employee.id,
#                 "first_name": employee.first_name,
#                 "last_name": employee.last_name,
#                 "email": employee.email,
#                 "number": employee.number
#             }
#             produce_response(employee_data)

# def update_employee(data, id):
#     print("In Update function")
#     print("ID", id)
    
#     if id is not None:
#         employee = Employee.query.get(id)
#         if employee:
#             if "firstname" in data:
#                 employee.first_name = data["firstname"]
#             if "lastname" in data:
#                 employee.last_name = data["lastname"]
#             if "email" in data:
#                 employee.email = data["email"]
#             if "number" in data:
#                 employee.number = data["number"]     
#             db.session.commit()
#             response = {
#                 "message" : "Employee updated successfully",
#                 "id" : employee.id
#             }
#             produce_response(response)
    
# def delete_employee(data):
#     employee_id = data.get("employee_id")
#     if employee_id is not None:
#         employee = Employee.query.get(employee_id)
#         if employee:
#             db.session.delete(employee)
#             db.session.commit()
#             response = {
#                 "message" : "Employee Deleted successfully",
#                 "id" : employee.id
#             }
#             produce_response(response)


