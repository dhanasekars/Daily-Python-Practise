""" 
Created on : 02/10/22 5:47 AM
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

    # Calculate the frequency total
    # Calculate percentage of every category frequency dividing it by the frequencies total.
    # Transform every percentage in degrees multiplying it for 360.
    # Dict comprehension is used
    # new_dict = {new_key: new_value for (key, value) in dict.items() if test}

    total = sum(test_data.values())
    return {key: round((value/total)*360, 1) for (key, value) in test_data.items()}


print(pie_chart(test_data=data))