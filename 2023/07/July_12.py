""" 
Created on : 12/07/23 6:35 pm
@author : ds  
"""

def parent():
    print("Printing from parent() function")

    def first_child():
        print(f"Print from {first_child.__name__} function")

    def second_child():
        print("Printing from second_child() function")

    second_child()
    first_child()


parent()
first_child()