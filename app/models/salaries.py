from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Salary:
    id: str
    employee_id: str
    basic_salary: float
    bonus: float = 0.0
    allowances: float = 0.0
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    @property
    def total_salary(self) -> float:
        return self.basic_salary + self.bonus + self.allowances