
class Employee:
    def __init__(self, emp_id:str, name:str, salary:int):
        self.emp_id = emp_id
        self.name = name 
        self.salary = salary
    
    def __str__(self):
        return f'Employee Details - {self.emp_id} - {self.name} - {self.salary}'
