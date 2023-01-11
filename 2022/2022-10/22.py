""" 
Created on : 22/10/22 9:43 AM
@author : ds  
"""

data_string = "45"
data_int = 34


def int_to_str(num):
    return int(num)


def str_to_int(num):
    return str(num)


print(int_to_str(data_int))
print(str_to_int(data_string))


# other interesting solution
# str, int = int, str
# int_to_str = int
# str_to_int = str