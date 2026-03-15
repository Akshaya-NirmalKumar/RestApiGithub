from .health import health_bp
from .auth import auth_bp
from .students import students_bp
from .employees import employees_bp
from .departments import departments_bp  # <-- Make sure this is 'departments' (plural)
from .salaries import salaries_bp

__all__ = ['health_bp', 'auth_bp', 'students_bp', 'employees_bp', 'departments_bp', 'salaries_bp']