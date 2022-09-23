""" 
Created on : 23/09/22 5:31 AM
@author : ds  
"""
link = "https://edabit.com/challenges"
text = "Hello"


def tidy_link(url, name, hover_text="h"):
    return '[' + name + '](' + url + " " + '"' + hover_text + '")' if hover_text else '[' + name + '](' + url + ')'


print(tidy_link(link, text))

