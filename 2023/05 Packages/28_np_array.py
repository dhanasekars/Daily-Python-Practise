""" 
Created on : 28/05/23 5:34 pm
@author : ds  
"""

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

addition_of_array = array1 + array2
multiplication_of_array = array1 * array2

print("Addition Results:", addition_of_array)
print("Multiplication Results:", multiplication_of_array)

# check the output
print(np.array_equal(addition_of_array, [ 7, 9, 11, 13, 15]))
print(np.array_equal(multiplication_of_array, [ 6, 14, 24, 36, 50]))