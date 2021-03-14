"""
Test file 'employee.py' to see if it is working
"""
import unittest
from employee import Employee
class TestEmployeeCase(unittest.TestCase):
    def setUp(self):
       """make an employee to use in tests."""
       self.eric=Employee('eric','matthes',65000)
    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_rise()
        self.assertEqual(self.eric.annual_salary,70000) 
    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_rise(10000)
        self.assertEqual(self.eric.annual_salary,75000)
if __name__ == '__main__':
    unittest.main()