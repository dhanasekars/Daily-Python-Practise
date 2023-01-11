""" 
Created on : 29/10/22 4:33 AM
@author : ds  
"""
import re

data = "/users/edabit/filepy.py"
txt1 = "The end of the story."
txt2 = "We viewed the rendering at the end."


def check_py_extension(path):
    """
     regular expression that will match the files with the extension .py or .pyw.
     You must use the RegEx line anchor $, which matches the end of a string.
    :param path: String
    :return: Bool
    """
    return bool(re.search(r'\.py(w)?$', path))


def line_anchor(path):
    """
    regular expression that will match any file located within the "users/edabit" directory.
    You must use at least one RegEx line anchor.
    :param data:
    :return:
    """
    return bool(re.match(r"^/users/edabit/", path))


def boundary_assertions(txt):
    """
     regular expression that ensures the word "end" is inside of another word (e.g. "bending").
     You must use RegEx boundary assertions. Non-word characters such as !, ?, etc. cannot be boundaries.
    :param txt:
    :return:
    """
    print(txt)
    return bool(re.search(r"\Bend\B", txt))


print(boundary_assertions(txt1))

