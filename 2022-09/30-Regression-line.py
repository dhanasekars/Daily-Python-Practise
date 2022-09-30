""" 
Created on : 30/09/22 6:54 AM
@author : ds  
"""

test_data = [(1, 2), (4, 3), (-1, -1), (-2, -3)]


def regression_line(lst):
    """
    For a given list of tuples of x and y values, the function returns the best regression line fit as string
    y = mx + b and the R-squared
    :param lst: List of tuples. Tuples are (x,y) coordinates.
    :return: A tuple - (Equation of line best fit, R-squared)
    """
    datapoints = len(lst)
    x_ = round(sum([i[0] for i in lst])/datapoints, 2)
    y_ = round(sum([i[1] for i in lst])/datapoints, 2)
    xy_ = round(sum([i[0] * i[1] for i in lst])/datapoints, 2)
    xx_ = round(sum([i[0] * i[0] for i in lst])/datapoints, 2)
    m = round((xy_ - x_ * y_) / (xx_ - pow(x_, 2)), 2)
    b = round(y_ - m * x_,2)
    y_list = [i[1] for i in lst]
    y_predicted_list = [round(m*i[0] + b, 2) for i in lst]
    sqrd_error_with_line = 0
    for i in range(len(lst)):
        sqrd_error_with_line = sqrd_error_with_line + round(pow((y_list[i]-y_predicted_list[i]), 2), 2)
    sqrd_from_y_ = round(sum([pow(i-y_,2) for i in y_list]), 2)
    r_squared = 1 - sqrd_error_with_line / sqrd_from_y_
    return f"y = {m}x {b:+}", f"{round(r_squared,2)*100} %"


print(regression_line(test_data))

