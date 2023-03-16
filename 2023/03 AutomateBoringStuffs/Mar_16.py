""" 
Created on : 16/03/23 10:10 am
@author : ds  
"""

def sing(n):
    lst = []
    line1 = '{} bottles of beer on the wall, {} bottles of beer.'
    line2 = 'Take one down and pass it around, {} bottles of beer on the wall.'
    line3 = ''
    for i in range(n, 0, -1):
        lst.append(line1.format(i, i))
        lst.append(line2.format(i - 1))
        lst.append(line3)
    return lst


print(sing(99))
