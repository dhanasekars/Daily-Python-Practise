""" 
Created on : 27/04/23 11:36 pm
@author : ds  
"""
from googlefinance import getQuotes
from yahoo_finance import Share
import json

print(json.dumps(getQuotes('AAPL'),indent=2))

# Learned google finance API is shut down