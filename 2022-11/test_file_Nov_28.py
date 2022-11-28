""" 
Created on : 28/11/22 5:17 AM
@author : ds  
"""

import unittest
from Nov_28 import Employee


class testEmployee(unittest.TestCase):

    def test_firstname(self):
        emp_1 = Employee("John", "Smith")
        self.assertEqual(emp_1.firstname, "John")

    def test_lastname(self):
        emp_1 = Employee("John", "Smith")
        self.assertEqual(emp_1.lastname, "Smith")

    def test_fullname(self):
        emp_1 = Employee("John", "Smith")
        self.assertEqual(emp_1.fullname, "John Smith")

    def test_email(self):
        emp_1 = Employee("John", "Smith")
        self.assertEqual(emp_1.email, "john.smith@company.com")
