""" 
Created on : 20/03/23 8:51 am
@author : ds  
"""

def gradient_descent(derivative_func, initial_guess, multiplier=0.02, precision=0.0001, max_iter=300):
    """
    For a given cost function, the function will calculate and return a tuple containing
    Local minimum, list of guesses, gradient(slope) list for each guess
    :param derivative_func:
    :param initial_guess:
    :param multiplier:
    :param precision:
    :param max_iter:
    :return: tuple
    """
    # get the derivative of cost_func
    new_x = initial_guess
    x_list = [new_x]
    slope_list = [derivative_func(new_x)]

    for i in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - multiplier * gradient
        step_size = abs(new_x - previous_x)

        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))

        # stop if the new x is close enough to the previous one
        if step_size < precision:
            break

    return new_x, x_list, slope_list

def f(x):
    return x ** 4 - 4 * x ** 2 + 5


def df(x):
    return 4*x**3 - 8*x


local_min, list_x, derivative_list = \
    gradient_descent(derivative_func=df, initial_guess=0.5, multiplier=0.02, precision=0.00001)

print("Local minimum occurs at : ", local_min)
print("Slope / df(x) value at the local minimum is ", df(local_min))
print("f(x) / cost at this local minimum is:", f(local_min))
print("Total Iteration :", len(list_x))
