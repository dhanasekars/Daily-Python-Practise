""" 
Created on : 18/04/23 10:16 am
@author : ds  
"""
# http://www.pythonchallenge.com/pc/return/balloons.html
#  difference is brightness so
# http://www.pythonchallenge.com/pc/return/brightness.html

import gzip, difflib
from urllib.request import urlopen, Request


text = gzip.open("18_delta.txt.gz")
print(type(text))
print(text)

d1, d2 = [], []

for line in text:
    d1.append(line[:53].decode()+"\n")
    d2.append((line[56:].decode()))

compare = difflib.Differ().compare(d1, d2)

f = open("f.png", "wb")
f1 = open("f1.png", "wb")
f2 = open("f2.png", "wb")

for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)