from typing import List, Optional, Dict, Any
from app.models.departments import Department
from app.repositories.department_repository import DepartmentRepository

class DepartmentService:
    def __init__(self, repository: DepartmentRepository):
        self._repo = repository

    def get_all_departments(self) -> List[Department]:
        return self._repo.get_all()

    def get_department_by_id(self, dept_id: str) -> Optional[Department]:
        return self._repo.get_by_id(dept_id)

    def create_department(self, data: Dict[str, Any]) -> Department:
        new_dept = Department(
            id=data['id'],
            department_name=data['department_name'],
            location=data['location']
        )
        return self._repo.create(new_dept)

    def update_department(self, dept_id: str, data: Dict[str, Any]) -> Optional[Department]:
        existing = self._repo.get_by_id(dept_id)
        if not existing:
            return None
        
        updated_dept = Department(
            id=existing.id,
            department_name=data.get('department_name', existing.department_name),
            location=data.get('location', existing.location)
        )
        return self._repo.update(dept_id, updated_dept)

    def delete_department(self, dept_id: str) -> bool:
        return self._repo.delete(dept_id)