""" 
Created on : 30/03/23 1:44 pm
@author : ds  
"""


def email_slicer(email):
    return f"Your username is {email.split('@')[0]} and domain is {email.split('@')[1]}"
