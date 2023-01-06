""" 
Created on : 06/01/23 10:12 AM
@author : ds
https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

"""


test = "abracadabra"


def mutate_string(string, position, character):
    """
    Read a given string, change the character at a given index and print the modified string
    :param string: the string to change
    :param position: the index to insert the character at
    :param character: the character to insert
    :return:
    """
    try:
        new_string = list(string)
        new_string[position] = character
    except IndexError:
        return "Position provided is invalid!"
    else:
        return "".join([i for i in new_string])

