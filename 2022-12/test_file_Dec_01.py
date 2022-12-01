""" 
Created on : 01/12/22 4:59 AM
@author : ds  
"""

import unittest
from Dec_01 import Memories


class testMemories(unittest.TestCase):

    def test_remember(self):
        m1 = Memories()
        m1.add(name="Shane", gender="M", catch_phrase="bazinga")
        m1.add(work="None", love_life=0)
        m1.add(adress="car")
        self.assertEqual(m1.remember("work"), "None")
        self.assertEqual(m1.remember("gender"), "M")
        self.assertEqual(m1.remember("lover"), False)




