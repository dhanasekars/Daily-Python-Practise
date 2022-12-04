""" 
Created on : 04/12/22 5:22 AM
@author : ds  
"""
import unittest
from Dec_04 import Player

class test_Player(unittest.TestCase):

    def test_class_initiation(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        self.assertEqual(alice.name, "Alice")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(alice._Player__hp, 110)
        self.assertEqual(bob._Player__hp, 100)
        self.assertEqual(alice._Player__en, 50)
        self.assertEqual(bob._Player__en, 60)
        self.assertEqual(alice.armor, 10)
        self.assertEqual(bob.armor, 20)

    def test_set_hp(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        alice.set_hp(200)
        self.assertEqual(alice._Player__hp, 200)
        self.assertEqual(bob.set_hp(-0.01), "Unexpected health levels")
        self.assertEqual(bob.set_hp(1000.2), "Unexpected health levels")

    def test_set_en(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        alice.set_en(200)
        self.assertEqual(alice._Player__en, 200)
        self.assertEqual(bob.set_en(-0.01), "Unexpected energy levels")
        self.assertEqual(bob.set_en(1000.2), "Unexpected energy levels")

    def test_get_hp(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        self.assertEqual(alice.get_hp(), 110)
        self.assertEqual(bob.get_hp(), 100)

    def test_get_en(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        self.assertEqual(alice.get_en(), 50)
        self.assertEqual(bob.get_en(), 60)

    def test_get_hpPerc(self):
        alice = Player('Alice', 110, 50, 10)
        bob = Player('Bob', 100, 60, 20)
        self.assertEqual(alice.get_hpPerc(), 11.00)
        self.assertEqual(bob.get_hpPerc(), 10.00)
        alice.set_hp(991)
        self.assertEqual(alice.get_hpPerc(), 99.10)
        bob.set_hp(1.5)
        self.assertEqual(bob.get_hpPerc(), 0.15)





