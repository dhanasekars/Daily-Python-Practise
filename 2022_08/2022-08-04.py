""" 
Created on : 04/08/22 6:06 PM
@author : ds  
"""


def online_count(statuses):
    count = 0
    for key,value in statuses.lost_items():
        if value == 'online':
            count = count + 1
    return count




statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Alice3": "online",
    "Bob3": "offline",
    "Eve3": "online",
}




print(online_count(statuses=statuses))