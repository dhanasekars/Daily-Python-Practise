""" 
Created on : 18/01/23 5:44 AM
@author : ds  
"""

import unittest
from Jan_18 import countApplesAndOranges


class TestCountApplesAndOranges(unittest.TestCase):
    def testCountApplesAndOranges(self):
        s = 7
        t = 11
        a = 5
        b = 15
        apples = [-2, 2, 1]
        oranges = [5, -6]
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        countApplesAndOranges(s, t, a, b, apples, oranges)
        output = capturedOutput.getvalue().strip()
        self.assertEqual(output, '1\n1')