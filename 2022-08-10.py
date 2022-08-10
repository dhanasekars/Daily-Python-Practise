""" 
Created on : 10/08/22 5:47 PM
@author : ds  
"""


def is_anagram(a,b):
    global var
    if len(a) == len(b):
        a = sorted(a)
        b = sorted(b)
        for i in range(len(a)):
            if a[i] != b[i]:
                var = False
            else:
                var = True

    else:
        var = False
    return var


print(is_anagram("typhoon", "opythonr"))


# Shortest solutions

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)