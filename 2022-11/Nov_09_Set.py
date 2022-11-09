""" 
Created on : 08/11/22 1:20 PM
@author : ds  
"""

# Vowel Families https://edabit.com/challenge/uwFHSRewNpmBNvbME
# Prep :
#    Look at set() sorted()


def same_vowel_group(w):
    result = []
    lst = ['a', 'e', 'i', 'o', 'u']
    vowels = ([c for c in set(w[0]) if c in lst])
    check_vowels = list((set(lst)-set(vowels)))
    for c in w:
        if set(vowels) <= set(c):
            result.append(c)
    for c in result[1:]:
        if set.intersection(set(check_vowels),set(c)):
            result.remove(c)
    return result


print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))


# Better way to use set
# def same_vowel_group(w):
# 	first = set(w[0]) & set('aeiou')
# 	return [i for i in w if set(i) & set('aeiou') == first]

