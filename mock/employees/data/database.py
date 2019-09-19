from abc import ABC, abstractmethod
import os
import json
from dataclasses import dataclass
from typing import Dict, Any, List


class Employee(ABC):
    identifier: int
    first_name: str
    last_name: str
    email: str
    gender: str
    country: str
    car: str

    @abstractmethod
    def to_dict(self) -> Dict[Any, Any]:
        pass

    @abstractmethod
    def has_keyword(self,  keyword: str) -> bool:
        pass


@dataclass(order=True)
class TargetEmployee(Employee):
    identifier: int
    first_name: str
    last_name: str
    email: str
    gender: str
    country: str
    car: str

    def to_dict(self) -> Dict[Any, Any]:
        return self.__dict__

    def has_keyword(self, keyword: str) -> bool:
        for attribute in self.to_dict().values():  # type: str
            if keyword in str(attribute):
                return True
        return False


class NonExistedEmployee(Employee):
    def __init__(self) -> None:
        self._employee: Employee = TargetEmployee(-1, "null", "null", "null", "null", "null", "null")

    def to_dict(self) -> Dict[Any, Any]:
        return self._employee.to_dict()

    def has_keyword(self, keyword: str) -> bool:
        return self._employee.has_keyword(keyword)


class Employees:
    _storage: str = "employees.json"

    def __init__(self, *, limit: int) -> None:
        self._limit = limit
        self._employees: Dict[int, Employee] = {}

    @property
    def truncated(self) -> int:
        return self._limit

    def search_by_keyword(self, keyword: str) -> List[Employee]:
        return list(filter(lambda employee: employee.has_keyword(keyword), self._serialized().values()))[: self._limit]

    def search_by_id(self, identifier: int) -> Employee:
        if identifier > 1000:
            return NonExistedEmployee()
        return self._serialized()[identifier]

    def to_dict(self, employees: List[Employee]) -> List[Dict[Any, Any]]:
        if not employees:
            return [{}]
        return list(map(lambda employee: employee.to_dict(), employees))[: self._limit]

    def _serialized(self) -> Dict[int, Employee]:
        storage_file: str = os.path.join(os.path.dirname(__file__), self._storage)
        with open(storage_file, encoding="utf-8") as stream:
            for employee_record in json.load(stream):  # type: Dict[Any, Any]
                employee: Employee = TargetEmployee(*employee_record.values())
                self._employees[employee.identifier] = employee
        return self._employees
