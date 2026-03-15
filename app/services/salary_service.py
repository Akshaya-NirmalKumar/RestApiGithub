from typing import List, Optional, Dict, Any
from app.models.salaries import Salary
from app.repositories.salary_repository import SalaryRepository
from uuid import uuid4

class SalaryService:
    def __init__(self, repository: SalaryRepository):
        self._repo = repository

    def get_all_salaries(self) -> List[Salary]:
        return self._repo.get_all()

    def get_salary_by_id(self, sal_id: str) -> Optional[Salary]:
        return self._repo.get_by_id(sal_id)

    def create_salary(self, data: Dict[str, Any]) -> Salary:
        # Generate ID if not provided
        if 'id' not in data or not data['id']:
            data['id'] = str(uuid4())
            
        new_sal = Salary(
            id=data['id'],
            employee_id=data['employee_id'],
            basic_salary=float(data['basic_salary']),
            bonus=float(data.get('bonus', 0)),
            allowances=float(data.get('allowances', 0))
        )
        return self._repo.create(new_sal)

    def update_salary(self, sal_id: str, data: Dict[str, Any]) -> Optional[Salary]:
        existing = self._repo.get_by_id(sal_id)
        if not existing:
            return None
        
        updated_sal = Salary(
            id=existing.id,
            employee_id=existing.employee_id, 
            basic_salary=float(data.get('basic_salary', existing.basic_salary)),
            bonus=float(data.get('bonus', existing.bonus)),
            allowances=float(data.get('allowances', existing.allowances))
        )
        return self._repo.update(sal_id, updated_sal)

    def delete_salary(self, sal_id: str) -> bool:
        return self._repo.delete(sal_id)