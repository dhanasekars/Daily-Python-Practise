""" 
Created on : 05/12/22 5:24 AM
@author : ds  
"""

from Dec_04 import Player


class PlayerSkills(Player):

    def __init__(self, name, health, energy, armor):
        super().__init__(name, health, energy, armor)
        self.stats = None
        self.skills_name = None

    def learnSkill(self, skills_name, stats: dict):
        self.skills_name = skills_name
        self.stats = stats
        return


alice = PlayerSkills('Alice', 600, 500, 300)
bob = PlayerSkills("Bob", 100, 60, 20)
alice.learnSkill("fireball",
                         {"damage": 23, "penetration": 1.2,
                          "heal": 5, "cost": 15, "desc": "a firey magical attack"})

alice.fireball(bob)