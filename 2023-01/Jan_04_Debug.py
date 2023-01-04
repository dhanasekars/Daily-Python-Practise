""" 
Created on : 04/01/23 3:13 PM
@author : ds
https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
"""


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels is not 0:
            if num_vowels % 2 == 0:
                score += 2
            else:
                score += 1
        else:
            score = 0
    return score




