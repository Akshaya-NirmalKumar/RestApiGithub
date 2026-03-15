from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Department:
    id: str
    department_name: str
    location: str
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())