""" 
Created on : 14/07/23 4:36 am
@author : ds  
"""

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)
print(first())
print(second())