""" 
Created on : 25/07/23 9:31 am
@author : ds  
"""

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass

    return wrapper


def say_whee():
    print("Whee!!!!")


say_whee = not_during_the_night(say_whee)
say_whee()