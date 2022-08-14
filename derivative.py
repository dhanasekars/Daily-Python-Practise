""" 
Created on : 12/08/22 4:37 PM
@author : ds  
"""
x = 1

f = x**6/6-3*x**4-2*x**3/3+27*x**2/2+18*x-30
df = x**5-12*x**3-2*x**2+27*x+18


output = 1 - f/df

print(output)