""" 
Created on : 09/09/22 6:05 AM
@author : ds  
"""

test_data = [{"product": "Milk","quantity": 1, "price": 1.50},
    {"product": "Eggs", "quantity": 12, "price": 0.10},
    {"product": "Bread", "quantity": 2, "price": 1.60},
    {"product": "Cheese", "quantity": 1, "price": 4.50}

]


def get_total_price(groceries):
    return round(sum([i['quantity'] * i['price'] for i in groceries]),1)


print(get_total_price(test_data))