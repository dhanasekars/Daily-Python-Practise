""" 
Created on : 11/11/22 5:59 AM
@author : ds  
"""

from Nov_12 import programmer
import unittest


class TestProgrammer(unittest.TestCase):

    def test_salary(self):
        self.assertEqual(2500, prog.salary)
        self.assertEqual(2500, prog1.salary)

    def test_workhours(self):
        self.assertEqual(5, prog.work_hours)
        self.assertEqual(6, prog1.work_hours)

    def test_delete(self):
        self.assertEqual("oof, 2500, 5", prog.__del__())
        self.assertEqual("oof, 2500, 6", prog1.__del__())

    def test_compare(self):
        self.assertEqual("5", prog.compare(prog1))
        self.assertEqual("4", prog.compare(prog2))


prog = programmer(2500, 5)
prog1 = programmer(2500, 6)
prog2 = programmer(2000, 6)
prog3 = programmer(2500, 4)