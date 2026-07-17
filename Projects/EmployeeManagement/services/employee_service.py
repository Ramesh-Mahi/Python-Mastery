from models.employee import Employee
from utils.logger import get_logger
from utils.validators import validate_salary

logger = get_logger(__name__)

class Employee_Service:

    def __init__(self):
        self._records = {}

    def add_employee(self, name:str, emp_id:str, salary:int) -> bool:
        if emp_id in self._records:
            logger.warning(f'The Employee addition is aborted, employee - {self.name} already exists')
            return False
        
        try:
            validate_salary(self.salary)
            new_emp = Employee(emp_id, name, salary)
            self._records[emp_id] = new_emp
            print(self._records)
            print(self._records.items())
            logger.info(f'New employee successfully added - {self.name}')
        
        except Exception as e:
            logger.error(f'Falied to add the employee..{name}: {e}')
            raise
    
    def remove_employee(self, emp_id:str) -> bool:
        if emp_id in self._records:
            removed = self._records.pop(emp_id)
            logger.info(f'Successfully removed the employee record: {removed}')
            return True
        
        logger.warning(f'Deletion failed. No record matching the employee ID {emp_id}')
        return False
    
    def search_employee(self, emp_id: str) -> Employee:
        logger.info(f'Searching the catalog..{emp_id}')
        return self._records.get(emp_id, None)
    
    def list_all_records(self):
        return list(self._records.values())
    
