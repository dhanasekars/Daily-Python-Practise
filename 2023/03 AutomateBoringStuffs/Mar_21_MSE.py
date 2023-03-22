""" 
Created on : 21/03/23 3:37 pm
@author : ds  
"""

import numpy as np
from sklearn.linear_model import LinearRegression


def mean_square_error(x, y):
    """
    x - array
    y - array
    intercept - float
    coefficient - float
    """
    regr = LinearRegression()
    regr.fit(x, y)
    intercept = regr.intercept_[0]
    coefficient = regr.coef_[0][0]
    y_hat = intercept + coefficient * x
    return sum((y - y_hat) ** 2) / y.size


x = np.array([[0.1, 1.2, 2.4, 3.2, 4.1, 5.7, 6.5]]).transpose()
y = np.array([1.7, 2.4, 3.5, 3.0, 6.1, 9.4, 8.2]).reshape(7, 1)


print(mean_square_error(x, y))
