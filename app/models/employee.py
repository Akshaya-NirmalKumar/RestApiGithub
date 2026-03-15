from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Employee:
    id: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: str  # Format: YYYY-MM-DD
    department_id: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())