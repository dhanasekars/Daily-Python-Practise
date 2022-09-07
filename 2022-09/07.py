""" 
Created on : 07/09/22 5:43 AM
@author : ds  
"""

profit_input = ({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
})


def profit(info):
    print(info.values())
    return round((info["sell_price"] - info["cost_price"]) * info['inventory'])


print(profit(profit_input))


# Interesting one from solutions


def profit(info):
    [a, b, c] = info.values()
    return round((b - a) * c)
