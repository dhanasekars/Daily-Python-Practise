""" 
Created on : 01/06/23 10:36 am
@author : ds  
"""


def reverse_words(s):
    return ' '.join(s.strip().split()[::-1])



print(reverse_words("the sky is blue      "))

