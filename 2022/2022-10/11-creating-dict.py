""" 
Created on : 11/10/22 9:13 AM
@author : ds  
"""

data = "Christmas is the 25th of December"


def atbash(txt):
    """
    The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in
    the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
    :param txt: String
    :return: atbash cipher text as string
    """
    # using Zip to create a dictionary of mapping only for alphabets
    dictChars = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'))
    # using list comprehension, replace alphabets based on above dictionary only if the character exist in the
    # dictionary else leave the character as is(all those are not alphabetical characters.
    # use join to concatenate the list
    return "".join([c if c not in dictChars else dictChars[c] for c in txt])


print(atbash(data))

