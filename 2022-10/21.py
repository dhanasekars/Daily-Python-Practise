""" 
Created on : 21/10/22 2:28 PM
@author : ds  
"""

data = {
    "round1": {"me": 40, "spouse": 39},
    "round2": {"me": 9, "spouse": 10},
    "round3": {"me": 9, "spouse": 10}}


def determine_who_cursed_the_most(d):
    """
    Given a dict with three rounds, with nested dicts as your score per round,
    return who cursed the most based on the following:
    :param d:
    :return: string
    """
    me = sum([v1 for k, v in d.items() for k1, v1 in v.items() if k1 == "me"])
    spouse = sum([v1 for k, v in d.items() for k1, v1 in v.items() if k1 == "spouse"])
    return "ME!" if me > spouse else "SPOUSE!" if spouse > me else "DRAW"


# m = sum([d[i]['me'] for i in d])
# s = sum([d[i]['spouse'] for i in d])


print(determine_who_cursed_the_most(data))
