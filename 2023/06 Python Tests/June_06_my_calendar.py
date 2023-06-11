""" 
Created on : 06/06/23 10:31 am
@author : ds  
"""
import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    return 0 <= today.weekday() < 5

def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None

