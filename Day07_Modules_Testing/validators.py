class AgeRestricted(Exception):
    pass
class NotInteger(Exception):
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise NotInteger(f'{age} is not a integer')
    if age < 18:
        raise AgeRestricted(f'{age} is below 18')
    return True

def validate_salary(salary):
    if not isinstance(salary, int):
        raise AgeRestricted(f'{salary} is not a integer')
    return True


