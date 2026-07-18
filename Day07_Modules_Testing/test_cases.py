import unittest

from calculator import add, divide

class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3,3),6)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3,-3),-6)
    
    def test_add_mix_numbers(self):
        self.assertEqual(add(3,-4),-1)
    
    def test_divide_numbers(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)
        
        