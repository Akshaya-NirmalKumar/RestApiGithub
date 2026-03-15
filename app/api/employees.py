from flask import Blueprint, request, jsonify
from uuid import uuid4
from app.services.employee_service import EmployeeService
from app.repositories.employee_repository import EmployeeRepository

# Define the blueprint
employees_bp = Blueprint('employees', __name__, url_prefix='/api/v1/employees')

# Initialize service (In a real app, use Dependency Injection)
emp_repo = EmployeeRepository()
emp_service = EmployeeService(emp_repo)

@employees_bp.route('', methods=['GET'])
def get_all():
    employees = emp_service.get_all_employees()
    return jsonify([e.__dict__ for e in employees]), 200

@employees_bp.route('/<emp_id>', methods=['GET'])
def get_one(emp_id):
    emp = emp_service.get_employee_by_id(emp_id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(emp.__dict__), 200

@employees_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    try:
        new_emp = emp_service.create_employee(data)
        return jsonify({"message": "Employee created", "employee": new_emp.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@employees_bp.route('/<emp_id>', methods=['PUT'])
def update(emp_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    updated = emp_service.update_employee(emp_id, data)
    if not updated:
        return jsonify({"error": "Employee not found"}), 404
        
    return jsonify({"message": "Employee updated", "employee": updated.__dict__}), 200

@employees_bp.route('/<emp_id>', methods=['DELETE'])
def delete(emp_id):
    success = emp_service.delete_employee(emp_id)
    if not success:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"message": "Employee deleted"}), 200