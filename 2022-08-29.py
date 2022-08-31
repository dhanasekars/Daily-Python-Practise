""" 
Created on : 29/08/22 5:33 PM
@author : ds  
"""

import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

expression = input()  # the expression to calculate
input_values = [x.strip() for x in expression.split('+')]
final_list = []
unit_order = {'um': 0, 'mm': 1, 'cm': 2, 'dm': 3, 'm': 4, 'km': 5}
unit_difference = {0: 1, 1: 1000, 2: 100, 3: 1000, 4: 1000000, 5: 1000000000}
for i in input_values:
    if i[-2:-1] in ['u', 'm', 'c', 'd', 'k']:
        final_list.append(i[:-2])
        final_list.append(i[-2:])
    else:
        final_list.append(i[:-1])
        final_list.append(i[-1:])
# print(final_list)
diff = abs(unit_order[final_list[1]] - unit_order[final_list[3]])

if unit_order[final_list[1]] >= unit_order[final_list[3]]:
    if final_list[1] == 'km' and final_list[3] == 'dm':
        final_list[0] = float(final_list[0]) * 100
    if final_list[1] == 'dm' and final_list[3] == 'um':
        final_list[0] = float(final_list[0]) * 100
    if final_list[1] == 'cm' and final_list[3] == 'mm':
        final_list[0] = (float(final_list[0]) * 10) / 1000

    final_list[0] = float(final_list[0]) * unit_difference[diff]
    final_list[0] = float("{:.5f}".format(final_list[0]))
    output_unit = final_list[3]
else:
    final_list[2] = float(final_list[2]) * unit_difference[diff]
    final_list[2] = float("{:.5f}".format(final_list[2]))
    output_unit = final_list[1]

final_list[2] = float(final_list[2])
final_list[2] = float("{:.5f}".format(final_list[2]))
output_float = final_list[0] + final_list[2]

if output_float % 1 == 0:
    output_float = str(output_float)
    output_value = output_float.split('.')[0] + output_unit
else:
    output_value = str(output_float) + output_unit

print(output_value)






# Write an answer using print
# To debug: print("Debug messages..., file=sys.stderr, flush=True)
