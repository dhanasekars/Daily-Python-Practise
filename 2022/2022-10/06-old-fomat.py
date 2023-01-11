""" 
Created on : 06/10/22 5:26 AM
@author : ds  
"""

data_rgb = (0, 0, 0)
data_hexa = "#456789"


def rgb_or_hex(*args):
    if len(args) == 1:
        return tuple(int(i, 16) for i in [args[0][1:3], args[0][3:5], args[0][5:7]])
    else:
        # hexa = "".join(hex(i)[2:4] for i in args)
        # return f"#{hexa}"
        return "#{}".format("".join(hex(i)[2:4].zfill(2) for i in args))


print(rgb_or_hex(data_hexa))