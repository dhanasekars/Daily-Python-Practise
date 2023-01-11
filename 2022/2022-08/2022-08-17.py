""" 
Created on : 17/08/22 5:45 AM
@author : ds  
"""


def consecutive_zeros(x):
    lt = sorted(x.split('1'))
    return len(lt[-1])


# shorter solution
# def consecutive_zeros(bin_str):
#    return max([len(s) for s in bin_str.split("1")])
