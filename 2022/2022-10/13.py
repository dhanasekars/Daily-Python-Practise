""" 
Created on : 13/10/22 6:05 AM
@author : ds  
"""

data = (["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon")


def remove_letters(letters, word):
    """
    Create a function that takes a list and string.
    The function should remove the letters in the string from the list, and return the list.
    :param: letters: A list
    :param word: String
    :return: string
    """

    # for c in word:
    #     if c in letters:
    #         letters.remove(c)
    # return letters
    # The above is in list comprehension below
    [letters.remove(c) for c in word if c in letters]
    return letters


print(remove_letters(data[0], data[1]))
