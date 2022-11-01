""" 
Created on : 31/10/22 2:49 PM
@author : ds  
"""
import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
data = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St."
txtin = "242Edabit2345can3443be3254324addictive!"


def negative_lookbehind(txt):
    return len(re.findall(r'(?<!good) cookie', ",".join(txt)))


def negative_lookbehind1(txt):
    return re.findall(r'(?<![-\d+])\d+', txt)


def digit_character_class(txt):
    return re.findall(r"\d+ [^.]+.", txt)


def digit_character_class1(txt):
    return " ".join(re.findall(r"\D+", txt))


print(digit_character_class1(txtin))


