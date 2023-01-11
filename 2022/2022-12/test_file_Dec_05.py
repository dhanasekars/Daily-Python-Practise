""" 
Created on : 05/12/22 5:24 AM
@author : ds  
"""

from Dec_05 import PlayerSkills
import unittest


class testPlayerSkills(unittest.TestCase):

    def test_learning_skills(self):
        alice = PlayerSkills('Alice', 600, 500, 300)
        alice.learnSkill("fireball",
                         {"damage": 23, "penetration": 1.2,
                          "heal": 5, "cost": 15, "desc": "a firey magical attack"})
        self.assertEqual(alice.stats, {'damage': 23, 'penetration': 1.2, 'heal': 5,
                                       'cost': 15, 'desc': 'a firey magical attack'})
        self.assertEqual(alice.skills_name, "fireball")

