""" 
Created on : 05/09/22 5:09 PM
@author : ds  
"""


def reverse_words(s):
    return ' '.join(s.strip().split()[::-1])



print(reverse_words("the sky is blue      "))