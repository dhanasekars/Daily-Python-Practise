""" 
Created on : 15/11/22 5:28 AM
@author : ds  
"""

import unittest
from Nov_15_class_kwargs__dict_update import Employee


class TestEmployee(unittest.TestCase):

    def test_name(self):
        john = Employee("John Doe")
        self.assertEqual('John', john.name)

    def test_lastname(self):
        john = Employee("John Doe")
        self.assertEqual('Doe', john.lastname)

    def test_salary(self):
        mary = Employee("Mary Major", salary=120000)
        self.assertEqual('1200000', mary.salary)

    def test_height(self):
        richard = Employee("Richard Roe", salary=110000, height=178)
        self.assertEqual('178', richard.height)

    def test_nationality(self):
        giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
        self.assertEqual('Italian',giancarlo.nationality)