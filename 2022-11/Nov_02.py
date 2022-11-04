""" 
Created on : 02/11/22 5:46 AM
@author : ds  
"""
data = [5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]


def discount(lst):
    # Find how many products can be free
    total_products = len(lst)
    total_free_products = total_products // 3
    # Products to be billed
    to_bill = sorted(lst)[total_free_products:]
    # Total purchase
    total_purchase = sum(lst)
    # Percentage discount
    discount_percentage = ((total_purchase - sum(to_bill)) / total_purchase)
    # Return the Discounted price list
    return [round(i - i*discount_percentage, 2) for i in lst]

    # Pythonic calculation of percentage
    # per = sum(sorted(lst)[len(lst)//3:])/sum(lst)



print(discount(data))

