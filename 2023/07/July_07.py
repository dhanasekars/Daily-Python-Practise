""" 
Created on : 07/07/23 4:42 pm
@author : ds  
"""
data = {"a": 30, "b": 15, "c": 55}


def pie_chart(test_data):
    """
    A pie chart is a circular graphical representation of a dataset,
    where each category frequency is represented by a slice (or circular sector)
    with an amplitude in degrees given by the single frequency percentage over the total of frequencies.
    :param: test_data: a dictionary data with keys being the data categories (represented by letters)
    and values being the data frequencies.
    :return:the same dictionary with values transformed in degrees instead of frequencies
    """

    total = sum(test_data.values())
    return {key: round((value/total)*360, 1) for (key, value) in test_data.items()}


print(pie_chart(test_data=data))