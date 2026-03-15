from typing import List, Optional, Dict, Any
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from uuid import uuid4

class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self._repo = repository

    def get_all_employees(self) -> List[Employee]:
        return self._repo.get_all()

    def get_employee_by_id(self, emp_id: str) -> Optional[Employee]:
        return self._repo.get_by_id(emp_id)

    def create_employee(self, data: Dict[str, Any]) -> Employee:
        # Generate a unique ID if not provided
        if 'id' not in data or not data['id']:
            data['id'] = str(uuid4())
        
        new_emp = Employee(
            id=data['id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            gender=data['gender'],
            date_of_birth=data['date_of_birth'],
            department_id=data.get('department_id')
        )
        return self._repo.create(new_emp)

    def update_employee(self, emp_id: str, data: Dict[str, Any]) -> Optional[Employee]:
        existing = self._repo.get_by_id(emp_id)
        if not existing:
            return None
        
        # Update only provided fields
        updated_emp = Employee(
            id=existing.id,
            first_name=data.get('first_name', existing.first_name),
            last_name=data.get('last_name', existing.last_name),
            gender=data.get('gender', existing.gender),
            date_of_birth=data.get('date_of_birth', existing.date_of_birth),
            department_id=data.get('department_id', existing.department_id)
        )
        return self._repo.update(emp_id, updated_emp)

    def delete_employee(self, emp_id: str) -> bool:
        return self._repo.delete(emp_id)