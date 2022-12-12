""" 
Created on : 13/12/22 4:58 AM
@author : ds  
"""

import unittest
from Dec_13_dictionary import DictionaryClass


class test_DictionaryClass(unittest.TestCase):

    def test_setter(self):
        dictionaryclass = DictionaryClass()
        dictionaryclass.set_input({"a": 44, "b": 45, "c": 46}, "d")
        self.assertEqual(dictionaryclass.dict_in, {"a": 44, "b": 45, "c": 46})
        self.assertEqual(dictionaryclass.keytocheck, "d")

    def test_getter(self):
        dictionaryclass = DictionaryClass()
        dictionaryclass.set_input({"a": 44, "b": 45, "c": 46}, "d")
        self.assertEqual(dictionaryclass.get_details(), ({"a": 44, "b": 45, "c": 46}, "d"))

    def test_has_key(self):
        dictionaryclass = DictionaryClass()
        dictionaryclass.set_input({"a": 44, "b": 45, "c": 46}, "c")
        self.assertEqual(dictionaryclass.has_key(), True)
        dictionaryclass.set_input({"a": 44, "b": 45, "c": 46}, "d")
        self.assertEqual(dictionaryclass.has_key(), False)

    def test_swap_dict(self):
        dictionaryclass = DictionaryClass()
        dictionaryclass.set_input({"Mubashir": "Name",
                                   "31": "Age",
                                   "Male": "Sex",
                                   "Pilot": "Job",
                                   "Matt": "Name",
                                   "40": "Age",
                                   "Programmer": "Job"
                                   }, "Name")
        self.assertEqual(dictionaryclass.swap_dict(), {
            "Name": ["Mubashir", "Matt"],
            "Age": ["31", "40"],
            "Sex": ["Male"],
            "Job": ["Pilot", "Programmer"]
        })
