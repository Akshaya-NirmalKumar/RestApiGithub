import json
import os
import threading
from typing import List, Optional, Dict, Any
from app.models.departments import Department
from app.repositories.base_repository import BaseRepository

class DepartmentRepository(BaseRepository[Department]):
    def __init__(self, data_dir: str = "./data"):
        self._file_path = os.path.join(data_dir, "departments.json")
        self._lock = threading.Lock()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        if not os.path.exists(self._file_path):
            with open(self._file_path, 'w') as f:
                json.dump([], f)

    def _read_data(self) -> List[Dict[str, Any]]:
        with self._lock:
            with open(self._file_path, 'r') as f:
                return json.load(f)

    def _write_data(self, data: List[Dict[str, Any]]):
        with self._lock:
            with open(self._file_path, 'w') as f:
                json.dump(data, f, indent=2)

    def get_all(self) -> List[Department]:
        raw = self._read_data()
        return [Department(**item) for item in raw]

    def get_by_id(self, entity_id: str) -> Optional[Department]:
        raw = self._read_data()
        for item in raw:
            if item['id'] == entity_id:
                return Department(**item)
        return None

    def create(self, entity: Department) -> Department:
        raw = self._read_data()
        raw.append(entity.__dict__)
        self._write_data(raw)
        return entity

    def update(self, entity_id: str, entity: Department) -> Optional[Department]:
        raw = self._read_data()
        for i, item in enumerate(raw):
            if item['id'] == entity_id:
                raw[i] = entity.__dict__
                self._write_data(raw)
                return entity
        return None

    def delete(self, entity_id: str) -> bool:
        raw = self._read_data()
        initial_len = len(raw)
        raw = [item for item in raw if item['id'] != entity_id]
        if len(raw) < initial_len:
            self._write_data(raw)
            return True
        return False