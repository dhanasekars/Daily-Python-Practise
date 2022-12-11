""" 
Created on : 12/12/22 4:32 AM
@author : ds  
"""

import unittest
from Dec_12_lambda import PremierLeague

class testPremierLeague(unittest.TestCase):

    def test_champions(self):
        data = [
            {
                "name": "Manchester United",
                "wins": 30,
                "loss": 3,
                "draws": 5,
                "scored": 88,
                "conceded": 20,
            },
            {
                "name": "Arsenal",
                "wins": 24,
                "loss": 6,
                "draws": 8,
                "scored": 98,
                "conceded": 29,
            },
            {
                "name": "Chelsea",
                "wins": 22,
                "loss": 8,
                "draws": 8,
                "scored": 98,
                "conceded": 29,
            }
        ]
        PL_2022 = PremierLeague()
        self.assertEqual(PL_2022.champions(teams=data), "Manchester United")

