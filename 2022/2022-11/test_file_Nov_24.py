""" 
Created on : 24/11/22 5:25 AM
@author : ds  
"""

from Nov_24 import Testpaper
import unittest


class test_Testpaper(unittest.TestCase):
    def test_paper(self):
        paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "50%")
        self.assertEqual(paper1.subject, "Maths")
        self.assertEqual(paper1.markscheme, ["1A", "2C", "3D", "4A", "5A"])
        self.assertEqual(paper1.pass_mark, "50%")

