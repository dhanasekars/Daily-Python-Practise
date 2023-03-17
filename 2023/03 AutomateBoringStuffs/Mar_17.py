""" 
Created on : 17/03/23 10:40 am
@author : ds  
"""


def gradient_descent(derivative_func, initial_guess, multiplier, precision, iteration):
    """

    :param iteration:
    :param derivative_func: a function that is a derivative of cost function
    :param initial_guess:
    :param multiplier:
    :param precision:
    :return: a tuple
    """
    new_x = initial_guess
    x_list = [new_x]
    slope_list = [derivative_func(new_x)]

    for n in range(iteration):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - multiplier * gradient
        step_size = abs(new_x - previous_x)

        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))

        if step_size < precision:
            break

    return new_x, x_list, slope_list


# Let's run this for g(x) = x^4 - 4x^2 + 5
# dg(x) = 4x^3 - 8x

def g(x):
    return x ** 4 - 4 * x ** 2 + 5


def dg(x):
    return 4 * x ** 3 - 8 * x


if __name__ == '__main__':
    local_min, list_x, derivative_list \
        = gradient_descent(derivative_func=dg, initial_guess=0.5, multiplier=0.02, precision=0.00001, iteration=500)
    print(local_min, g(local_min))