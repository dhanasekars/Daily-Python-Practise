""" 
Created on : 28/06/23 6:23 pm
@author : ds  
"""
import json

with open('hereGoes.json', 'r') as f:
    json_object = json.load(f)
    print(len(json_object['key1']['key2']))