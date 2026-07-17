import config 

class InvalidSalaryError(Exception):
    # here we will handle the salary errors
    pass 

def validate_salary(salary):
    if not isinstance(salary, (float, int)):
        raise InvalidSalaryError(f'The salary is incorrect format - not integer and float')
    if salary < config.MIN_SALARY or salary > config.MAX_SALARY:
        raise InvalidSalaryError(f'The given salary is either above or below the limit')
    return True


