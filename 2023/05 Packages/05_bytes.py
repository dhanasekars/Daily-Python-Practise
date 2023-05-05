""" 
Created on : 27/04/23 7:54 am
@author : ds  
"""

# https://betterprogramming.pub/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686

a_string = "A unicode string! 😊😊"

print(a_string)

a_bytes = a_string.encode()

print(a_bytes)

a = b'abcdefghj'
b = 'abcdefghj'

for i in range(0, len(a)):
    print(a[i])
a_b = b'spam,egg,spam,bacon,spam,lobster'
print(a_b.count(b'hello'))
print(a_b.split(sep=b','))
print(list(a_b))