#Unit Testing 

# import unittest 

# def add(a,b):
#     return a + b

# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2,3), 5)

# if __name__ == '__main__':
#     unittest.main()

'''
self.assertEqual(a,b)
self.assertTrue(value)
self.assertFalse(value)
self.assertIn(value, collection)
self.assertIsNone(value)
self.assertRaises(ValueError)
'''

#Problem 1

#calculator.py
# def add(a,b):
#     return a+b
# def substract(a,b):
#     return a-b
# def multify(a,b):
#     return a*b
# def divide(a,b):
#     return a/b

from calculator import add, substract, multify, divide

print(add(2,5))
print(substract(5,3))
print(multify(3,4))
print(divide(5,5))

#problem 2 

from utils import file_handling
from utils.logging import get_logger

logger = get_logger(__name__)
logger.info('Application instantiated')

text_file = 'file.txt'
logger.info('Writing to the file')
file_handling.write_txt(text_file, 'Mahi | 99')

file_handling.read_txt(text_file)
logger.info('Reading the file - file.txt')

json_file = 'employee.json'
employee_details = {
    'name': 'Mahi', 'salary':44444,
    'name': 'Ra', 'salary':34444
}

file_handling.write_json(json_file, employee_details)
logger.info('Writing to json_file')

loaded_json = file_handling.read_json(json_file)
logger.info('Successfully loaded the json')






#problem 3 

import config

print(config.api_url)

import constants

print(constants.ERROR)

print(constants.SUCCESS)

'''
Interview Questions

module - any python files is considered as a module. instead of making one big file. we can make multiple modules to make it modular 
package - a package can contain multiple modules with __init__.py and that can be reused in the other packages by importing that package
import module - we are importing the complete module 
from module import .. - we are importing the specific function, methods inside the module 
if __name__ == '__main__' -> to order to execute the module only when we required. otherwise it will get excuted wheneven we import the module
virtual env -> in order to deal with the different versions of the packages and lib, we use virtual env. bez, some project would need v2.0 of a package and some would need v3.0
unit testing -> we develop the testing class with the test_ functions in order to test whether the code is working as code. we normally use the assert keyword to check the status
unit testing - testing each small functionalities separately. small and fast 
integration testing - testing how the individual parts are work together. large and slow
assertions -> assertions are the boolean expressions that is the ultimate checkpoint which compares the actual results vs the results we wanted
we split the code into modules -> for maintainability, readability, reusability, code ownership and easier testing
'''