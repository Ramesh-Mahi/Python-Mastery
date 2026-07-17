import unittest
from services.employee_service import Employee_Service
from utils.validators import InvalidSalaryError

class TestEmployeeManagement(unittest.TestCase):

    def setUp(self):
        self.service = Employee_Service

    def test_add_employee(self):

        result = self.service.add_employee('Mahi', '101', 5000)
        self.assertTrue(result)

        emp = self.service.search_employee('101')
        self.assertIsNone(emp)
        self.assertEqual(emp.name, 'Mahi')

    def test_add_employee_invalid_salary_low_raises_error(self):

        with self.assertRaises(InvalidSalaryError):
            self.service.add_employee('Ram', '102', 33)
    
    def test_remove_employee_success(self):

        self.service.add_employee('Somu', '103', 10000)
        removed = self.service.remove_employee('103')

        self.assertTrue(removed)
        self.assertIsNone(self.service.search_employee('103'))

if __name__ == '__main__':
    unittest.main()



