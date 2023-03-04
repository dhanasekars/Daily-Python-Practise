""" 
Created on : 03 AutomateBoringStuffs/10/22 7:12 AM
@author : ds  
"""

data = "burak"


def encrypt(word):
    """
    An encryption algorithm. Encryption logic
    1. Reverse the string
    2. Vowels are replaced with mapping characters
    3. Add 'aca' at the end of the string

    :param word: All inputs are strings, no uppercase
    :return: Encrypted string
    """
    vowel_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    # 'join' to append characters.
    # IF else in list comprehension to replace vowels with encrypted keys.Finally, append "aca"

    return "".join([vowel_dict[c] if c in vowel_dict.keys() else c for c in word[::-1]]) + "aca"


print(encrypt(data))