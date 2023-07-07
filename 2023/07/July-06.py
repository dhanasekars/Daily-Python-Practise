""" 
Created on : 06/07/23 7:32 am
@author : ds  
"""
import itertools

listA = ["create", "Read", "Update", "Delete"]
perm = itertools.permutations(listA)

for i in list(perm):
    print(i)