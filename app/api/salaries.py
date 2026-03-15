from flask import Blueprint, request, jsonify
from app.services.salary_service import SalaryService
from app.repositories.salary_repository import SalaryRepository

# Define the blueprint with the correct URL prefix
salaries_bp = Blueprint('salaries', __name__, url_prefix='/api/v1/salaries')

# Initialize repository and service
sal_repo = SalaryRepository()
sal_service = SalaryService(sal_repo)

@salaries_bp.route('', methods=['GET'])
def get_all():
    salaries = sal_service.get_all_salaries()
    # Include calculated total_salary in response
    result = []
    for s in salaries:
        d = s.__dict__
        d['total_salary'] = s.total_salary
        result.append(d)
    return jsonify(result), 200

@salaries_bp.route('/<sal_id>', methods=['GET'])
def get_one(sal_id):
    sal = sal_service.get_salary_by_id(sal_id)
    if not sal:
        return jsonify({"error": "Salary record not found"}), 404
    d = sal.__dict__
    d['total_salary'] = sal.total_salary
    return jsonify(d), 200

@salaries_bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    try:
        new_sal = sal_service.create_salary(data)
        d = new_sal.__dict__
        d['total_salary'] = new_sal.total_salary
        return jsonify({"message": "Salary record created", "salary": d}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@salaries_bp.route('/<sal_id>', methods=['PUT'])
def update(sal_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    
    updated = sal_service.update_salary(sal_id, data)
    if not updated:
        return jsonify({"error": "Salary record not found"}), 404
        
    d = updated.__dict__
    d['total_salary'] = updated.total_salary
    return jsonify({"message": "Salary record updated", "salary": d}), 200

@salaries_bp.route('/<sal_id>', methods=['DELETE'])
def delete(sal_id):
    success = sal_service.delete_salary(sal_id)
    if not success:
        return jsonify({"error": "Salary record not found"}), 404
    return jsonify({"message": "Salary record deleted"}), 200