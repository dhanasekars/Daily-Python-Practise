""" 
Created on : 12/01/23 9:52 AM
@author : ds  
"""
import unittest
from Jan_12_staircase import staircase

class test_staircase(unittest.TestCase):

    def test_staircase_1(self):
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        staircase(1)
        output = capturedOutput.getvalue().strip()
        self.assertEqual(output, "#")

    def test_staircase_6(self):
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        staircase(6)
        output = capturedOutput.getvalue().strip()
        self.assertEqual(output, '#\n    ##\n   ###\n  ####\n #####\n######')

    def test_staircase_2(self):
        with self.assertLogs() as cm:
            staircase(2)
            self.assertEqual(cm.output, ['INFO:root: #', 'INFO:root: ##'])