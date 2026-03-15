from flask import Blueprint, request, jsonify
from app.services.department_service import DepartmentService
from app.repositories.department_repository import DepartmentRepository

# Define the blueprint with the correct URL prefix
departments_bp = Blueprint('departments', __name__, url_prefix='/api/v1/departments')

# Initialize repository and service
dept_repo = DepartmentRepository()
dept_service = DepartmentService(dept_repo)

@departments_bp.route('', methods=['GET'])
def get_all():
    depts = dept_service.get_all_departments()
    return jsonify([d.__dict__ for d in depts]), 200

@departments_bp.route('/<dept_id>', methods=['GET'])
def get_one(dept_id):
    dept = dept_service.get_department_by_id(dept_id)
    if not dept:
        return jsonify({"error": "Department not found"}), 404
    return jsonify(dept.__dict__), 200

@departments_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    try:
        new_dept = dept_service.create_department(data)
        # Fixed typo here: was 'de', now 'department'
        return jsonify({"message": "Department created", "department": new_dept.__dict__}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@departments_bp.route('/<dept_id>', methods=['PUT'])
def update(dept_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    updated = dept_service.update_department(dept_id, data)
    if not updated:
        return jsonify({"error": "Department not found"}), 404
        
    return jsonify({"message": "Department updated", "department": updated.__dict__}), 200

@departments_bp.route('/<dept_id>', methods=['DELETE'])
def delete(dept_id):
    success = dept_service.delete_department(dept_id)
    if not success:
        return jsonify({"error": "Department not found"}), 404
    return jsonify({"message": "Department deleted"}), 200