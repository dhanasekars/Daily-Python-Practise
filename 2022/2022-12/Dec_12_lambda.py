""" 
Created on : 12/12/22 4:32 AM
@author : ds
https://edabit.com/challenge/cToBLderwJrpqML8w
"""
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


class PremierLeague:

    def __init__(self):
        self.teams = None

    def champions(self, teams):
        self.teams = teams
        return max(teams, key=lambda x: (x['wins'] * 3 + x['draws'], x['scored'] - x['conceded']))['name']
