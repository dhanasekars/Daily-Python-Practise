""" 
Created on : 24/09/22 5:42 AM
@author : ds  
"""

lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
test_data = "Oscar"


def alphabet_index(alphabet, string):
    val = alphabet.index(string.lower()[0])
    for c in string.lower():
        if val < alphabet.index(c):
            val = alphabet.index(c)
    return str(val+1) + alphabet[val]


print(alphabet_index(lst, test_data))